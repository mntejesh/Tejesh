def precedence(op):
    if op == '^':
        return 3
    if op == '*' or op == '/':
        return 2
    if op == '+' or op == '-':
        return 1
    return 0
def apply_operator(operand1, operand2, operator):
    if operator == '+':
        return operand1 + operand2
    if operator == '-':
        return operand1 - operand2
    if operator == '*':
        return operand1 * operand2
    if operator == '/':
        return operand1 / operand2
    if operator == '^':
        return operand1 ** operand2

def infix_to_postfix(expression):
    stack = []  # Stack for operators
    output = []  # List for output
    
    for char in expression:
      
        if char.isalnum():
            output.append(char)
        
        elif char == '(':
            stack.append(char)
        
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        
        else:
            while (stack and precedence(stack[-1]) >= precedence(char)):
                output.append(stack.pop())
            stack.append(char)
    
    while stack:
        output.append(stack.pop())

    return ''.join(output)

expression = "a+b*(c^d-e)^(f+g*h)-i"
result = infix_to_postfix(expression)
print("Postfix Expression:", result)
