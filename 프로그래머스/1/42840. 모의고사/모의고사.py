def solution(answers):

    patterns = [
        [1, 2, 3, 4, 5],  
        [2, 1, 2, 3, 2, 4, 2, 5],  
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    # 각 수포자의 점수 계산 (리스트 컴프리헨션 활용)
    scores = [sum(a == p[i % len(p)] for i, a in enumerate(answers)) for p in patterns]

    # 최고 점수를 가진 수포자 찾기
    max_score = max(scores)

    # 최고 점수를 가진 사람들 반환 (1번부터 시작하므로 index + 1)
    return [i + 1 for i, score in enumerate(scores) if score == max_score]