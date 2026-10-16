import flet as ft


class Calculator:
    def __init__(self, number):
        self.number = number

    def add(self):
        res = 0
        for i in self.number:
            res += i
        return res

    def minus(self):
        res = self.number[0]
        for i in range(1, len(self.number)):
            res -= self.number[i]
        return res

    def multiply(self):
        res = 1
        for i in self.number:
            res *= i
        return res

    def divide(self):
        res = self.number[0]
        for i in range(1, len(self.number)):
            if self.number[i] == 0:
                return "0으로 나눌 수 없습니다"
            res /= self.number[i]
        return res

    def average(self):
        return sum(self.number) / len(self.number)

    def maximum(self):
        return max(self.number)


def main(page: ft.Page):
    page.title = "계산기"

    number_input = ft.TextField(
        label="숫자 입력",
        hint_text="예: 10 20 30"
    )

    result_text = ft.Text("결과 출력")

    def get_numbers():
        try:
            nums = list(map(int, number_input.value.split()))
            if len(nums) == 0:
                result_text.value = "숫자를 입력하세요"
                page.update()
                return None
            return nums
        except:
            result_text.value = "숫자를 공백으로 입력하세요"
            page.update()
            return None

    def do_add(e):
        nums = get_numbers()
        if nums:
            calc = Calculator(nums)
            result_text.value = f"덧셈: {calc.add()}"
            page.update()

    def do_minus(e):
        nums = get_numbers()
        if nums:
            calc = Calculator(nums)
            result_text.value = f"뺄셈: {calc.minus()}"
            page.update()

    def do_multiply(e):
        nums = get_numbers()
        if nums:
            calc = Calculator(nums)
            result_text.value = f"곱셈: {calc.multiply()}"
            page.update()

    def do_divide(e):
        nums = get_numbers()
        if nums:
            calc = Calculator(nums)
            result_text.value = f"나눗셈: {calc.divide()}"
            page.update()

    def do_average(e):
        nums = get_numbers()
        if nums:
            calc = Calculator(nums)
            result_text.value = f"평균: {calc.average()}"
            page.update()

    def do_max(e):
        nums = get_numbers()
        if nums:
            calc = Calculator(nums)
            result_text.value = f"최댓값: {calc.maximum()}"
            page.update()

    page.add(
        ft.Column(
            [
                number_input,
                ft.Row([
                    ft.ElevatedButton("덧셈", on_click=do_add),
                    ft.ElevatedButton("뺄셈", on_click=do_minus),
                ]),
                ft.Row([
                    ft.ElevatedButton("곱셈", on_click=do_multiply),
                    ft.ElevatedButton("나눗셈", on_click=do_divide),
                ]),
                ft.Row([
                    ft.ElevatedButton("평균", on_click=do_average),
                    ft.ElevatedButton("최댓값", on_click=do_max),
                ]),
                result_text
            ]
        )
    )


ft.app(target=main)