import heapq

def solution(n, works):

    # 모든 작업을 처리할 수 있는 경우
    if sum(works) <= n: return 0
    
    # heapq는 최소힙이므로 최대힙으로 활용하기 위해 음수로 만듬
    works = [-work for work in works]
    heapq.heapify(works)
    
    for _ in range(n):
        
        work = heapq.heappop(works) + 1 # 최댓값 꺼내서 작업 1 처리
        heapq.heappush(works, work)
    
    answer = sum([work ** 2 for work in works])
    
    return answer

# solution(n, works)