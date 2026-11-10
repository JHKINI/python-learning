MAX_SIZE = 100

stack = [None] * MAX_SIZE
top = -1

def push(item):
    global top
    top += 1
    stack[top] = item

def pop():
    global top
    item = stack[top]
    top -= 1
    return item

def peek():
    return stack[top]

def is_empty():
    return top == -1

def priority(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    else:
        return 0

def is_open(ch):
    return ch == '(' or ch == '[' or ch == '{'

def is_close(ch):
    return ch == ')' or ch == ']' or ch == '}'

def matching(open_ch, close_ch):
    return (open_ch == '(' and close_ch == ')') or \
           (open_ch == '[' and close_ch == ']') or \
           (open_ch == '{' and close_ch == '}')

def infix_to_postfix(expr):
    global top
    top = -1
    result = []

    for ch in expr:
        if ch == ' ':
            continue

        # 피연산자
        if ch.isalnum():
            result.append(ch)

        # 여는 괄호
        elif is_open(ch):
            push(ch)

        # 닫는 괄호
        elif is_close(ch):
            while not is_empty() and not is_open(peek()):
                result.append(pop())

            if is_empty():
                return "괄호 오류"

            open_ch = pop()

            if not matching(open_ch, ch):
                return "괄호 오류"

        # 연산자
        elif ch in '+-*/':
            while not is_empty() and not is_open(peek()) and \
                  priority(peek()) >= priority(ch):
                result.append(pop())

            push(ch)

    while not is_empty():
        if is_open(peek()):
            return "괄호 오류"
        result.append(pop())

    return ''.join(result)


expr = input("중위표기식 입력: ")
print("후위표기식:", infix_to_postfix(expr))