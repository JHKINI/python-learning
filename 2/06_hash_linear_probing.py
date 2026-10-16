# 해싱 - 선형 조사법
# coding: utf-8
SIZE = 10
EMPTY = None
DELETED = 'deleted'
table = [EMPTY] * SIZE

def hash_func(key):
    return key % SIZE

def insert(key):
    idx = hash_func(key)
    start = idx
    while table[idx] not in (EMPTY, DELETED):
        idx = (idx + 1) % SIZE
        if idx == start:
            print('해시 테이블이 가득 찼습니다.')
            return
    table[idx] = key

def search(key):
    idx = hash_func(key)
    start = idx
    while table[idx] is not EMPTY:
        if table[idx] == key:
            return idx
        idx = (idx + 1) % SIZE
        if idx == start:
            break
    return -1

def delete(key):
    idx = search(key)
    if idx != -1:
        table[idx] = DELETED

for x in [35, 25, 15, 26, 46]:
    insert(x)
print(table)
print('26 위치:', search(26))
delete(25)
print(table)
