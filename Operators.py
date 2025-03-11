def main():
    # Arithmetic Operators
    print("\nArithmetic Operators:")
    a = int(input())
    b = int(input())
    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    print(f"Division: {a} / {b} = {a / b}")
    print(f"Floor Division: {a} // {b} = {a // b}")
    print(f"Modulus: {a} % {b} = {a % b}")
    print(f"Exponentiation: {a} ** {b} = {a ** b}")

    # Comparison Operators
    print("\nComparison Operators:")
    print(f"Equal: {a} == {b} -> {a == b}")
    print(f"Not Equal: {a} != {b} -> {a != b}")
    print(f"Greater Than: {a} > {b} -> {a > b}")
    print(f"Less Than: {a} < {b} -> {a < b}")
    print(f"Greater Than or Equal: {a} >= {b} -> {a >= b}")
    print(f"Less Than or Equal: {a} <= {b} -> {a <= b}")

    # Logical Operators
    print("\nLogical Operators:")
    x, y = True, False
    print(f"AND: {x} and {y} -> {x and y}")
    print(f"OR: {x} or {y} -> {x or y}")
    print(f"NOT: not {x} -> {not x}")

    # Bitwise Operators
    print("\nBitwise Operators:")
    print(f"Bitwise AND: {a} & {b} -> {a & b}")
    print(f"Bitwise OR: {a} | {b} -> {a | b}")
    print(f"Bitwise XOR: {a} ^ {b} -> {a ^ b}")
    print(f"Bitwise NOT: ~{a} -> {~a}")
    print(f"Left Shift: {a} << 1 -> {a << 1}")
    print(f"Right Shift: {a} >> 1 -> {a >> 1}")

    # Assignment Operators
    print("\nAssignment Operators:")
    c = a
    print(f"Assign: c = {a} -> c = {c}")
    c += b
    print(f"Add and Assign: c += {b} -> c = {c}")
    c -= b
    print(f"Subtract and Assign: c -= {b} -> c = {c}")
    c *= b
    print(f"Multiply and Assign: c *= {b} -> c = {c}")
    c /= b
    print(f"Divide and Assign: c /= {b} -> c = {c}")
    c //= b
    print(f"Floor Divide and Assign: c //= {b} -> c = {c}")
    c %= b
    print(f"Modulus and Assign: c %= {b} -> c = {c}")
    c **= b
    print(f"Exponentiate and Assign: c **= {b} -> c = {c}")

    # Identity Operators
    print("\nIdentity Operators:")
    print(f"Is: {a} is {b} -> {a is b}")
    print(f"Is Not: {a} is not {b} -> {a is not b}")

    # Membership Operators
    print("\nMembership Operators:")
    my_list = [1, 2, 3, 4, 5]
    print(f"In: 3 in {my_list} -> {3 in my_list}")
    print(f"Not In: 6 not in {my_list} -> {6 not in my_list}")

if __name__ == "__main__":
    main()
