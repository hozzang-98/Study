def solution(friends, gifts):
    n = len(friends)
    name_to_idx = {name: i for i, name in enumerate(friends)}
    gift_score = [0] * n
    history = [[0] * n for _ in range(n)]

    # 선물 내역 저장
    for g in gifts:
        a, b = g.split()
        ai, bi = name_to_idx[a], name_to_idx[b]
        history[ai][bi] += 1
        gift_score[ai] += 1
        gift_score[bi] -= 1

    answer = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if i == j:
                continue
            if history[i][j] > history[j][i]:
                cnt += 1
            elif history[i][j] == history[j][i] and gift_score[i] > gift_score[j]:
                cnt += 1
        answer = max(answer, cnt)

    return answer