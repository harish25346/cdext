def simple_optimizer():
    print("Enter each line of code (type 'end' to finish):")

    lines = []
    while True:
        line = input()
        if line.strip().lower() == "end":
            break
        lines.append(line.strip())

    optimized = []
    expr_to_var = {}

    for line in lines:
        if "=" in line:
            var, expr = line.split("=", 1)
            var=var.strip()
            expr=expr.strip()
            # Dead code elimination: e.g., anything * 0
            if "* 0" in expr or "0 *" in expr:
                continue

            # Check if the expression was already computed
            if expr in expr_to_var:
                optimized.append(f"{var} = {expr_to_var[expr]}")
            else:
                expr_to_var[expr] = var
                optimized.append(f"{var} = {expr}")
        else:
            optimized.append(line)

    print("\nOptimized Code:")
    for line in optimized:
        print(line)

# Example run
simple_optimizer()
