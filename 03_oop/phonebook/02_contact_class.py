class Contact:
    def __init__(self,name,phone,email,company):
        self.name=name
        self.phone=phone
        self.email=email
        self.company=company
class ContactBook:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self,contact):
        self.contacts.append(contact)
    
    def search_contact(self,name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None
def input_contact():
    name = input("등록할 이름을 입력하세요: ")
    phone = input("전화번호를 입력하세요:000-0000-0000 ")
    email = input("이메일을 입력하세요: @를 포함한 이메일 주소 ")
    company = input("회사를 입력하세요: ")
    return Contact(name, phone, email, company)

c= ContactBook()
while True:
    contact = input_contact()
    c.add_contact(contact)
    search_name = input("검색할 이름을 입력하세요: ")
    contact = c.search_contact(search_name)
    if contact:
        print("이름: {}, 전화번호: {}, 이메일: {}, 회사: {}".format(contact.name, contact.phone, contact.email, contact.company))
    else:
        print("등록되지 않은 연락처입니다.")