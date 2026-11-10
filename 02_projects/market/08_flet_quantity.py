import random
from datetime import datetime
import flet as ft

# 물품 목록
물품명 = [
    "비누","치약","샴푸","린스","바디워시","폼클렌징","칫솔","수건",
    "휴지","물티슈","세탁세제","섬유유연제","주방세제","수세미","고무장갑",
    "쌀","라면","햇반","생수","우유","계란","두부","콩나물","시금치",
    "양파","감자","고구마","사과","바나나","오렌지","귤","토마토",
    "김치","된장","고추장","간장","식용유","참기름","소금","설탕",
    "커피","차","과자","빵","젤리","초콜릿","음료수","맥주","소주",
    "고기(돼지고기)","고기(소고기)","닭고기","생선","오징어","새우","게",
    "쌀국수","파스타","잼","버터","치즈","요거트","아이스크림","통조림",
    "냉동만두","어묵","햄","소시지","김","미역","다시마","멸치",
    "밀가루","부침가루","튀김가루","빵가루","식초","소스","향신료",
    "양초","성냥","건전지","전구","쓰레기봉투","지퍼백","호일","랩"
]

prices = {item: random.randrange(1000, 5000, 500) for item in 물품명}
stock = {item: random.randrange(10, 50) for item in 물품명}

sales_log = []
date = datetime.now().strftime("%Y-%m-%d")


# ---------------- 앱 ----------------

def main(page: ft.Page):
    page.title = "POS + 재고관리 시스템"
    page.window_width = 700
    page.window_height = 500

    cart = {}
    output = ft.Column()

    qty = {"value": 1}
    qty_text = ft.Text(str(qty["value"]), width=40, text_align="center")

    # ---------------- 수량 ----------------

    def plus_qty(e):
        qty["value"] += 1
        qty_text.value = str(qty["value"])
        page.update()

    def minus_qty(e):
        if qty["value"] > 1:
            qty["value"] -= 1
            qty_text.value = str(qty["value"])
            page.update()

    qty_row = ft.Row([
        ft.ElevatedButton("-", width=40, on_click=minus_qty),
        qty_text,
        ft.ElevatedButton("+", width=40, on_click=plus_qty),
    ])

    # ---------------- 장바구니 ----------------

    def update_cart():
        output.controls.clear()

        total = sum(prices[i] * q for i, q in cart.items())

        output.controls.append(ft.Text("🛒 장바구니", weight="bold"))

        for item, q in cart.items():
            output.controls.append(
                ft.Text(f"{item} | {q}개 | {prices[item] * q}원")
            )

        output.controls.append(ft.Text(f"총 금액: {total}원", weight="bold"))
        page.update()

    # ---------------- 추가 ----------------

    def add_to_cart(e):
        item = dropdown.value
        if not item:
            return

        q = qty["value"]

        if stock[item] < q:
            output.controls.append(ft.Text("❌ 재고 부족", color="red"))
            page.update()
            return

        cart[item] = cart.get(item, 0) + q
        stock[item] -= q   # 🔥 재고 감소

        update_cart()

    # ---------------- 결제 ----------------

    def checkout(e):
        if not cart:
            return

        total = 0

        for item, q in cart.items():
            price = prices[item]
            total += price * q

            sales_log.append({
                "date": date,
                "item": item,
                "qty": q,
                "price": price,
                "total": price * q
            })

        cart.clear()
        update_cart()

        output.controls.append(ft.Text(f"✅ 결제 완료: {total}원", color="green"))
        page.update()

    # ---------------- 취소 (재고 복구) ----------------

    def cancel_cart(e):
        for item, q in cart.items():
            stock[item] += q   # 🔥 재고 복구

        cart.clear()
        update_cart()

        output.controls.append(ft.Text("❌ 결제 취소 (재고 복구됨)", color="red"))
        page.update()

    # ---------------- 재고 보기 ----------------

    def show_inventory(e):
        output.controls.clear()
        output.controls.append(ft.Text("📦 재고 현황", weight="bold"))

        for item, cnt in stock.items():
            output.controls.append(
                ft.Text(f"{item}: {cnt}개")
            )

        page.update()

    # ---------------- 매출 ----------------

    def show_sales(e):
        output.controls.clear()

        total = 0

        for row in sales_log:
            output.controls.append(
                ft.Text(f"{row['date']} | {row['item']} | {row['qty']}개 | {row['total']}원")
            )
            total += row["total"]

        output.controls.append(ft.Text(f"💰 총 매출: {total}원", weight="bold"))
        page.update()

    # ---------------- UI ----------------

    dropdown = ft.Dropdown(
        label="물품 선택",
        options=[ft.dropdown.Option(i) for i in 물품명],
        width=150
    )

    page.add(
        ft.Row([dropdown, qty_row, ft.ElevatedButton("추가", on_click=add_to_cart)]),
        ft.Row([
            ft.ElevatedButton("결제", on_click=checkout),
            ft.ElevatedButton("취소", on_click=cancel_cart),
            ft.ElevatedButton("재고보기", on_click=show_inventory),
            ft.ElevatedButton("매출보기", on_click=show_sales),
        ]),
        ft.Divider(),
        output
    )


ft.app(target=main)