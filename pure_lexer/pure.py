# -*- coding: utf-8 -*-
"""
    pure_lexer.pure
    ~~~~~~~~~~~~~~~

    Lexer for the Pure language.
"""

import re

from pygments.lexer import Lexer, RegexLexer, bygroups, include, do_insertions
from pygments.token import Text, Comment, Operator, Keyword, Name, \
     String, Number, Punctuation, Literal, Generic

class PureLexer(RegexLexer):
    """
    For the Pure language.
    """

    name = 'Pure'
    aliases = ['pure']
    filenames = ['*.pure']
    mimetypes = ['text/x-pure']

    keywords = ['infix[lr]?', 'outfix', 'prefix', 'postfix', 'nonfix',
                'namespace', 'private', 'public', 'case', 'const', 'def',
                'else', 'end', 'extern', 'if', 'let', 'of', 'otherwise',
                'then', 'using', 'when', 'with', 'type', 'interface']

    # These aren't really keywords but we want them to stick out anyway.
    keywords2 = ['catch', 'throw']

    primitives = ['bigint', 'bool', 'char', 'short', 'int', 'long',
                  'float', 'double', 'expr', 'string', 'pointer', 'void',
                  'int8', 'int16', 'int32', 'int64',
                  'matrix', 'dmatrix', 'cmatrix', 'imatrix',
                  'smatrix', 'nmatrix']

    commands = ['break', 'bt', 'cd', 'clear', 'del', 'dump', 'help', 'ls',
                'mem', 'override', 'pwd', 'quit', 'run', 'save', 'show',
                'stats', 'trace', 'underride']

    tokens = {
        'root': [
            # Whitespace and comments.
            (r'\s+', Text),
            (r'/[*](.|\n)*?[*]/', Comment.Multiline),
            (r'//.*?\n', Comment.Single),
            (r'^#!.*?\n', Comment.Preproc),

            # Inline foreign language code. Avoid highlighting these.
            (r'%<(.|\n)*?%>', Text),

            # Interactive prompts and error messages.
            (r'^> ?$', Generic.Prompt), # lone prompt at end of snippet
            (r'^> ', Generic.Prompt, 'prompt'),
            (r'^[^"\s][^,\n]*, line [0-9]+: ', Generic.Error, 'error'),

            # Various kinds of keywords and built-in punctuation.
            (r'\b(%s)\b' % '|'.join(keywords), Keyword.Reserved),
            (r'\b(%s)\b' % '|'.join(keywords2), Name.Builtin),
            (r'\b(%s)\b' % '|'.join(primitives), Keyword.Type),
            (r'[@;]|::', Punctuation),

            # Numbers.
            (r'\b(\d*\.\d+|(\d+\.\d*|\.\d+|\d+)[eE][+-]?\d+)\b', Number.Float),
            (r'\b(0x[0-9a-fA-F]+L?)\b', Number.Hex),
            (r'\b(0[0-7]+L?)\b', Number.Oct),
            (r'\b(0[bB][01]+L?)\b', Number.Binary),
            (r'\b(\d+L?)\b', Number.Integer),

            # Strings.
            (r'"', String, 'string'),

            # Specials (thunks, closures, pointers, etc.).
            (r'#<[^>\n]+>', Keyword.Type),

            # Pretty much everything else can be a legal (utf-8) identifier or
            # operator symbol in Pure, we just highlight these as text for now.
            (r'\S', Text),
        ],
        'string': [
            (r'"', String, '#pop'),
            (r'\\([\\abfnrtv"\']|&[^;]+;|\([^)]+\))', String.Escape),
            (r'\\(0x[0-9a-fA-F]+|0[0-7]+|0[bB][01]+|\d+)', String.Escape),
            (r'[^\\"\n]+', String), # all other characters
            (r'\\\n', String), # line continuation
            (r'\\', String), # stray backslash
        ],
        'prompt': [
            # Interactive interpreter commands. No highlighting.
            (r'(%s)\b.*?\n' % '|'.join(commands), Text, '#pop'),
            # Interactively typed pragmas.
            (r'#!.*?\n', Comment.Preproc, '#pop'),
            # Anything else is highlighted as usual.
            ('', Text, '#pop'),
        ],
        'error': [
            (r'.*?\n', Text, '#pop'),
        ]
    }
