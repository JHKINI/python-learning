class Calculator:
    
    def __init__(self,number):
        self.number=number
        self.res_add = None
        self.res_minus = None
        self.res_multiply = None    
        self.res_divide = None
    
    def add(self):
        res = 0
        for i in self.number:
            res += i
        self.res_add = res
        return res
    def minus(self):
        res = self.number[0]
        for i in range(1, len(self.number)):
            res -= self.number[i]
        self.res_minus = res
        return res
    def multiply(self):
        res = 1
        for i in self.number:
            res *= i
        self.res_multiply = res
        return res
    def divide(self):
        res = self.number[0]
        for i in range(1, len(self.number)):
            if self.number[i] == 0:
                print("0으로 나눌 수 없습니다")
                return None
            res /= self.number[i]
        self.res_divide = res
        return res
 
result = list(map(int, input("숫자 입력(예:1 2 3):  ").split()))
    
calc = Calculator(result)

print(calc.add())      
print(calc.minus())    
print(calc.multiply())  
print(calc.divide())    