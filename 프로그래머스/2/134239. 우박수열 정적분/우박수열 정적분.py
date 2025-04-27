def ubak(k):
    result = []
    while k != 1:
        result.append(k)
        k = k // 2 if k % 2 == 0 else k * 3 + 1
    result.append(1)
    return result

def solution(k, ranges):
    answer = []
    ubak_list = ubak(k)
    n = len(ubak_list) - 1  # 마지막 인덱스

    for a, b in ranges:
        start = a
        end = n + b

        if start > end:
            answer.append(-1)
            continue

        total = 0
        for i in range(start, end):
		        # 사다리꼴 공식 = (윗변 + 아랫변) * 높이 / 2 
		        # 높이 1 고정
            total += (ubak_list[i] + ubak_list[i+1]) / 2

        answer.append(total)

    return answer