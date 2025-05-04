import re

def solution(dartResult):

    p = re.compile(r'(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    
    scores = []

    for i, (num, bonus, option) in enumerate(dart):
        score = int(num) ** {"S": 1, "D": 2, "T": 3}[bonus]

        if option == "*":
            if scores:
                scores[-1] *= 2
            score *= 2
        elif option == "#":
            score *= -1

        scores.append(score)

    return sum(scores)