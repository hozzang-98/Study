def solution(sizes):

    answer = 0

    w = max([max(size) for size in sizes])
    h = max([min(size) for size in sizes])

    answer += w*h

    return answer