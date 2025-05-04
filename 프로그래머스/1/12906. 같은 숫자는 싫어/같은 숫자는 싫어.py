from collections import deque

def solution(arr):
    
    answer = []
    dq = deque(arr)
    i = dq.popleft()
    answer.append(i)

    while dq:

        i = dq.popleft()

        if i != answer[-1]:

            answer.append(i)

    return answer
            
            