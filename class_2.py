
class numberbook:
    def __init__ (self, name,phon_number):
        self.name = name
        
    def e_adress(self,adress):
        return "{}의 주소는{}".format (self.name,adress)
    def job_name(self,job):
        return "{}의 주소는{}".format (self.name,job)
    user = numberbook("user",01012345678)
    print(user.e_address())
    print (user.job_name())

class road (numberbook):
    def __int__(self):
