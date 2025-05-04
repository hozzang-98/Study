from collections import deque

def solution(numbers, target):
    answer = 0
    n = len(numbers)
    q = deque()
    q.append([numbers[0],0])
    q.append([-1*numbers[0],0])
    while q:
        temp, idx = q.popleft()
        idx += 1
        if idx < n:
            q.append([temp+numbers[idx],idx])
            q.append([temp-numbers[idx],idx])
        elif temp == target:
                answer += 1
    
    return answer