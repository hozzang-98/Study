from collections import deque

def solution(bandage, health, attacks):

    answer = health
    attacks = deque(attacks)

    i = 1
    cnt = 0 # 연속 성공

    while len(attacks) > 0:

        # 공격 시점
        if i == attacks[0][0]:
            
            attack = attacks.popleft()
            cnt = 0 # 연속 성공 초기화  

            answer -= attack[1]

            if answer <= 0:

                return -1
            
        else:

            answer += bandage[1]

            if answer >= health: # 최대 체력 제한

                answer = health

            cnt += 1

            if cnt == bandage[0]:

                answer += bandage[2]

                if answer >= health:

                    answer = health

                cnt = 0

        i += 1

    return answer