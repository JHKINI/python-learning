import flet as ft


class Calculator:
    def __init__(self, number):
        self.number = number
        self.res_add = None
        self.res_minus = None
        self.res_multiply = None
        self.res_divide = None

    def add(self):
        res = 0
        for i in self.number:
            res += i
        self.res_add = res
        return res

    def minus(self):
        res = self.number[0]
        for i in range(1, len(self.number)):
            res -= self.number[i]
        self.res_minus = res
        return res

    def multiply(self):
        res = 1
        for i in self.number:
            res *= i
        self.res_multiply = res
        return res

    def divide(self):
        res = self.number[0]
        for i in range(1, len(self.number)):
            if self.number[i] == 0:
                return "0으로 나눌 수 없습니다"
            res /= self.number[i]
        self.res_divide = res
        return res


def main(page: ft.Page):
    page.title = "계산기"
    page.window_width = 400
    page.window_height = 500
    page.padding = 20

    title = ft.Text("Flet 계산기", size=24, weight="bold")

    number_input = ft.TextField(
        label="숫자 입력",
        hint_text="예: 10 2 3",
        width=300
    )

    result_text = ft.Text("결과가 여기에 표시됩니다.", size=16)

    def get_numbers():
        try:
            nums = list(map(int, number_input.value.split()))
            if len(nums) == 0:
                result_text.value = "숫자를 입력하세요."
                page.update()
                return None
            return nums
        except:
            result_text.value = "숫자를 공백으로 구분해서 정수로 입력하세요."
            page.update()
            return None

    def do_add(e):
        nums = get_numbers()
        if nums is None:
            return
        calc = Calculator(nums)
        result_text.value = f"덧셈 결과: {calc.add()}"
        page.update()

    def do_minus(e):
        nums = get_numbers()
        if nums is None:
            return
        calc = Calculator(nums)
        result_text.value = f"뺄셈 결과: {calc.minus()}"
        page.update()

    def do_multiply(e):
        nums = get_numbers()
        if nums is None:
            return
        calc = Calculator(nums)
        result_text.value = f"곱셈 결과: {calc.multiply()}"
        page.update()

    def do_divide(e):
        nums = get_numbers()
        if nums is None:
            return
        calc = Calculator(nums)
        result_text.value = f"나눗셈 결과: {calc.divide()}"
        page.update()

    page.add(
        ft.Column(
            [
                title,
                number_input,
                ft.Row(
                    [
                        ft.ElevatedButton("덧셈", on_click=do_add),
                        ft.ElevatedButton("뺄셈", on_click=do_minus),
                    ]
                ),
                ft.Row(
                    [
                        ft.ElevatedButton("곱셈", on_click=do_multiply),
                        ft.ElevatedButton("나눗셈", on_click=do_divide),
                    ]
                ),
                result_text
            ],
            spacing=20
        )
    )


ft.app(target=main)