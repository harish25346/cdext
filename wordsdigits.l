%{
#include <stdio.h>
int word_count = 0, line_count = 0, digit_count = 0;
int uppercase_count = 0, lowercase_count = 0;
%}

/* Token Definitions */
DIGIT      [0-9]
UPPERCASE  [A-Z]
LOWERCASE  [a-z]
WORD       [a-zA-Z]+
NEWLINE    \n
WHITESPACE [ \t]

%%

{DIGIT}      { digit_count++; }
{UPPERCASE}  { uppercase_count++; }
{LOWERCASE}  { lowercase_count++; }
{WORD}       { word_count++; }
{NEWLINE}    { line_count++; }
{WHITESPACE} {/* Ignore spaces, count words separately */}

%%

int main() {
    printf("Enter text (Press Ctrl+D to end input):\n");
    yylex();
    
    printf("\nStatistics:\n");
    printf("Number of words: %d\n", word_count);
    printf("Number of lines: %d\n", line_count);
    printf("Number of digits: %d\n", digit_count);
    printf("Uppercase letters: %d\n", uppercase_count);
    printf("Lowercase letters: %d\n", lowercase_count);

    return 0;
}

int yywrap() {
    return 1;
}
