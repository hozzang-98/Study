def solution(absolutes, signs):
    answer = 0
    for v, s in zip(absolutes, signs):
        if s == True:
            answer += v
        else:
            answer -= v
    return answer