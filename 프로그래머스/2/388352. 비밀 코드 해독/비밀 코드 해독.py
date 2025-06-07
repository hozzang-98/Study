from itertools import combinations

def solution(n, q, ans):
    
    count = 0
    for candidate in combinations(range(1, n+1), 5):
     
        valid = True

        for trial, answer in zip(q, ans):

            if len(set(candidate) & set(trial)) != answer:
                valid = False
                break
            
        if valid: count += 1

    return count