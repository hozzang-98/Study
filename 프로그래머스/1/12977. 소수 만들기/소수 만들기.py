from itertools import combinations

def isprime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
    
def solution(nums):
    answer = 0
    
    for c in combinations(nums, 3):   # 3개 숫자 조합
        s = sum(c)
        if isprime(s):          # 합이 소수라면
            answer += 1              # 카운트 증가

    return answer