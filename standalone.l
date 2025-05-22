%{
#include <stdio.h>
#include <stdlib.h>
%}

/* Token Definitions */
DIGIT       [0-9]
LETTER      [a-zA-Z]
IDENTIFIER  {LETTER}({LETTER}|{DIGIT})*
NUMBER      {DIGIT}+
KEYWORD     "if"|"else"|"while"|"return"|"int"|"float"|"char"
OPERATOR    [+\-*/=]
SYMBOL      [(){};,]
WHITESPACE  [ \t\n]+

%%

{KEYWORD}    { printf("Keyword: %s\n", yytext); }
{IDENTIFIER} { printf("Identifier: %s\n", yytext); }
{NUMBER}     { printf("Number: %s\n", yytext); }
{OPERATOR}   { printf("Operator: %s\n", yytext); }
{SYMBOL}     { printf("Symbol: %s\n", yytext); }
{WHITESPACE} {/* Ignore whitespace */}
.            { printf("Unknown Token: %s\n", yytext); }

%%

int main() {
    printf("Enter input text (Press Ctrl+D to end input):\n");
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}
