%{
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>  // Added for exit function
%}

/* Define patterns for tokenization */
DIGIT       [0-9]
LETTER      [a-zA-Z]
IDENTIFIER  {LETTER}({LETTER}|{DIGIT})*
NUMBER      {DIGIT}+
KEYWORD     "if"|"else"|"while"|"return"|"int"|"float"|"char"
WHITESPACE  [ \t\n]+

%%

{KEYWORD}    { printf("Keyword: %s\n", yytext); }
{IDENTIFIER} { printf("Identifier: %s\n", yytext); }
{NUMBER}     { printf("Number: %s\n", yytext); }
[+\-*/=]     { printf("Operator: %s\n", yytext); }
[(){};]      { printf("Symbol: %s\n", yytext); }
{WHITESPACE} {/* Ignore whitespace */}
.            { printf("Unknown Token: %s\n", yytext); }

%%

int main() {
    printf("Enter input:\n");
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}
