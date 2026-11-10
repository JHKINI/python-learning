class calculater:
    attr_number = []
    def __init__(self,number):
        self.number=number
        self.res_add = None
    
    def _add(self):
        res = 0
        for i in self.number:
            res += i
        self.res_add = res
        return res
    
    def _check_add_res(self):
        res = 0
        if self.res_add == None:
            res = self._add()
        else:
            res = self.res_add
            if res <101:
                return False
            else:
                return True
    
    def _add_in(self, _in):
        res = 0
        for i in _in:
            res += i

        return res

in_list  = []    
for i in range(10):
    in_list.append(int(input()))

a = calculater(in_list)
print(a.number)
#print(a._add())
#b = a._add_in([2,3,4])
if a._check_add_res() == False:
    print("입력이 충분하지 않아요.")





    # try:
    #     if 
        

    # except ValueError:
    #     print(0)    