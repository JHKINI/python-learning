숫자=None
반환=None
if 숫자 ==2:
    반환 = True
elif 숫자 >2:
    for k in range(2, 숫자-1,1):
        나머지 = 숫자 % k
        if 나머지 == 0:
            반환 = False
            break
    if 반환 == None: 반환 == True
else:
    반환 = False  # 사용자 0 음수 1 넣을때 예외처리