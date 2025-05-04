from heapq import heappush, heappop

def solution(jobs):

    jobs.sort()  # 요청 시간 기준 정렬
    heap = []  # 실행 대기 작업 저장할 최소 힙
    now, i, answer = 0, 0, 0
    job_index = 0  # jobs 배열의 현재 인덱스
    
    while i < len(jobs):  # 모든 작업이 완료될 때까지 반복
        # 현재 시간(now)까지 요청된 모든 작업을 heap에 추가
        while job_index < len(jobs) and jobs[job_index][0] <= now:
            heappush(heap, [jobs[job_index][1], jobs[job_index][0]])  # [소요 시간, 요청 시간]
            job_index += 1
        
        if heap:  # 수행할 작업이 존재하면
            cur = heappop(heap)  # 소요 시간이 가장 적은 작업 선택
            now += cur[0]  # 현재 시간 갱신
            answer += now - cur[1]  # 요청 시각부터 종료 시각까지 걸린 시간 누적
            i += 1  # 완료된 작업 개수 증가
        else:
            now = jobs[job_index][0]  # 다음 작업이 들어오는 시간으로 건너뜀

    return answer // len(jobs)