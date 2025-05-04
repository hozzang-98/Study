def solution(n, times):
    answer = 0
    min_time = 1
    max_time = max(times) * n
    
    while min_time <= max_time:

        mid = (min_time+max_time)//2 
        done = 0
        for time in times:

            done += mid // time 

            if done >= n: 

                break

        if done >= n:

            answer = mid

            max_time = mid - 1

        else:

            min_time = mid + 1

    return answer