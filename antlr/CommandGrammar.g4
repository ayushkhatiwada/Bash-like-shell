grammar CommandGrammar;
// could also use Lark instead of Antlr
// These parsers allow you to use the visitor pattern


/*
 * Parser Rules
 */







/*
 * Lexer Rules
 */

PIPE: '|';
SINGLE_QUOTE: '\'';
DOUBLE_QUOTE: '"';
SEMI_COLON: ';';
LESS_THAN: '<';     // Change to REDIRECT_INPUT: '<'; ?
GREATER_THAN: '>';  // Change to REDIRECT_OUTPUT: '>'; ?
BACKTICK: '`';

