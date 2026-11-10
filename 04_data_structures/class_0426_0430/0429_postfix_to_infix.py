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