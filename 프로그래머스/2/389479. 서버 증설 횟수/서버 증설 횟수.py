def solution(players, m, k):
    
    n = len(players)
    server = [0] * n
    answer = 0

    for time in range(n):
        needed = players[time] // m

        if needed > server[time]:
            add = needed - server[time]
            answer += add

            # k시간 동안 추가 서버 적용
            for j in range(k):
                if time + j < n:
                    server[time + j] += add
                else:
                    break

    return answer