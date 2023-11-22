grammar CommandGrammar;

// antlr4 -Dlanguage=Python3 CommandGrammar.g4 - Generates lexer, parser, and listener files

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
WHITESPACE : [ \t\r]+;

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


/*
 * Parser Rules
 */

/*
<command> ::= <pipe> | <seq> | <call>
<pipe> ::= <call> "|" <call> | <pipe> "|" <call>
<seq>  ::= <command> ";" <command>
<call> ::= ( <non-keyword> | <quoted> ) * - ignore this call, use other call
 */
// might not need EOF
command : (pipe | seq | call)? EOF;
pipe : call PIPE call | call PIPE pipe;

// Error: The following sets of rules are mutually left-recursive [pipe] and [command, seq] ???
seq : (pipe | call) SEMI_COLON (pipe | seq | call)?;

// two call commands in read me? 
// * means it can appear 0 or more times
//call : (NON_KEYWORD | quoted)*;
call: WHITESPACE* (redirection WHITESPACE*)* argument (WHITESPACE* atom)* WHITESPACE*;



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
singleQuoted : SINGLE_QUOTE (~(NEWLINE | SINGLE_QUOTE))+ SINGLE_QUOTE;
backQuoted : BACKQUOTE (~(NEWLINE | BACKQUOTE))+ BACKQUOTE;

// master shell code differs, does not include DOUBLE_QUOTE in ~(... "doubleQuoted: DOUBLE_QUOTE (backQuoted | ~(NEWLINE | BACKTICK))* DOUBLE_QUOTE;"
// think SP has made mistake here
// UZK code differs from this - doubleQuoted : '"' (((~[`"\n]) | '\\"')+ | backQuoted)* '"'; 
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

//call: WHITESPACE? (redirection WHITESPACE?)* argument (WHITESPACE? atom)* WHITESPACE?;
atom : redirection | argument;
// + means it can appear 1 or more times
argument : (quoted | UNQUOTED)+;

// redirection could be simplified to: (LESS_THAN | GREATER_THAN) WHITESPACE? argument;
// ? means it can appear 0 times or once
redirection : LESS_THAN WHITESPACE* argument | GREATER_THAN WHITESPACE* argument;
