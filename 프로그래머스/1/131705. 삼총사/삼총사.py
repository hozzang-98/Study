from itertools import combinations

def solution(numbers):

    number = [-2,3,0,2,-5]
        
    answer = 0
    tmp_set = list(combinations(numbers,3))
    for s in tmp_set:

        if sum(s) == 0:

            answer += 1

    return answer