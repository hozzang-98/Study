import math
from collections import Counter

def solution(progresses, speeds):

    answer = []

    for progress, speed in zip(progresses, speeds):

        work = math.ceil((100 - progress) / speed) # 7, 3, 9

        if len(answer) == 0 or answer[-1][0] < work:
            
            answer.append([work, 1])

        else:

            answer[-1][1] += 1

    return [i[1] for i in answer]
 
