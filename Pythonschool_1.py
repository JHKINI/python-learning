#아웃풋

# Print "Hello World!"
print("Hello, World!")
# Print "Have a good day."
print("Have a good day.")
# Print "Learning Python is fun!"
print("Learning Python is fun!")
'''
Hello, World!
Have a good day.
Learning Python is fun!
'''


#주석처리 하기

# Write a single-line comment
#This is a comment
# Comment out this line so it does not run:
#print("This should not run")#

# Add a multiline comment
"""
This is a multiiline
comment
"""

#변수

x=5
y="John"
print(x)
print(y)

x = 4
x = "Sally"
print(x)
'''
5
John
Sally
'''

#변수_캐스팅

x = str(3)
y = int(3)
z = float(3)
print(x)
print(y)
print(z)

'''
3
3
3.0
'''
#변수_타입구하기
x=5
y="John"
print(type(x))
print(type(y))
'''
<class 'int'>
<class 'str'>
'''
#"" 와''차이
a = "John"
b = 'John'
print(a)
print(b)
'''
John
John
'''

#대소문자 구분
a=4
A="Sally"
print(a)
print(A)
'''
4
Sally
'''
#변수이름

import random
a=[1,2,3]
선택= random.choice(a)
print(선택)

import os
print(os.getcwd())