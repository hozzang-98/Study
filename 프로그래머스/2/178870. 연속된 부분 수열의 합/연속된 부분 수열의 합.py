def solution(sequence, k):
    n = len(sequence)
    max_sum = 0
    end = 0 # pointer_2
    interval = n # 길이가 짧은 수열을 찾기 위한 변수, 초기값은 리스트의 길이, 이후에는 새로운 길이로 초기화
    
    # start - pointer_1
    for start in range(n):

        while max_sum < k and end < n: 

            max_sum += sequence[end] 
            end += 1 #

        # 이미 end가 1 증가된 상태기 때문에 1을 빼주고 확인해야함
        if max_sum == k and (end-1) - start < interval:

            answer = [start, end-1]
            interval = (end-1) - start

        # 만약 max_sum이 k가 아니라면 start 값을 빼줌
        max_sum -= sequence[start]
        # end는 따로 초기화 필요 X 

    return answer