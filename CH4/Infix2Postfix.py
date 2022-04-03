from CH4.Postfix import postfix


def precedence(op):
    if op == '(' or op == ')':
        return 0
    elif op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    else :
        return -1

def infix2Postfix(ex):
    from Stack import Stack
    operatorStack = Stack()
    output = []
    for token in ex:
        if token == '(':
            operatorStack.push(token)
        elif token == ')':
            while not operatorStack.isEmpty():
                op = operatorStack.pop()
                if op == '(': break
                else:
                    output.append(op)
        elif token in "+-*/":
            while not operatorStack.isEmpty():
                op = operatorStack.peek()
                if precedence(op) >= precedence(token):
                    output.append(op)
                    operatorStack.pop()
                else:
                    break
            operatorStack.push(token)
        else:
            output.append(token)

    while not operatorStack.isEmpty():
        output.append(operatorStack.pop())

    return ''.join(output)

ex = "(2+3)*4"
print(infix2Postfix(ex))
print(postfix(infix2Postfix(ex)))