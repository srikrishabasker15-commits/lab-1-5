
# ==========================================
# Compiler Design Lab
# Elimination of Ambiguity, Left Recursion
# and Conversion to Right Recursion
# ==========================================

# ---------- PART 1: ELIMINATION OF AMBIGUITY ----------
def eliminate_ambiguity():
    print("\n--- Elimination of Ambiguity ---")

    ambiguous = {
        "E": ["E+E", "E*E", "id"]
    }

    print("\nAmbiguous Grammar:")
    for nt, prods in ambiguous.items():
        print(nt, "→", " | ".join(prods))

    print("\nUnambiguous Grammar (using precedence):")
    unambiguous = {
        "E": ["E+T", "T"],
        "T": ["T*F", "F"],
        "F": ["id"]
    }

    for nt, prods in unambiguous.items():
        print(nt, "→", " | ".join(prods))


# ---------- PART 2: ELIMINATION OF LEFT RECURSION ----------
def eliminate_left_recursion(non_terminal, productions):
    print("\n--- Elimination of Left Recursion ---")

    alpha = []
    beta = []

    for prod in productions:
        if prod.startswith(non_terminal):
            alpha.append(prod[len(non_terminal):])
        else:
            beta.append(prod)

    if not alpha:
        print("No left recursion found.")
        return

    print("\nAfter Removing Left Recursion:")
    print(f"{non_terminal} → ", end="")
    for b in beta:
        print(f"{b}{non_terminal}' | ", end="")
    print()

    print(f"{non_terminal}' → ", end="")
    for a in alpha:
        print(f"{a}{non_terminal}' | ", end="")
    print("ε")


# ---------- PART 3: CONVERSION TO RIGHT RECURSION ----------
def convert_to_right_recursion():
    print("\n--- Conversion to Right Recursion ---")

    print("\nOriginal (Left Recursive Grammar):")
    print("E → E + T | T")

    print("\nRight Recursive Grammar:")
    print("E  → T E'")
    print("E' → + T E' | ε")


# ---------- MAIN FUNCTION ----------
def main():
    eliminate_ambiguity()

    eliminate_left_recursion(
        non_terminal="E",
        productions=["E+T", "T"]
    )

    convert_to_right_recursion()


if __name__ == "__main__":
    main()
