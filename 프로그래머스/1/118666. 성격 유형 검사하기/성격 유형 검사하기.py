from collections import defaultdict

def solution(survey, choices):
    
    score = defaultdict(int)
    types = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]

    for sv, ch in zip(survey, choices):
        if ch < 4:
            score[sv[0]] += 4 - ch
        elif ch > 4:
            score[sv[1]] += ch - 4

    return ''.join(a if score[a] >= score[b] else b for a, b in types)