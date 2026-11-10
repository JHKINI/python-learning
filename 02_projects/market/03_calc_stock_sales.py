import random

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
    sales[date] = 0

print(f"{date} 매출 시작: {sales[date]}원")

# 기능 함수들
def 계산():
    total = 0
    
    while True:
        item = input("물품명 입력 (끝내려면 q): ")
        
        if item == "q":
            break
        
        if item in prices:
            total += prices[item]
            rmi[item] -= 1
            print(f"{item} 가격: {prices[item]}원")
        else:
            print("없는 물품입니다")
    
    sales[date] += total
    print(f"총 금액: {total}원")

def 재고관리():
    for item, count in rmi.items():
        print(f"{item}: {count}개")

def 매출관리():
    print(f"{date} 총 매출: {sales[date]}원")

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