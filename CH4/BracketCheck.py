from CH4.Stack import Stack

def bracketCheck(str):
    stack = Stack()

    for ch in str:
        if ch in ('{', '(', '['):
            stack.push(ch)
        elif ch in ('}', ')', ']'):
            if stack.isEmpty(): #괄호의 개수가 맞지 않다면 리턴
                return False
            else:
                left = stack.pop()
                if (ch == '{' and left != '{') or \
                        (ch == '(' and left != ')') or \
                        (ch == '[' and left != ']'): #괄호의 종류가 맞지 않으면
                    return False

    return stack.isEmpty() #스택이 비어있는지 확인 (괄호의 개수 및 짝이 다 맞으면 Empty-True 아니면 False

print(bracketCheck("(()){}{}[{}]"))
print(bracketCheck("(()){}{}[{}])"))
print(bracketCheck("(()){}{}[{}}"))