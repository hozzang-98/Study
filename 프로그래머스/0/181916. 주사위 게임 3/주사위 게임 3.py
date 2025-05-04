from collections import Counter

def solution(a, b, c, d):
    counts = Counter([a, b, c, d])  # 주사위 숫자의 빈도 계산
    items = sorted(counts.items(), key=lambda x: -x[1])  # 빈도 기준으로 내림차순 정렬

    if items[0][1] == 4:  # p p p p (모두 같음)
        return 1111 * items[0][0]
    
    if items[0][1] == 3:  # p p p q
        p, q = items[0][0], items[1][0]
        return (10 * p + q) ** 2
    
    if items[0][1] == 2:
        if len(items) == 2:  # p p q q
            p, q = items[0][0], items[1][0]
            return (p + q) * abs(p - q)
        else:  # p p q r
            return items[1][0] * items[2][0]

    return min(items)[0]  # p q r s (모두 다름)