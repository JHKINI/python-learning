# -*- coding: utf-8 -*-
import flet as ft
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "test.txt")

def main(page: ft.Page):
    page.title = "라인 편집기"
    page.window_width = 500
    page.window_height = 600

    doc = []

    pos_input = ft.TextField(label="행 번호", width=120)
    text_input = ft.TextField(label="내용", expand=True)
    output = ft.Column()

    def refresh():
        output.controls.clear()
        output.controls.append(ft.Text("[현재 문서]"))

        for i in range(len(doc)):
            output.controls.append(ft.Text(f"[{i}] {doc[i]}"))

        page.update()

    def insert_line(e):
        pos = int(pos_input.value)
        text = text_input.value
        doc.insert(pos, text)
        refresh()

    def delete_line(e):
        pos = int(pos_input.value)
        doc.pop(pos)
        refresh()

    def replace_line(e):
        pos = int(pos_input.value)
        text = text_input.value
        doc[pos] = text
        refresh()

    def load_file(e):
        doc.clear()

        infile = open(FILE_PATH, "r", encoding="utf-8")  # 읽기
        for line in infile:
            doc.append(line.strip())
        infile.close()

        refresh()

    def save_file(e):
        outfile = open(FILE_PATH, "w", encoding="utf-8")  # 읽기
        for line in doc:
            outfile.write(line + "\n")
        outfile.close()

        output.controls.append(ft.Text("파일 저장 완료"))
        page.update()

    page.add(
        ft.Text("라인 편집기", size=24, weight="bold"),
        ft.Row([pos_input, text_input]),
        ft.Row([
            ft.ElevatedButton("삽입", on_click=insert_line),
            ft.ElevatedButton("삭제", on_click=delete_line),
            ft.ElevatedButton("변경", on_click=replace_line),
        ]),
        ft.Row([
            ft.ElevatedButton("파일 읽기", on_click=load_file),
            ft.ElevatedButton("파일 저장", on_click=save_file),
            ft.ElevatedButton("출력", on_click=lambda e: refresh()),
        ]),
        output
    )


ft.app(target=main)