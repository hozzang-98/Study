def solution(diffs, times, limit):
    def is_valid(level):
        now = 0
        time_prev = 0
        for diff, time in zip(diffs, times):
            if diff <= level:
                now += time
            else:
                now += (diff - level) * (time + time_prev) + time
            time_prev = time
            if now > limit:
                return False
        return True

    left, right = 1, max(diffs)
    answer = right

    while left <= right:
        mid = (left + right) // 2
        if is_valid(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer