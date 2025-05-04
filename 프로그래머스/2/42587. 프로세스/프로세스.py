from collections import deque

def solution(priorities, location):
    answer = 0
    dq = deque([(priority, idx) for idx, priority in enumerate(priorities)])
    
    while dq:
        # 큐에서 첫 번째 프로세스를 꺼냄
        i = dq.popleft()
        
        # 큐에서 우선순위가 더 높은 프로세스가 있으면, 현재 프로세스는 다시 큐에 넣음
        if any(i[0] < p[0] for p in dq):
            dq.append(i)
        else:
            # 우선순위가 더 높은 프로세스가 없으면 실행
            answer += 1
            if i[1] == location:
                return answer

    return answer