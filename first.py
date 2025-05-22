def find_first(grammar, non_terminal, first_sets, visited):
    if non_terminal in visited:
        return first_sets[non_terminal]
    
    visited.add(non_terminal)
    first_sets[non_terminal] = set()

    if non_terminal not in grammar:
        return set()

    for production in grammar[non_terminal]:
        for symbol in production:
            if symbol.islower() or symbol in {'ε'}:  # Terminal or ε
                first_sets[non_terminal].add(symbol)
                break
            else:  # Non-terminal
                first_sets[non_terminal].update(find_first(grammar, symbol, first_sets, visited) - {'ε'})
                if 'ε' not in first_sets[symbol]:
                    break
        else:
            first_sets[non_terminal].add('ε')  # If all symbols produced ε

    return first_sets[non_terminal]

def main():
    grammar = {
        'S': ['AB', 'a'],
        'A': ['BC', 'ε'],
        'B': ['b'],
        'C': ['c', 'ε']
    }

    first_sets = {}
    visited = set()

    for non_terminal in grammar:
        if non_terminal not in first_sets:
            find_first(grammar, non_terminal, first_sets, visited)

    print("\nFIRST sets:")
    for non_terminal, first_set in first_sets.items():
        print(f"FIRST({non_terminal}) = {first_set}")

if __name__ == "__main__":
    main()
