def solution(s):
    if len(s) == 1:
        return 1

    min_length = len(s)

    for step in range(1, len(s)//2 + 1):
        compressed = ""
        prev = s[:step]
        count = 1

        for i in range(step, len(s) + step, step):
            current = s[i:i+step]
            if prev == current:
                count += 1
            else:
                compressed += (str(count) + prev) if count > 1 else prev
                prev = current
                count = 1

        min_length = min(min_length, len(compressed))

    return min_length