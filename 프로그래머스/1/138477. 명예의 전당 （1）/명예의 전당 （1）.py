import heapq

def solution(k, score):
    answer = []
    honor = []

    for s in score:
        heapq.heappush(honor, s)  # 점수 추가
        if len(honor) > k:
            heapq.heappop(honor)  # 가장 낮은 점수 제거
        answer.append(honor[0])   # 최하위 점수 기록

    return answer