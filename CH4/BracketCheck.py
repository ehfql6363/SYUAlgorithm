def bracketCheck(string):
    from StackClass import Stack
    stack = Stack()

    for char in string:
        if char in ('{', '[', '('):
            stack.push(char)
        elif char in ('}', ']', ')'):
            if stack.isEmpty():
                print("조건 2 위반: 여는 괄호 없음")
                return False
            else:
                left = stack.pop()
                if (left != '(' and char == ')') or \
                        (left != '{' and char == '}') or \
                        (left != '[' and char == ']'):
                    print("조건 3 위반 : 괄호의 종류가 맞지 않음")
                    return False

    if stack.isEmpty():
        return True
    else:
        print("조건 1 위반 : 괄호의 개수가 맞지 않음")
        return False

print(bracketCheck("(()){}{}[{}]"))
bracketCheck("(()){}{}[{}])")
bracketCheck("(()){}{}[{}}")