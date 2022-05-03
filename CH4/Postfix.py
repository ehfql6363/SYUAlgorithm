#후위 표기식
from CH4.Stack import Stack

def postfix(ex):
    s = Stack() #피연산자만 넣음

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

# test
# ex = "82/3-32*+"
# print(postfix(ex))