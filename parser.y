%{
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Symbol table for variables
struct {
    char *id;
    int val;
} symtab[100];
int symtab_size = 0;

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}
%}

%union {
    int num;
    char *id;
}

%token <num> NUMBER
%token <id> IDENTIFIER
%token PLUS MINUS MULTIPLY DIVIDE LPAREN RPAREN ASSIGN SEMICOLON

%type <num> expr

%%

program:
    | program statement SEMICOLON
    ;

statement:
    IDENTIFIER ASSIGN expr { 
        // Assign value to variable
        for (int i = 0; i < symtab_size; i++) {
            if (strcmp(symtab[i].id, $1) == 0) {
                symtab[i].val = $3;
                return;
            }
        }
        symtab[symtab_size].id = $1;
        symtab[symtab_size].val = $3;
        symtab_size++;
    }
    ;

expr:
    NUMBER                { $$ = $1; }
    | IDENTIFIER          { 
        // Look up variable value
        for (int i = 0; i < symtab_size; i++) {
            if (strcmp(symtab[i].id, $1) == 0) {
                $$ = symtab[i].val;
                return;
            }
        }
        yyerror("Undefined variable");
        exit(1);
    }
    | expr PLUS expr      { $$ = $1 + $3; }
    | expr MINUS expr     { $$ = $1 - $3; }
    | expr MULTIPLY expr  { $$ = $1 * $3; }
    | expr DIVIDE expr    { $$ = $1 / $3; }
    | LPAREN expr RPAREN  { $$ = $2; }
    ;

%%

int main() {
    printf("Enter arithmetic expressions (e.g., 'x = 2 + 3;'):\n");
    yyparse();
    return 0;
}
