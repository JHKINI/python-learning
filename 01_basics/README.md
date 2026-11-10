# 01. 파이썬 문법 기초

> 2026년 3월 ~ 4월 초 · 폴리텍 AI소프트웨어과 파이썬 수업 (Python 3.13)

변수, 자료형, 반복문, 함수 같은 문법을 직접 쳐보면서 익힌 단계입니다.
이 단계의 손필기는 [`notes/python.md`](../notes/python.md)에 정리해 두었습니다.

## 파일 목록

| 파일 | 내용 |
|---|---|
| `01_output.py` ~ `05_loops.py` | 출력, 주석, 변수·캐스팅, 대소문자 구분, `range()`와 `for`문 (처음 정리한 노트: [`first_notes.md`](first_notes.md)) |
| `06_variable_memory.py` | 변수와 대입 연산자. "값이 어딘가에 기록되고, 그 주소를 변수가 알고 있다"는 개념을 주석으로 정리 |
| `07_tuple_set.py` | 튜플 안의 리스트는 수정할 수 있다는 점, 세트 안에 튜플 넣기, 딕셔너리 접근, 문자열 → 정수 형변환 |
| `08_dictionary_comprehension.py` | `dict()` 생성, 딕셔너리 컴프리헨션, `sorted()` |
| `09_function_arguments.py` | 기본값 매개변수, 키워드 인자, 여러 값 반환과 언패킹 |
| `10_function_sales.py` | 가격 × 수량을 계산하는 함수 + `input()` |
| `11_is_prime.py` | 소수 판별 함수 (설계 메모는 [`drafts/is_prime_design.py`](../drafts/is_prime_design.py)) |
| `12_basics_review.py` | 출력·주석·변수·캐스팅 복습 |
| `notebooks/` | Colab 실습: 짝수 추출, 개수·합·평균, 입력값 예외 처리 |

## 이 단계에서 익힌 것 (필기 요약)

- **값 교환**: `A[0] = A[1]`을 바로 쓰면 값이 덮어써진다. 그래서 임시 변수 `n`을 쓰거나 파이썬식 `A[0], A[1] = A[1], A[0]`으로 바꾼다.
- **이중 for문**: 바깥 `for`는 기준 위치를 고정하고, 안쪽 `for`는 그 뒤의 값들과 비교한다. 이 흐름이 나중에 선택 정렬로 이어졌다.
- **컴프리헨션 원칙**: 결과를 먼저 쓰고 반복은 뒤에 쓴다. 예) `{item: random.randrange(3000, 15001, 500) for item in 물품}`
- **도움말 찾기**: `help(a.append)`, `dir(a)`로 쓸 수 있는 메서드를 직접 확인했다.
- **파일 입출력**: `r` / `w` / `a` / `+` 모드의 차이를 익히고, `with open(...) as f:`를 쓰면 `close()`를 하지 않아도 정리된다는 것을 배웠다. `f.tell()`, `f.seek()`, `f.readline()`도 다뤘다.

## 실행

```bash
python 01_basics/05_loops.py
```
