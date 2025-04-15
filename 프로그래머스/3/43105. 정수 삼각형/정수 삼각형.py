def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            left = triangle[i-1][j-1] if j > 0 else 0
            right = triangle[i-1][j] if j < len(triangle[i-1]) else 0
            triangle[i][j] += max(left, right)
    return max(triangle[-1])