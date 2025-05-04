def solution(people, limit):

    people.sort()  # 몸무게 오름차순 정렬
    left, right = 0, len(people) - 1
    answer = 0

    while left <= right:
    
        if people[left] + people[right] <= limit:  # 가장 가벼운 사람 + 가장 무거운 사람 태울 수 있음
        
            left += 1  # 가벼운 사람 태움

        right -= 1  # 무거운 사람 태움 (항상 pop)

        answer += 1  # 보트 1개 사용

    return answer
