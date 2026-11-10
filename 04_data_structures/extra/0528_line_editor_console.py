# -*- coding: utf-8 -*-

# 라인 편집기
def line_editor():
    doc = []

    while True:
        cmd = input("명령(i,d,r,p,l,s,q): ")

        # 라인 삽입
        if cmd == 'i':
            pos = int(input("행번호: "))
            text = input("내용: ")

            doc.insert(pos, text)

        # 라인 삭제
        elif cmd == 'd':
            pos = int(input("행번호: "))
            doc.pop(pos)

        # 라인 변경
        elif cmd == 'r':
            pos = int(input("행번호: "))
            text = input("내용: ")

            doc[pos] = text

        # 현재 내용과 라인 번호 출력
        elif cmd == 'p':
            print("\n[현재 문서]")

            for i in range(len(doc)):
                print(f"[{i}] {doc[i]}")

            print()

        # test.txt 파일로부터 읽어들임
        elif cmd == 'l':
            infile = open("test.txt", "r", encoding="utf-8")

            doc.clear()

            for line in infile:
                doc.append(line.strip())

            infile.close()
            print("파일 로드 완료")

        # test.txt 파일로 편집 내용을 저장
        elif cmd == 's':
            outfile = open("test.txt", "w", encoding="utf-8")

            for i in range(len(doc)):
                outfile.write(doc[i] + "\n")

            outfile.close()
            print("파일 저장 완료")

        # 종료
        elif cmd == 'q':
            break

        else:
            print("잘못된 명령입니다.")


line_editor()