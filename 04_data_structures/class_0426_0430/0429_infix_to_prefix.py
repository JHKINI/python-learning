def priority(op):
    if op in '+-': return 1
    if op in '*/': return 2
    return 0

def infix_to_prefix(expr):
    # 1. 뒤집기
    expr = expr[::-1]

    # 2. 괄호 바꾸기
    temp = ""
    for ch in expr:
        if ch == '(':
            temp += ')'
        elif ch == ')':
            temp += '('
        else:
            temp += ch
    expr = temp

    # 3. 후위 변환
    stack = []
    result = ""

    for ch in expr:
        if ch.isalnum():
            result += ch
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
        else:
            while stack and priority(stack[-1]) >= priority(ch):
                result += stack.pop()
            stack.append(ch)

    while stack:
        result += stack.pop()

    # 4. 다시 뒤집기
    return result[::-1]