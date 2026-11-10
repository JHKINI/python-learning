import flet as ft


class StackADT:
    def __init__(self, max_size=100):
        self.max_size = max_size
        self.items = [None] * max_size
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.max_size - 1

    def push(self, item):
        if not self.isFull():
            self.top += 1
            self.items[self.top] = item

    def pop(self):
        if not self.isEmpty():
            item = self.items[self.top]
            self.top -= 1
            return item

    def peek(self):
        if not self.isEmpty():
            return self.items[self.top]

    def size(self):
        return self.top + 1

    def clear(self):
        self.top = -1


def priority(op):
    if op == '(':
        return 0
    elif op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    return -1


def apply_op(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b


def eval_infix(expr):
    values = StackADT(100)
    ops = StackADT(100)

    tokens = expr.split()

    for token in tokens:
        if token.isdigit():
            values.push(int(token))

        elif token == '(':
            ops.push(token)

        elif token == ')':
            while not ops.isEmpty() and ops.peek() != '(':
                op = ops.pop()
                b = values.pop()
                a = values.pop()
                values.push(apply_op(a, b, op))

            ops.pop()

        elif token in '+-*/':
            while not ops.isEmpty() and priority(ops.peek()) >= priority(token):
                op = ops.pop()
                b = values.pop()
                a = values.pop()
                values.push(apply_op(a, b, op))

            ops.push(token)
        else:
            raise ValueError("잘못된 수식")

    while not ops.isEmpty():
        op = ops.pop()
        b = values.pop()
        a = values.pop()
        values.push(apply_op(a, b, op))

    return values.pop()


def main(page: ft.Page):
    page.title = "StackADT 계산기"
    page.window_width = 400
    page.window_height = 300

    txt_expr = ft.TextField(
        label="수식 입력",
        hint_text="예: ( 3 + 4 ) * 2"
    )

    result = ft.Text(size=20)

    def calculate(e):
        try:
            answer = eval_infix(txt_expr.value)
            result.value = f"계산 결과: {answer}"
        except:
            result.value = "수식 오류입니다. 예: ( 3 + 4 ) * 2 처럼 공백을 넣어주세요."

        page.update()

    page.add(
        ft.Text("괄호 계산 가능한 StackADT 계산기", size=22),
        txt_expr,
        ft.ElevatedButton("계산", on_click=calculate),
        result
    )


ft.app(target=main)