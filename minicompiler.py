# Simple Mini-Compiler for arithmetic expressions (e.g., "3 + 5 * 2")

# Stage 1: Lexical Analyzer (Tokenizer)
def tokenize(code):
    tokens = []
    i = 0
    while i < len(code):
        if code[i].isspace():
            i += 1
        elif code[i] in '()+-*/':
            tokens.append(('OPERATOR', code[i]))
            i += 1
        elif code[i].isdigit():
            num = ''
            while i < len(code) and code[i].isdigit():
                num += code[i]
                i += 1
            tokens.append(('NUMBER', int(num)))
        else:
            raise ValueError(f"Unknown character: {code[i]}")
    return tokens

# Stage 2: Parser (Converts tokens to Abstract Syntax Tree)
def parse(tokens):
    return parse_add_sub(tokens)

def parse_add_sub(tokens):
    node = parse_mul_div(tokens)
    
    while tokens and tokens[0][0] == 'OPERATOR' and tokens[0][1] in '+-':
        op = tokens.pop(0)[1]
        node = ('BIN_OP', op, node, parse_mul_div(tokens))
    
    return node

def parse_mul_div(tokens):
    node = parse_number(tokens)
    
    while tokens and tokens[0][0] == 'OPERATOR' and tokens[0][1] in '*/':
        op = tokens.pop(0)[1]
        node = ('BIN_OP', op, node, parse_number(tokens))
    
    return node

def parse_number(tokens):
    if tokens[0][0] == 'NUMBER':
        return ('NUMBER', tokens.pop(0)[1])
    elif tokens[0][1] == '(':
        tokens.pop(0)  # Remove '('
        node = parse_add_sub(tokens)
        tokens.pop(0)  # Remove ')'
        return node
    else:
        raise ValueError("Expected number or parentheses")

# Stage 3: Code Generator (Converts AST to Python executable code)
def generate_code(node):
    if node[0] == 'NUMBER':
        return str(node[1])
    elif node[0] == 'BIN_OP':
        left = generate_code(node[2])
        right = generate_code(node[3])
        return f"({left} {node[1]} {right})"
    else:
        raise ValueError("Unknown node type")

# Main compiler function
def compile(code):
    print(f"Source: {code}")
    
    # Lexical Analysis
    tokens = tokenize(code)
    print(f"Tokens: {tokens}")
    
    # Parsing
    ast = parse(tokens.copy())  # Use copy to preserve original tokens
    print(f"AST: {ast}")
    
    # Code Generation
    compiled_code = generate_code(ast)
    print(f"Compiled: {compiled_code}")
    
    # Execute
    result = eval(compiled_code)
    print(f"Result: {result}")
    return result

# Example usage
if __name__ == "__main__":
    while True:
        expr = input("Enter expression (or 'quit'): ")
        if expr.lower() == 'quit':
            break
        try:
            compile(expr)
        except Exception as e:
            print(f"Error: {e}")