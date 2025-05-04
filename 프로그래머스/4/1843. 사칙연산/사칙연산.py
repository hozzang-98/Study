def solution(arr):
    n = (len(arr) + 1) // 2  # 숫자의 개수

    nums = [int(arr[i]) for i in range(0, len(arr), 2)]
    ops = [arr[i] for i in range(1, len(arr), 2)]

    # DP 테이블 초기화 (최댓값, 최솟값 저장)
    M = [[0] * n for _ in range(n)]
    m = [[0] * n for _ in range(n)]

    # Base case: 한 개의 숫자만 있는 경우
    for i in range(n):
        M[i][i] = nums[i]
        m[i][i] = nums[i]

    # 부분 수열의 길이를 1부터 점점 늘려가며 계산
    for d in range(1, n):  
        for i in range(n - d):  
            j = i + d  # 끝점
            maxcandidates, mincandidates = [], []

            for k in range(i, j):  
                if ops[k] == '-':
                    maxcandidates.append(M[i][k] - m[k+1][j])
                    mincandidates.append(m[i][k] - M[k+1][j])
                else:
                    maxcandidates.append(M[i][k] + M[k+1][j])
                    mincandidates.append(m[i][k] + m[k+1][j])

            M[i][j] = max(maxcandidates)
            m[i][j] = min(mincandidates)

    return M[0][n-1]