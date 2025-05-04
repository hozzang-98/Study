from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for i in course:  # 코스 요리의 메뉴 개수
        temp = []  
        
        for order in orders:
            temp.extend(combinations(sorted(order), i))  # 조합 리스트에 추가
        
        counter = Counter(temp)  # 조합 등장 횟수 계산
        if not counter:  # 빈 딕셔너리면 패스
            continue

        max_count = max(counter.values())  # 가장 많이 등장한 횟수 찾기
        if max_count < 2:  # 2번 미만으로 주문된 조합은 제외
            continue

        # 가장 많이 주문된 조합을 answer에 추가
        answer.extend(''.join(menu) for menu, count in counter.items() if count == max_count)

    return sorted(answer)  # 정렬 후 반환