from collections import deque

def solution(begin, target, words):
    
    answer = 0
    q = deque([[begin,0]])
    v = [0 for i in range(len(words))]
    while q:
        word,cnt = q.popleft()
        if word == target:
            answer= cnt
            break
        for i in range(len(words)):
            tmp_cnt = 0
            if v[i] == 0:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        tmp_cnt += 1
                if tmp_cnt == 1:
                    q.append([words[i],cnt+1])
                    v[i] = 1
    return answer