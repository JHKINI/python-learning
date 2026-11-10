#기본코드
import queue

Q = queue.Queue(maxsize=20)

for v in range(1, 10):
    Q.put(v)

print("큐의 내용:", end=' ')
for _ in range(1, 10):
    print(Q.get(), end=' ')

print()
#공백상태에서 get()하면 멈춘것처럼 보임
import queue

Q = queue.Queue(maxsize=3)

print(Q.get())
#수정버전
if not Q.empty():
    print(Q.get())
else:
    print("큐가 비어있음")

#maxsize 이상 put()하면? 이것도 멈춘것처럼 보임.
import queue

Q = queue.Queue(maxsize=3)

Q.put(1)
Q.put(2)
Q.put(3)
Q.put(4)
#안전하게 하려면
if not Q.full():
    Q.put(4)
else:
    print("큐가 가득 참")

# maxsize=0이면 무한대 크기 큐 처럼 동작함 
import queue

Q = queue.Queue(maxsize=0)

for v in range(1, 100):
    Q.put(v)

print("입력 완료")
#empty(), full() 필요? 필요함 조건안맞으면 멈춘것처럼 대기하기때문에
if not Q.empty():
    print(Q.get())

if not Q.full():
    Q.put(10)
#queue.Queue에서 get()은 큐가 비어 있으면 대기하고,
#put()은 큐가 가득 차 있으면 대기한다.
#따라서 empty(), full()로 상태를 확인하는 것이 안전하다.