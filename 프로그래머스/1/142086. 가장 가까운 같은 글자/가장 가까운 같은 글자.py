def solution(s):
    answer = []
    for i in range(len(s)):
        
        if s[i] in s[:i]:
            answer.append(i - s[:i].rindex(s[i]))

        else:
            answer.append(-1)
                
    return answer