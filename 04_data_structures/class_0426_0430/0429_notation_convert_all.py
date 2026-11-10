def postfix_to_infix(expr):
    stack = []

    for ch in expr:
        if ch.isalnum():
            stack.append(ch)
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append("(" + a + ch + b + ")")

    return stack.pop()


def postfix_to_prefix(expr):
    stack = []

    for ch in expr:
        if ch.isalnum():
            stack.append(ch)
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(ch + a + b)

    return stack.pop()


def priority(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    else:
        return 0


def infix_to_postfix(expr):
    stack = []
    result = ""

    for ch in expr:
        if ch.isalnum():
            result += ch
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack[-1] != '(':
                result += stack.pop()
            stack.pop()
        elif ch in '+-*/':
            while stack and priority(stack[-1]) >= priority(ch):
                result += stack.pop()
            stack.append(ch)

    while stack:
        result += stack.pop()

    return result


def infix_to_prefix(expr):
    expr = expr[::-1]

    temp = ""
    for ch in expr:
        if ch == '(':
            temp += ')'
        elif ch == ')':
            temp += '('
        else:
            temp += ch

    postfix = infix_to_postfix(temp)
    return postfix[::-1]


# 실행 예시
print("후위 → 중위:", postfix_to_infix("ABC*+"))
print("후위 → 전위:", postfix_to_prefix("ABC*+"))
print("중위 → 후위:", infix_to_postfix("A+B*C"))
print("중위 → 전위:", infix_to_prefix("A+B*C"))