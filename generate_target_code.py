def generate_target_code():
    # Sample input
    intermediate = [
        "t1 = a + b",
        "t2 = t1 - c",
        "y = t2"
    ]

    reg_map = {}  # To store which variable is in which register
    reg_num = 1
    target = []

    for line in intermediate:
        lhs, rhs = line.split('=')
        lhs = lhs.strip()
        parts = rhs.strip().split()

        if len(parts) == 3:
            op1, operator, op2 = parts
            reg = f"R{reg_num}"
            reg_num += 1

            if operator == '+':
                target.append(f"ADD {reg}, {op1}, {op2}")
            elif operator == '-':
                target.append(f"SUB {reg}, {op1}, {op2}")
            elif operator == '*':
                target.append(f"MUL {reg}, {op1}, {op2}")
            elif operator == '/':
                target.append(f"DIV {reg}, {op1}, {op2}")

            reg_map[lhs] = reg

        elif len(parts) == 1:
            var = parts[0]
            reg = reg_map.get(var, var)
            target.append(f"MOV {lhs}, {reg}")

    # Print target code
    for line in target:
        print(line)


generate_target_code()
