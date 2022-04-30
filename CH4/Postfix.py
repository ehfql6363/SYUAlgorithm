#후위 표기식
from CH4.Stack import Stack

def postfix(ex):
    s = Stack()

    for token in ex:
        if token in "+-*/":
            b = s.pop()
            a = s.pop()
            if token == '+' : s.push(a + b)
            elif token == '-' : s.push(a - b)
            elif token == '*' : s.push(a * b)
            else: s.push(a / b)
        else:
            s.push(float(token))

    return s.pop()

ex = "82/3-32*+"
print(postfix(ex))