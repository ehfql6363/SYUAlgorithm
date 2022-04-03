def postfix(ex):
    from Stack import Stack
    s = Stack()
    for token in ex:
        if token in "123456789":
            s.push(float(token))
        elif token in "+-*/":
            b = s.pop()
            a = s.pop()
            if token == '+':
                s.push(a+b)
            elif token == '-':
                s.push(a-b)
            elif token == '*':
                s.push(a*b)
            else:
                s.push(a/b)

    return s.pop()

ex = "82/3-32*+"
print(postfix(ex))