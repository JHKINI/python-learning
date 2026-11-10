# 05. 알고리즘: 정렬 · 탐색 · 트리 · 그래프

> 2026년 4월 말 ~ 5월 · 자료구조 수업 후반부

필기에 남긴 "숫자 3개를 큰 순서대로 바꾸려면?"이라는 질문(값 교환 → 이중 for문)에서 시작해서, 정렬과 탐색, 트리, 그래프 알고리즘까지 이어졌습니다.

## 시작: 선택 정렬

| 파일 | 내용 |
|---|---|
| `0430_selection_sort.py` | 수업 시간에 작성한 선택 정렬 |
| `selection_sort_practice.ipynb` | 같은 코드를 노트북에서 다시 연습 |

## 교재 예제 실습 (`textbook/`)

교재 예제를 직접 쳐보면서 각 함수가 하는 일을 주석으로 정리한 파일입니다.

| 분류 | 파일 |
|---|---|
| 정렬 | `01_selection_sort`, `18_heap_sort`, `19_quick_sort` |
| 집합 · 탐색 · 맵 | `02_set_operations`, `03_sequential_search`, `04_map_wordbook` (단어장) |
| 트리 | `05_binary_tree_traversal` (전위·중위·후위·레벨 순회), `06_morse_code_tree` (모스 부호 결정 트리), `09_bst_map` (이진 탐색 트리 삽입·삭제), `10_avl_tree` (LL·RR·LR·RL 회전) |
| 힙 | `07_max_heap`, `08_huffman_code` (최소 힙으로 허프만 코드 만들기) |
| 그래프 | `11_graph_dfs_bfs` (연결 성분, 신장 트리), `12_topological_sort`, `13_weighted_graph` |
| 최소 신장 트리 | `14_mst_kruskal` (Union-Find), `15_mst_prim` |
| 최단 경로 | `16_dijkstra`, `17_floyd_warshall` |

## 복습용 요약 (`review/`)

같은 주제를 짧게 다시 정리한 버전입니다.
`01_priority_queue_sorted_list` ~ `15_advanced_sorts` (해시 선형 조사, 이진 탐색, 삽입·버블 정렬 등 포함)

## 실행

모든 파일이 표준 라이브러리만 사용합니다.

```bash
python 05_algorithms/textbook/16_dijkstra.py
```
