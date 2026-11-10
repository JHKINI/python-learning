# 04. 자료구조 직접 구현

> 2026년 4월 말 ~ 6월 · 파이썬 자료구조 수업

파이썬의 `list`, `deque`를 그냥 가져다 쓰지 않고, **고정 크기 배열과 노드 연결로 ADT를 직접 만들어 보는 것**이 목표였습니다.
그 다음 직접 만든 자료구조로 계산기, 라인 편집기, 미로 탐색을 구현했습니다.

- 개념 정리 노트: [`CONCEPTS.md`](CONCEPTS.md) (선형·비선형 구조, 빅오 표기법, 리스트·스택·큐·덱)
- `class_0426_0430/`: 수업 시간에 처음 작성한 코드. 함수로 먼저 만들고 → 클래스로 바꾼 흔적이 남아 있습니다.
- 번호가 붙은 파일: 6월에 다시 정리한 최종본

## 최종본 구성

| 번호 | 파일 | 자료구조 | 내용 |
|---|---|---|---|
| 01 | `01_list_array.py` | 리스트 | 배열 기반 ListADT: insert, delete, find, replace, append, clear |
| 02 | `02_list_linked.py` | 리스트 | 노드를 연결한 단순 연결 리스트 버전 |
| 03 | `03_line_editor_flet.py` | 리스트 활용 | 행 삽입·삭제·수정, `test.txt` 저장·불러오기 (Flet GUI) |
| 04 | `04_set_array.py` | 집합 | 배열 기반 SetADT: 포함 검사, 합집합, 교집합, 차집합, 같은 집합인지 비교 |
| 05 | `05_set_linked.py` | 집합 | 연결 구조 버전 |
| 06 | `06_stack_array.py` | 스택 | 배열 기반 StackADT: push, pop, peek (LIFO) |
| 07 | `07_stack_linked.py` | 스택 | 연결 구조 버전 |
| 08 | `08_stack_calculator_flet.py` | 스택 활용 | 연산자 우선순위를 고려해 중위 표기식을 스택 두 개로 계산 (Flet GUI) |
| 09 | `09_maze_dfs_flet.py` | 스택 활용 | 깊이 우선 탐색(DFS) 미로. 막히면 되돌아감 (Flet GUI) |
| 10 | `10_queue_linear_circular.py` | 큐 | 선형 큐와 원형 큐를 한 파일에서 비교 |
| 11 | `11_queue_linear.py` | 큐 | 선형 큐: front/rear 이동을 출력하며 동작 확인 |
| 12 | `12_queue_circular.py` | 큐 | 원형 큐: `(rear + 1) % size`로 공간 재사용 |
| 13 | `13_maze_bfs.py` | 큐 활용 | 너비 우선 탐색(BFS) 미로 |
| 14 | `14_deque_linear.py` | 덱 | 앞/뒤 삽입·삭제 |
| 15 | `15_deque_circular.py` | 덱 | 원형 덱 |
| 16 | `16_priority_queue.py` | 우선순위 큐 | 꺼낼 때 가장 큰 값을 찾아 먼저 내보내는 우선순위 큐 |
| 17 | `17_maze_priority.py` | 우선순위 큐 활용 | 출구까지 거리가 가까운 칸부터 탐색하는 전략 미로 |

## 수업 시간 첫 작성본 (`class_0426_0430/`)

| 주제 | 파일 |
|---|---|
| 연결 리스트 | `0426_linked_list_delete_middle.py`, `0429_linked_stack.py` |
| 리스트 ADT | `0429_list_adt_functions.py` (전역 변수 + 함수) → `0429_list_adt_class.py` (클래스) → `0429_line_editor.py` |
| 집합 ADT | `0429_set_functions.py` → `0429_set_class.py` |
| 스택 활용 | `0429_stack_calculator.py`, `0429_stack_bracket_check.py` (괄호 짝 검사) |
| 표기식 변환 | 중위→후위, 중위→전위, 후위→중위, 후위→전위, 한 파일에 모은 버전 |
| 큐·덱 | 원형 큐, 원형 덱, 리스트로 만든 우선순위 큐, `collections.deque`를 큐/스택처럼 쓰기 |
| 실험 | `0429_queue_module_test.py`: `queue.Queue`가 가득 차거나 비었을 때 **멈춘 것처럼 대기한다**는 것을 직접 확인 (실행하면 일부러 멈춤) |
| 미로 | `0429_maze_dfs.py`: 스택으로 만든 DFS 미로 첫 버전 |

`extra/`에는 파이썬 `list`로 만든 ArrayList와 콘솔 라인 편집기(5/28)가 있습니다.

## 실행 예시: 전략 미로 (`17_maze_priority.py`)

```text
현재 위치: (2, 3) 출구까지 거리: 4
현재 위치: (3, 3) 출구까지 거리: 3
현재 위치: (4, 3) 출구까지 거리: 2
현재 위치: (4, 4) 출구까지 거리: 1
현재 위치: (4, 5) 출구까지 거리: 0
출구 발견!
```

## 배운 점

- 같은 ADT를 배열과 연결 구조로 각각 만들어 보면서, 배열은 인덱스 접근이 빠르지만 중간 삽입·삭제가 느리고 크기가 고정된다는 차이를 직접 확인했습니다.
- 선형 큐에서 앞쪽 공간이 낭비되는 문제를 겪고 나서 원형 큐가 왜 필요한지 이해했습니다.
- 같은 미로를 스택(DFS), 큐(BFS), 우선순위 큐(거리 기준)로 풀면서 자료구조 선택에 따라 탐색 순서가 달라지는 것을 비교했습니다.

## 실행 환경

- Python 3.13
- Flet (03, 08, 09 GUI 예제)
