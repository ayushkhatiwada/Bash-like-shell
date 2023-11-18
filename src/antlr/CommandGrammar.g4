grammar CommandGrammar;
// These parsers allow you to use the visitor pattern


/*
 * Parser Rules
 */


/*
<command> ::= <pipe> | <seq> | <call>
<pipe> ::= <call> "|" <call> | <pipe> "|" <call>
<seq>  ::= <command> ";" <command>
<call> ::= ( <non-keyword> | <quoted> ) *
 */
command : pipe | seq | call;
pipe : (call PIPE call) | (pipe PIPE call);
seq : command SEMI_COLON command;

// two call commands in read me? 
call : (NON_KEYWORD | quoted)*;

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////    


/*
<quoted> ::= <single-quoted> | <double-quoted> | <backquoted>
<single-quoted> ::= "'" <non-newline and non-single-quote> "'"
<backquoted> ::= "`" <non-newline and non-backquote> "`"
<double-quoted> ::= """ ( <backquoted> | <double-quote-content> ) * """
 */
quoted : singleQuoted | doubleQuoted | backQuoted;

//<single-quoted> ::= "'" <non-newline and non-single-quote> "'"
// non-newline and non-single-quote
// ~p /\ ~ q = ~(p \/ q)
// non-newline and non-single-quote = non (new-line or single-quote)
singleQuoted : SINGLE_QUOTE ~(NEWLINE | SINGLE_QUOTE)* SINGLE_QUOTE;

backQuoted : BACKQUOTE ~(NEWLINE | BACKQUOTE)* BACKQUOTE;

// master shell code differs, does not include DOUBLE_QUOTE in ~(... "doubleQuoted: DOUBLE_QUOTE (backQuoted | ~(NEWLINE | BACKTICK))* DOUBLE_QUOTE;"
// think SP has made mistake here
doubleQuoted : DOUBLE_QUOTE ( backQuoted | ~(NEWLINE | DOUBLE_QUOTE | BACKQUOTE) )* DOUBLE_QUOTE;

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////


/*
<call> ::= [ <whitespace> ] [ <redirection> <whitespace> ]* <argument> [ <whitespace> <atom> ]* [ <whitespace> ]
<atom> ::= <redirection> | <argument>
<argument> ::= ( <quoted> | <unquoted> )+
<redirection> ::= "<" [ <whitespace> ] <argument>
                | ">" [ <whitespace> ] <argument>
 */

// master shell code differs: "call: WHITESPACE? (redirection WHITESPACE?)* argument (WHITESPACE? argument)* (WHITESPACE? redirection)* WHITESPACE?;"
// not sure what SP is doing. Code below agrees with README from sergey and code from XLow 
call : WHITESPACE? (redirection WHITESPACE)* argument (redirection WHITESPACE)* WHITESPACE;


atom : redirection | argument;
argument : (quoted | UNQUOTED)+;

// redirection could be simplified to: (LESS_THAN | GREATER_THAN) WHITESPACE? argument;
redirection : LESS_THAN WHITESPACE? argument | GREATER_THAN WHITESPACE? argument;





/*
 * Lexer Rules
 */

PIPE : '|';
SINGLE_QUOTE : '\'';
DOUBLE_QUOTE : '"';
SEMI_COLON : ';';
LESS_THAN : '<';     // Change to REDIRECT_INPUT: '<'; ?
GREATER_THAN : '>';  // Change to REDIRECT_OUTPUT: '>'; ?

// name this BACTICK OR BACKQUOTE?
BACKQUOTE : '`';

NEWLINE : '\n';

WHITESPACE : [ \t\r]+ -> skip;

/* 
A non-keyword character is any character except for newlines, single quotes,
double quotes, backquotes, semicolons ; and vertical bars | 
*/
NON_KEYWORD : ~[\n'"`;|];


/*
The <unquoted> part of an <argument> can include any characters except
for whitespace characters, quotes, newlines, semicolons ;, vertical bar |, less than < and greater than >.
 */
// remove \t from unquoted?
// this is used in argument in Parser rules
UNQUOTED : ~[ "'`\n;|<>\t]+;
