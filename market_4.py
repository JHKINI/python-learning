import random
from datetime import datetime
import flet as ft

# 물품 목록
물품명 = [
    "비누", "치약", "샴푸", "린스", "바디워시", "폼클렌징", "칫솔", "수건",
    "휴지", "물티슈", "세탁세제", "섬유유연제", "주방세제", "수세미", "고무장갑",
    "쌀", "라면", "햇반", "생수", "우유", "계란", "두부", "콩나물", "시금치",
    "양파", "감자", "고구마", "사과", "바나나", "오렌지", "귤", "토마토",
    "김치", "된장", "고추장", "간장", "식용유", "참기름", "소금", "설탕",
    "커피", "차", "과자", "빵", "젤리", "초콜릿", "음료수", "맥주", "소주",
    "고기(돼지고기)", "고기(소고기)", "닭고기", "생선", "오징어", "새우", "게",
    "쌀국수", "파스타", "잼", "버터", "치즈", "요거트", "아이스크림", "통조림",
    "냉동만두", "어묵", "햄", "소시지", "김", "미역", "다시마", "멸치",
    "밀가루", "부침가루", "튀김가루", "빵가루", "식초", "소스", "향신료",
    "양초", "성냥", "건전지", "전구", "쓰레기봉투", "지퍼백", "호일", "랩"
]

# 가격 설정
prices = {item: random.randrange(3000, 15001, 500) for item in 물품명}

# 재고 설정
rmi = {item: random.randrange(5, 50) for item in 물품명}

# 오늘 날짜 매출 초기화
date = datetime.now()#input("오늘 날짜를 입력하세요 (예: 2026-04-02): ")
print(date)
sales = {date: {"total": 0, "items": {}}}

# ------------------- FLET GUI -------------------

def main(page: ft.Page):
    page.title = f"{date} POS 시스템"
    page.window_width = 700
    page.window_height = 500

    cart = {}  # 장바구니 {item: qty}

    # 출력 영역
    output = ft.Column()

    # 장바구니 갱신 함수
    def update_cart():
        output.controls.clear()
        total = sum(prices[item]*qty for item, qty in cart.items())
        output.controls.append(ft.Text("🛒 장바구니", weight="bold"))
        for item, qty in cart.items():
            output.controls.append(ft.Text(f"{item}: {qty}개 (단가 {prices[item]}원)"))
        #output.controls.append(ft.Text(f"총 금액: {total}원"))#
        page.update()

    # 아이템 선택 콤보박스
    item_dropdown = ft.Dropdown(
        label="물품 선택",
        options=[ft.dropdown.Option(item) for item in 물품명],
        width=150
    )
    qty_input = ft.TextField(label="수량", width=100, value="1")

    def add_to_cart(e):
        item = item_dropdown.value
        if not item:
            return
        try:
            qty = int(qty_input.value)
            if qty <= 0:
                return
            if rmi[item] < qty:
                output.controls.append(ft.Text(f"재고 부족! 현재 {rmi[item]}개"))
                page.update()
                return
            if item in cart:
                cart[item] += qty
            else:
                cart[item] = qty
            rmi[item] -= qty
            update_cart()
        except ValueError:
            return

    add_button = ft.ElevatedButton("장바구니에 추가", on_click=add_to_cart)

    # 결제
    def checkout(e):
        total = sum(prices[item]*qty for item, qty in cart.items())
        if not cart:
            return
        for item, qty in cart.items():
            if item in sales[date]["items"]:
                sales[date]["items"][item] += qty
            else:
                sales[date]["items"][item] = qty
        sales[date]["total"] += total
        cart.clear()
        update_cart()
        output.controls.append(ft.Text(f"✅ 결제 완료! 총 {total}원"))
        page.update()

    checkout_button = ft.ElevatedButton("결제", on_click=checkout)

    # 재고관리
    def show_inventory(e):
        output.controls.clear()
        output.controls.append(ft.Text("📦 재고 목록", weight="bold"))
        for item, count in rmi.items():
            output.controls.append(ft.Text(f"{item}: {count}개"))
        page.update()

    inventory_button = ft.ElevatedButton("재고관리", on_click=show_inventory)

    # 매출관리
    def show_sales(e):
        output.controls.clear()
        output.controls.append(ft.Text(f"📊 {date} 매출 기록", weight="bold"))
        for item, qty in sales[date]["items"].items():
            subtotal = prices[item] * qty
            output.controls.append(ft.Text(f"{item} 단가: {prices[item]}원 , 판매수량: {qty}개, 판매액: {subtotal}원"))
        output.controls.append(ft.Text(f"💰 총 매출: {sales[date]['total']}원", weight="bold"))
        page.update()

    sales_button = ft.ElevatedButton("매출관리", on_click=show_sales)

    page.add(
        ft.Row([item_dropdown, qty_input, add_button]),
        ft.Row([checkout_button, inventory_button, sales_button]),
        ft.Divider(),
        output
    )

ft.app(target=main)