#중위 표기식을 후위 표기식으로 전환
# from CH4.Postfix import postfix
from CH4.Stack import Stack

def precedence(op): #연산 우선순위 지정
    if op=='(' or op == ')': return 0
    elif op == '+' or op == '-' : return 1
    elif op == '*' or op == '/': return 2
    else: return -1

def infix2Postfix(ex): #중위표기식 입력
    s = Stack() #연산자 스택 괄호 포함
    out = [] #출력용 배열

    for token in ex:
        if token == '(':
            s.push(token)
        elif token == ')':
            while not s.isEmpty():
                op = s.pop()
                if op == '(': break
                else: out.append(op)

        elif token in "+-*/":
            while not s.isEmpty():
                op = s.peek()
                if precedence(token) <= precedence(op):
                    out.append(op)
                    s.pop()
                else: break
            s.push(token)

        else: out.append(token)

    while not s.isEmpty():
        out.append(s.pop())

    return out

ex = "(2+3)*4"
print(infix2Postfix(ex))
# print(postfix(infix2Postfix(ex)))