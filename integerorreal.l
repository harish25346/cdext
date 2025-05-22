%{
#include <stdio.h>
%}

%%
-?[0-9]+\.[0-9]+  { printf("%s is Real\n", yytext); }
-?[0-9]+          { printf("%s is Integer\n", yytext); }
\n                { return 0; }
.                 { /* ignore */ }
%%

int main(void) {
    printf("Enter number: ");
    fflush(stdout);
    yylex();
    return 0;
}

int yywrap(void) { 
    return 1; 
}
