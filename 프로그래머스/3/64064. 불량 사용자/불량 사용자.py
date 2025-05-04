from itertools import permutations
import re

def solution(user_id, banned_id):

    answer = 0

    ban = '_'.join(banned_id).replace('*','.') # pattern 생성: 정규 표현식 '.' 을 활용해 어느 문자가 오던 일치

    temp = set()

    for i in permutations(user_id,len(banned_id)): # 순열 생성

        if re.fullmatch(ban,'_'.join(i)): # pattern과 완전 일치하면 

            temp.add('_'.join(sorted(i)))

    answer += len(temp)

    return answer