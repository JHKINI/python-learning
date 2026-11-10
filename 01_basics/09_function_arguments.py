def A(a,b=10,c=6):
    print("함수실행")
    #return True, False
    return [True, False, 0]

print(A(a=10))
b,c1, c2 = A(b=10,a=4)
d = A(10)
print(b,c1)
print(d)

def 화면출력(_숫자, 소수여부 = False):
    if 소수여부:
        print(f"{_숫자}는 소수입니다")
    else:
        print(f"{_숫자}는 소수가 아닙니다")
    

def 소수판별함수(숫자):
    if 숫자 < 2:
        #print(f"{숫자}는 소수가 아닙니다")
        화면출력(숫자)
        return False
    
    for i in range(2, 숫자):
        if 숫자 % i == 0:
            화면출력(숫자)
            return False
        
    화면출력(숫자, True)
    return True
        
소수판별함수(3)
    