def solution(prices): # [1.2.3.2.3]

    n = len(prices)
    answer = [0] * n  # 결과 리스트 (초기값 0)
    stack = []  # 인덱스를 저장하는 스택

    for i in range(n):
    
        while stack and prices[stack[-1]] > prices[i]:  # 가격이 떨어지면 (이전 인덱스의 price > 이번 인덱스 price)
            
            idx = stack.pop()  # 이전 인덱스를 꺼냄
            answer[idx] = i - idx  # 지속된 시간 계산
            
        stack.append(i)  # 현재 인덱스를 스택에 추가

    while stack:  # 스택에 남아있는 인덱스는 끝까지 가격이 유지된 경우
    
        idx = stack.pop()
        answer[idx] = n - 1 - idx  # 마지막까지 유지된 시간

    return answer