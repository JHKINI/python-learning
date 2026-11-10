import flet as ft


class Contact:
    def __init__(self, name, phone, email, company):
        self.name = name
        self.phone = phone
        self.email = email
        self.company = company


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None


def main(page: ft.Page):
    page.title = "연락처 관리 프로그램"
    page.window_width = 400
    page.window_height = 600

    book = ContactBook()

    # 입력창들
    name_input = ft.TextField(label="이름")
    phone_input = ft.TextField(label="전화번호", hint_text="000-0000-0000")
    email_input = ft.TextField(label="이메일", hint_text="example@email.com")
    company_input = ft.TextField(label="회사")

    search_input = ft.TextField(label="검색할 이름")

    result_text = ft.Text("", size=16)

    # 등록 버튼 함수
    def add_contact_click(e):
        if (
            name_input.value == ""
            or phone_input.value == ""
            or email_input.value == ""
            or company_input.value == ""
        ):
            result_text.value = "모든 정보를 입력해주세요."
        else:
            contact = Contact(
                name_input.value,
                phone_input.value,
                email_input.value,
                company_input.value,
            )
            book.add_contact(contact)
            result_text.value = f"{name_input.value} 연락처가 등록되었습니다."

            # 입력창 비우기
            name_input.value = ""
            phone_input.value = ""
            email_input.value = ""
            company_input.value = ""

        page.update()

    # 검색 버튼 함수
    def search_contact_click(e):
        contact = book.search_contact(search_input.value)

        if contact:
            result_text.value = (
                f"이름: {contact.name}\n"
                f"전화번호: {contact.phone}\n"
                f"이메일: {contact.email}\n"
                f"회사: {contact.company}"
            )
        else:
            result_text.value = "등록되지 않은 연락처입니다."

        page.update()

    page.add(
        ft.Text("연락처 등록", size=20, weight="bold"),
        name_input,
        phone_input,
        email_input,
        company_input,
        ft.ElevatedButton("등록", on_click=add_contact_click),
        ft.Divider(),
        ft.Text("연락처 검색", size=20, weight="bold"),
        search_input,
        ft.ElevatedButton("검색", on_click=search_contact_click),
        ft.Divider(),
        result_text,
    )


ft.app(target=main)