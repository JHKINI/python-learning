MAX_SIZE = 100



def check_bracket(expr):

    A = [0] * MAX_SIZE   # 스택 배열

    i = 0                # top (스택 위치)

    j = 0                # 오류 체크용



    for ch in expr:

        # 1. 여는 괄호 → push

        if ch in '([{':

            A[i] = ch

            i += 1



        # 2. 닫는 괄호 → pop

        elif ch in ')]}':

            if i == 0:   # 스택 비었는데 닫힘

                j = 1

                break



            i -= 1

            top = A[i]



            # 3. 짝 검사

            if (ch == ')' and top != '(') or \

               (ch == ']' and top != '[') or \

               (ch == '}' and top != '{'):

                j = 1

                break



    # 4. 최종 검사

    if i == 0 and j == 0:

        return True

    else:

        return False





# 실행

expr = input("수식 입력: ")



if check_bracket(expr):

    print("정상 (괄호 맞음)")

else:

    print("오류 (괄호 틀림)")