import math
from itertools import permutations

def isprime(N):
    if N == 0 or N == 1:
        return False
    if N == 2 or N == 3:
        return True
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    nums = set()
    
    for i in range(1, len(numbers)+1): # 3

        nums |= set(map(''.join,permutations(numbers,i))) # 집합 += 집합

    nums = set(map(int,nums))
    for i in nums:
        if isprime(i):
            answer += 1
    return answer