#구조 
'''
비밀번호= None
승인여부= False
숫자모음=[] 
문자모음=[] 
특수문자모음=[]
for k in 비밀번호
    if k 숫자 숫자모음=k
    elif k 문자 문자모음=k
    elif k 특수문자 특수문자=k
    else 재입력요청
if 모음 각각 len() >0
   if 시그마 모음>=8
    if 문자모음 이 대문자에 포함되면
        승인여부 =True
true 면 승인됨
flase 면 재입력요청 
'''

'''
비밀번호= "123ab!!"
승인여부= False
승인여부_진행 = True #검증
대문자존재여부= False
숫자모음=[] 
문자모음=[] 
특수문자모음=[]
승인되는소문자모음 = "abcdefghijklnmopqrstuvwxyz"
승인되는대문자모음 = "ABCDEFGHIJKLNMOPQRSTUVWXYZ"
승인되는특수문자모음=['!','@','#']
for k in 비밀번호:
    #if 숫자: pass 
    if k in "1234567890":
       숫자모음.append(k)
    #elif 문자: pass 
    elif k in 승인되는소문자모음 or k in 승인되는대문자모음:
        문자모음.append(k)
        if k in 승인되는대문자모음: 대문자존재여부 = true
    #elif 특수문자:pass
    elif k in 승인되는특수문자모음: 특수문자모음.append(k) 
    else: 
       승인여부_진행= False
       print("재입력해주세요")
if 승인여부_진행:      
    if len(숫자모음)>0 and len(문자모음)>0 and len(특수문자모음)>0:
        if sum(len(숫자모음)+len(문자모음)+len(특수문자모음))>7:
            if 대문자존재여부:
               승인여부 =True
print(승인여부)
#flase면 재입력요청 
'''
비밀번호="1a54"
승인여부 =False
승인여부_진행 =True
숫자갯수 = 소문자갯수 = 대문자갯수 = 특수문자갯수 = 0
승인되는숫자모음="1234567890"
승인되는소문자모음 = "abcdefghijklnmopqrstuvwxyz"
승인되는대문자모음 = "ABCDEFGHIJKLNMOPQRSTUVWXYZ"
승인되는특수문자모음=['!','@','#']
for k in 비밀번호:
    if k in 승인되는숫자모음: 숫자갯수 += 1
    elif k in 승인되는소문자모음: 소문자갯수 += 1
    elif k in 승인되는대문자모음: 대문자갯수 += 1
    elif k in 승인되는특수문자모음: 특수문자갯수 += 1
    else:
        승인여부_진행 = False
        print("재입력해주세요")
if 승인여부_진행:
    if 숫자갯수 > 0 and 특수문자갯수 > 0 and (대문자갯수 > 0 or 소문자갯수 > 0):
        if sum(숫자갯수, 특수문자갯수, 대문자갯수, 소문자갯수) >7:
            if 대문자갯수 > 0:
                승인여부 = True
print(승인여부)
            

