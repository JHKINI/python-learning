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