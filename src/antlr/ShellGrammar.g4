grammar ShellGrammar;


/* Parser Rules */

command: (pipe | seq | call)?;
pipe: call PIPE call | call PIPE pipe;
seq: (pipe | call) SEMI_COLON (pipe | seq | call)?;
call: WHITESPACE* (redirection WHITESPACE*)* argument (WHITESPACE* atom)* WHITESPACE*;

atom: redirection | argument;
argument: (quoted | UNQUOTED)+;
redirection: LESS_THAN WHITESPACE* argument | GREATER_THAN WHITESPACE* argument;

quoted: singleQuoted | doubleQuoted | backQuoted;
singleQuoted: SINGLE_QUOTE ~(NEWLINE | SINGLE_QUOTE)* SINGLE_QUOTE;
doubleQuoted: DOUBLE_QUOTE (backQuoted | ~(NEWLINE | BACKQUOTE))* DOUBLE_QUOTE;
backQuoted: BACKQUOTE ~(NEWLINE | BACKQUOTE)* BACKQUOTE;


/* Lexer Rules */

UNQUOTED: ~[\t\n "';<>`|]+;

PIPE: '|';
SINGLE_QUOTE: '\'';
DOUBLE_QUOTE: '"';
SEMI_COLON: ';';
LESS_THAN: '<';
GREATER_THAN: '>';
BACKQUOTE: '`';
NEWLINE: '\n';

WHITESPACE: [ \t\r]+;
