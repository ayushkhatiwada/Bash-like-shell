grammar ShellGrammar;


/* Lexer Rules */

PIPE: '|';
SINGLE_QUOTE: '\'';
DOUBLE_QUOTE: '"';
SEMI_COLON: ';';
LESS_THAN: '<';
GREATER_THAN: '>';
BACKQUOTE: '`';
NEWLINE: '\n';

WHITESPACE: [ \t\r]+;

NON_KEYWORD: ~[\n'"`;|];
UNQUOTED: ~[ "'`\n;|<>\t]+;


/* Parser Rules */

command: (pipe | seq | call)?;
pipe: call PIPE call | call PIPE pipe;
seq: (pipe | call) SEMI_COLON (pipe | seq | call)?;
call: WHITESPACE* (redirection WHITESPACE*)* argument (WHITESPACE* atom)* WHITESPACE*;

quoted: singleQuoted | doubleQuoted | backQuoted;
singleQuoted: SINGLE_QUOTE (~(NEWLINE | SINGLE_QUOTE))+ SINGLE_QUOTE;
backQuoted: BACKQUOTE (~(NEWLINE | BACKQUOTE))+ BACKQUOTE;
doubleQuoted: DOUBLE_QUOTE (backQuoted | ~(NEWLINE | DOUBLE_QUOTE | BACKQUOTE))* DOUBLE_QUOTE;

atom: redirection | argument;
argument: (quoted | UNQUOTED)+;
redirection: LESS_THAN WHITESPACE* argument | GREATER_THAN WHITESPACE* argument;
