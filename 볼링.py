import random 
프레임당쓰러진핀 =[[0, 0]for _ in range(9)]
프레임당쓰러진핀.append([0,0,0])
추가점수 =[[0, 0] for _ in range(10)]
더하는횟수 = [0,0,0,0,0,0,0,0,0,0] 
프레임당점수 = [0,0]
누적점수 = [0,0,0,0,0,0,0,0,0,0]
프레임당점수계산완료여부=[False]*10
프레임_정보 = [[0,0,0]]*10

프레임_인덱스 = 0
프레임_투구수 = 0
def 프레임_정보_작성(프레임_인덱스, 프레임_투구수, pins):
    global 더하는횟수
    if 프레임_투구수 == 0 and pins == 10:
        더하는횟수[프레임_인덱스] = 2

def 프레임_인덱스_관리(pins): #def 계산(pins):
    global 프레임_인덱스
    global 프레임_투구수
    print(프레임_인덱스, 프레임_투구수, pins)
    프레임_정보[프레임_인덱스][프레임_투구수] = pins
    if pins == 10 and 프레임_투구수 == 0:        
        프레임_인덱스 += 1

    elif 프레임_투구수 == 1 :        
        프레임_인덱스 += 1
        프레임_투구수 = 0

    else:
        프레임_투구수 += 1
    

for 프레임 in range(9): #프레임을 적용
    pins1 = random.randint(0,10)
    프레임_인덱스_관리(pins1)
    pins2 = 0    
    if pins1 != 10:
        pins2 = random.randint(0,10-pins1)
        프레임_인덱스_관리(pins2)
    
    프레임당쓰러진핀[프레임][0] = pins1
    프레임당쓰러진핀[프레임][1] = pins2
    print(프레임당쓰러진핀)
    #print(f"{프레임+1}프레임에서 쓰러뜨린 총 핀의 수: {pins1+pins2}")

    # print("양진희", 123, "폴리텍")
    # print("{} {} {}".format("양진회", 123, "폴리텍"))
    # print("{0} {1} {2}".format("양진회", 123, "폴리텍"))
    # print("{a} {b} {c}".format(a:"양진회", b:123, c:"폴리텍"))
    # print(f"{"양진회"} {pins1} {pins2}")
    # "양진희의 학번은 123 입니다." 
    # print("양진희의 학번은", a, "입니다")
    
    
    # for i in range(10):
    #     if 더하는횟수[i]>0:
    #         if 추가점수[i][0]==0:
    #             추가점수[i][0]=pins
    #         else:
    #             추가점수[i][1]=pins
    #             더하는횟수[i]-=1
    #     if 더하는횟수[i] == 0:
    #         프레임당점수[i]= (프레임당쓰러진핀[i][0]+프레임당쓰러진핀[i][1]+추가점수[i][0]+ 추가점수[i][1])

#10프레임에 관한 코드          
pins1 = random.randint(0,10)
if pins1 == 10:
    pins2 = random.randint(0,10)
    if pins2 == 10:
        pins3 = random.randint(0,10)
    else:
        pins3 = random.randint(0,10-pins2)
else:
    pins2 = random.randint(0,10-pins1)
    if pins1 + pins2 == 10:
        pins3 = random.randint(0,10)
    else: pins3 = 0

프레임당쓰러진핀[9][0] = pins1
프레임당쓰러진핀[9][1] = pins2
프레임당쓰러진핀[9][2] = pins3
     
print(프레임당쓰러진핀)
