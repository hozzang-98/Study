from collections import Counter

def solution(X, Y):
    x_count = Counter(X)  # X의 숫자 개수 (문자 형태)
    y_count = Counter(Y)  # Y의 숫자 개수 (문자 형태)

    common_numbers = []
    for num in map(str, range(9, -1, -1)):  # 숫자를 문자열로 변환하여 확인
        if num in x_count and num in y_count:
            common_numbers.extend([num] * min(x_count[num], y_count[num]))

    if not common_numbers:
        return "-1"
    
    result = "".join(common_numbers)
    return "0" if result[0] == "0" else result