from collections import deque

def solution(lottos, win_nums):
    answer = [0,0] # 최고, 최저
    cnt_0 = lottos.count(0)
    rank = [6,6,5,4,3,2,1]
    for lotto in lottos:
        if lotto in win_nums:
            answer[0] += 1
            answer[1] += 1
    
    answer[0] += cnt_0
    
    
    
    return rank[answer[0]], rank[answer[1]]