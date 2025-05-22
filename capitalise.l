%{
#include <stdio.h>
#include <ctype.h>
%}

%%
[a-z]    { putchar(toupper(*yytext)); }
.        { putchar(*yytext); }
\n       { return 0; }  // Exit on newline
%%

int main(void) {
    printf("Enter a string: \n");
    fflush(stdout);
    yylex();
    printf("\n");
    return 0;
}

int yywrap(void) {
    return 1;
}
