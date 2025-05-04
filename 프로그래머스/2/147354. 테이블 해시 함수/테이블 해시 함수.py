def solution(data, col, row_begin, row_end):
    # 정렬 (1. col 번째 컬럼 기준 오름차순, 2. 첫 번째 컬럼 기준 내림차순)
    data.sort(key=lambda x: (x[col-1], -x[0]))

    result = 0
    for i in range(row_begin, row_end + 1):
        S_i = sum(n % i for n in data[i-1])  # 각 값의 나머지 합
        result ^= S_i  # XOR 연산
    
    return result