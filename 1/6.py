# -*- coding: utf-8 -*-
# 예제: 이진트리 응용 - 모르스 코드 결정트리
# 문자를 모르스 코드로 인코딩하고, 모르스 코드를 다시 문자로 디코딩


class TNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


table = [
    ("A", ".-"), ("B", "-..."), ("C", "-.-."), ("D", "-.."),
    ("E", "."), ("F", "..-."), ("G", "--."), ("H", "...."),
    ("I", ".."), ("J", ".---"), ("K", "-.-"), ("L", ".-.."),
    ("M", "--"), ("N", "-."), ("O", "---"), ("P", ".--."),
    ("Q", "--.-"), ("R", ".-."), ("S", "..."), ("T", "-"),
    ("U", "..-"), ("V", "...-"), ("W", ".--"), ("X", "-..-"),
    ("Y", "-.--"), ("Z", "--.."),
]


def make_morse_tree():
    # 모르스 코드 표를 이용해 결정트리 만들기
    root = TNode(None, None, None)

    for tp in table:
        code = tp[1]
        node = root

        for c in code:
            if c == ".":
                if node.left is None:
                    node.left = TNode(None, None, None)
                node = node.left

            elif c == "-":
                if node.right is None:
                    node.right = TNode(None, None, None)
                node = node.right

        node.data = tp[0]

    return root


def decode(root, code):
    # 모르스 코드 하나를 문자 하나로 바꾸기
    node = root

    for c in code:
        if c == ".":
            node = node.left
        elif c == "-":
            node = node.right

    return node.data


def encode(ch):
    # 문자 하나를 모르스 코드로 바꾸기
    idx = ord(ch) - ord("A")
    return table[idx][1]


# 실행 예시
if __name__ == "__main__":
    morseCodeTree = make_morse_tree()

    text = "DATA"
    mlist = []

    for ch in text:
        code = encode(ch)
        mlist.append(code)

    print("입력문장:", text)
    print("Morse Code:", mlist)
    print("Decoding  : ", end="")

    for code in mlist:
        ch = decode(morseCodeTree, code)
        print(ch, end="")
    print()
