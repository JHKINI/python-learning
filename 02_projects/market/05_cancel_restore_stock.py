import random
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
prices = {}
for item in 물품명:
    prices[item] = random.randrange(3000, 15001, 500)

# 재고 설정
rmi = {}
for item in 물품명:
    rmi[item] = random.randrange(1, 50)

# 날짜 입력 → 매출 초기화
sales = {}
date = input("오늘 날짜를 입력하세요 (예: 2026-04-02): ")

if date not in sales:
    sales[date] = {"total": 0, "items": {}}


# 기능 함수들
def 계산():
    total = 0
    cart = {}  # {물품: 수량}
    print(물품명)
    while True:
       
        item = input("물품명 입력 (완료시 e): ")
        
        if item == "e":
            break
        
        if item in prices:
            try:
                qty = int(input("수량 입력: "))
                
                if qty <= 0:
                    print("수량은 1개 이상이어야 합니다")
                    continue
                
                if rmi[item] < qty:
                    print(f"재고 부족! 현재 재고: {rmi[item]}개")
                    continue
                
                # 장바구니 추가
                if item in cart:
                    cart[item] += qty
                else:
                    cart[item] = qty
                
                total += prices[item] * qty
                rmi[item] -= qty
                
                print(f"{item} {qty}개 담김 (개당 {prices[item]}원)")
            
            except ValueError:
                print("숫자를 입력하세요")
        
        else:
            print("없는 물품입니다")
    
    # 장바구니 출력
    print("\n🛒 장바구니 목록")
    for item, qty in cart.items():
        print(f"- {item} {qty}개 ({prices[item]}원 x {qty})")
    
    print(f"총 금액: {total}원")
    
    # 결제 여부
    confirm = input("결제하시겠습니까? (yes/no): ")
    
    if confirm.lower() == "yes":
        sales[date]["total"] += total
        for item, qty in cart.items():
            if item in sales[date]["items"]:
                sales[date]["items"][item] += qty
            else:
                sales[date]["items"][item] = qty
        print("✅ 결제 완료!")
    else:
        # 결제 취소 시 재고 복구
        for item, qty in cart.items():
            rmi[item] += qty
        print("❌ 결제를 취소하였습니다.")
    

def 재고관리():
    for item, count in rmi.items():
        print(f"{item}: {count}개")

def 매출관리():
    # 날짜 매출 확인
    if date not in sales or sales[date]["total"] == 0:
        print(f"{date} 매출 내역이 없습니다.")
        return
    
    print(f"\n📦 {date} 판매 목록")
    
    for item, qty in sales[date]["items"].items():
        price = prices[item]
        subtotal = price * qty
        print(f"- {item}: {qty}개 (단가 {price} x {qty}개 = {subtotal}원)")
    
    print(f"\n💰 총 매출: {sales[date]['total']}원")

# 메뉴
while True:
    print("\n모드를 선택하시오")
    print("1. 계산")
    print("2. 재고관리")
    print("3. 매출관리")
    print("4. 종료")

    choice = input("번호 입력: ")

    if choice == "1":
        계산()
    
    elif choice == "2":
        재고관리()
    
    elif choice == "3":
        매출관리()
    
    elif choice == "4":
        print("프로그램 종료")
        break
    
    else:
        print("잘못된 입력입니다")