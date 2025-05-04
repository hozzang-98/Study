from heapq import heapify, heappop, heappush

def solution(scoville, K):

    heapify(scoville)  # 최소 힙 생성
    mix_count = 0  # 섞는 횟수

    while len(scoville) > 1 and scoville[0] < K:
        
        heappush(scoville, heappop(scoville) + 2 * heappop(scoville))
        mix_count += 1

    return mix_count if scoville[0] >= K else -1  # K 이상이면 mix_count 반환, 아니면 -1