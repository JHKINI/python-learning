MAX_SIZE = 100

stack = [0] * MAX_SIZE

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



def eval_postfix(expr):

    for token in expr.split():

        if token.isdigit():

            push(int(token))

        else:

            b = pop()

            a = pop()



            if token == '+':

                push(a + b)

            elif token == '-':

                push(a - b)

            elif token == '*':

                push(a * b)

            elif token == '/':

                push(a / b)



    return pop()





expr = input("후위표기식 입력: ")

result = eval_postfix(expr)



print("계산 결과:", result)