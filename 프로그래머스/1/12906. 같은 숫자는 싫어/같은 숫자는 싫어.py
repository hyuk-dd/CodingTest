from collections import deque

def solution(arr):
    answer = []
    
    deq = deque(arr)
    a = deq.popleft()

    for _ in range(len(deq)):
        q = deq.popleft()
        # print(q)
        if a != q:
            answer.append(a)
            a = q
    answer.append(a)
    
    return answer