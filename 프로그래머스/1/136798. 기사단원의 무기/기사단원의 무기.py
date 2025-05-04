def cnt(number):
    count = 0
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            count += 1
            if i < number // i:
                count += 1
    return count

def solution(number, limit, power):
    answer = 0
    for i in range(1, number + 1):
        div = cnt(i)
        if div > limit:
            answer += power
        else:
            answer += div
    return answer