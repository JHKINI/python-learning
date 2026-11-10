import random
프레임당쓰러진핀 =[[0, 0]for _ in range(9)]
프레임당쓰러진핀.append([0,0,0])
추가점수 =[[0, 0] for _ in range(10)]
더하는횟수 =[0]*10
프레임당점수=[0,0]
누적점수=[0]*10
프레임당점수계산완료여부=[False]*10
프레임_정보=[[0,0,0]]*10

프레임_인덱스 = 0
프레임_투구수 = 0
def 프레임_정보_작성(프레임_인덱스, 프레임_투구수, pins):
    global 더하는횟수 #외부변수 가져와서 사용하는 global
    if 프레임_투구수 == 0 and pins == 10: #첫번째투구에 쓰러트린 핀수가 10인경우
        더하는횟수[프레임_인덱스] = 2 #2를 더하는 횟수값에 저장하기

def 프레임_인덱스_관리(pins):
    global 프레임_인덱스
    global 프레임_투구수
    print(프레임_인덱스, 프레임_투구수,pins)
    프레임_정보[프레임_인덱스][프레임_투구수] = pins
    if pins == 10 and 프레임_투구수 == 0:
        프레임_인덱스 +=1

    elif 프레임_투구수 == 1 :
        프레임_인덱스 += 1
        프레임_투구수 = 0
    else:
        프레임_투구수 += 1

        
#기본적인 규칙
for 프레임 in range(9):
    pins1 = random.randint(0,10)
    프레임_인덱스_관리(pins1) #함수실행으로 함수에 값보내주기
    pins2 = 0 #자리만 확보 초기화
    if pins1 != 10: #첫번째에 스트라이크라면
        pins2 = random.randint(0,10-pins1)
        프레임_인덱스_관리(pins2)
       
    프레임당쓰러진핀[프레임][0]=pins1 #첫번째투구값저장
    프레임당쓰러진핀[프레임][1]=pins2 #두번째투구값저장
    print(프레임당쓰러진핀)
#10프레임에 관한코드 
pins1 = random.randint(0,10)
if pins1 == 10: #첫번째에 스트라이크인경우
    pins2 = random.randint(0,10)
    if pins2 == 10: #두번째에 스트라이크인경우
        pins3 = random.randint(0,10)
    else:
        pins3 = random.randint(0,10-pins2) #두번째에 스트라이크가 아닌경우
else:
    pins2 = random.randint(0,10-pins1) #첫번째가 스트라이크가아닌경우
    if pins1 + pins2 == 10:  #스페어인경우
        pins3 = random.randint(0,10)
    else: pins3 = 0 #그외의경우 3번째투구없음
프레임당쓰러진핀[9][0] = pins1
프레임당쓰러진핀[9][1] = pins2
프레임당쓰러진핀[9][2] = pins3

print(프레임당쓰러진핀)



# def A(a,b=10,c=6):
#     print("함수실행")
#     #return True, False
#     return [True, False, 0]

# print(A(a=10))
# b,c1, c2 = A(b=10,a=4)
# d = A(10)
# print(b,c1)
# print(d)

# def 화면출력(_숫자, 소수여부 = False):
#     if 소수여부:
#         print(f"{_숫자}는 소수입니다")
#     else:
#         print(f"{_숫자}는 소수가 아닙니다")
    

# def 소수판별함수(숫자):
#     if 숫자 < 2:
#         #print(f"{숫자}는 소수가 아닙니다")
#         화면출력(숫자)
#         return False
    
#     for i in range(2, 숫자):
#         if 숫자 % i == 0:
#             화면출력(숫자)
#             return False
        
#     화면출력(숫자, True)
#     return True
        
# 소수판별함수(3)
    