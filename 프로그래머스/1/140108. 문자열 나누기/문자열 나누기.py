def solution(s):
    
    answer = 0
    same, diff = 0, 0
    x = s[0]

    for i, c in enumerate(s):
        if c == x:
            same += 1
        else:
            diff += 1

        if same == diff:
            answer += 1
            if i + 1 < len(s):
                x = s[i + 1]
            same = 0
            diff = 0

    # 루프에서 같은 수가 안 맞아서 끝났다면 마지막 분해 포함
    if same != 0 or diff != 0:
        answer += 1

    return answer