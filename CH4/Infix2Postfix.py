#중위 표기식을 후위 표기식으로 전환
# from CH4.Postfix import postfix
from CH4.Stack import Stack

def precedence(op): #연산 우선순위 지정
    if op=='(' or op == ')': return 0
    elif op == '+' or op == '-' : return 1
    elif op == '*' or op == '/': return 2
    else: return -1

def infix2Postfix(ex): #중위표기식 입력
    s = Stack() #연산자 스택. 괄호 포함. 피연산자는 바로 출력 배열로 들어감
    out = [] #출력용 배열

    for token in ex:
        if token == '(':
            s.push(token)
        elif token == ')':
            while not s.isEmpty(): #스택이 빌 때까지 전부 pop
                op = s.pop()
                if op == '(': break #_)괄호와 짝이 맞는 (가 나오면 반복문 중지
                else: out.append(op) # (괄호가 안나오면 출력 배열에 추가

        elif token in "+-*/": #연산자일 경우,
            while not s.isEmpty():
                op = s.peek()
                if precedence(token) <= precedence(op): #기존 연산자가 새로운 연산자보다 우선순위가 높으면
                    out.append(op) #우선순위가 높은(기존) 연산자 출력 배열에 추가
                    s.pop() #기존 연산자가 들어있는 스택 pop
                else: break #새로운 연산자의 우선순위가 더 높으면 반복 중지
            s.push(token) #새로운 연산자 스택 삽입

        else: out.append(token) #피연산자는 출력배열에 추가

    while not s.isEmpty(): #스택에 남아있는 값을 전부 출력 배열로 pop
        out.append(s.pop())

    return out # 출력 배열 반환

ex = "(2+3)*4"
print(infix2Postfix(ex))
# print(postfix(infix2Postfix(ex)))