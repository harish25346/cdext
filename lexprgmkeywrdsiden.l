%{
#include <stdio.h>
#include <string.h>
%}

%option noyywrap

%%
// Keywords
"int"|"float"|"return"|"if"|"else"|"while"|"for"|"char" { 
    printf("Keyword: %s\n", yytext);
}

// Identifiers (variable/function names)
[a-zA-Z_][a-zA-Z0-9_]* { 
    printf("Identifier: %s\n", yytext);
}

// Ignore spaces, tabs, and newlines
[ \t\n]  ;  

// Ignore other characters
.  ;  

%%

int main() {
    printf("Enter the code snippet:\n");
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}
