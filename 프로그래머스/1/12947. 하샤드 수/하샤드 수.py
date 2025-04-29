def solution(x):
    sum_of_digits = sum(int(digit) for digit in str(x))
    return x % sum_of_digits == 0