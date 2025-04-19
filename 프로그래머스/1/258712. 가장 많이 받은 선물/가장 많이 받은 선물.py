from collections import defaultdict

def solution(friends, gifts):
    
    answer = 0
    n = len(friends)
    dic = {friend:[0,0] for friend in friends} # give, take
    gift_idx = [0]*n
    friends_idx = {friend:idx for idx, friend in enumerate(friends)}
    
    table = [[0] * n for _ in range(n)]
    
    for gift in gifts:
        
        give, take = gift.split()
        giver_idx, taker_idx = friends_idx[give], friends_idx[take]
        gift_idx[giver_idx] += 1
        gift_idx[taker_idx] -= 1
        table[giver_idx][taker_idx] += 1

    result = [0] * n
    for i in range(n):

        for j in range(n):
            
            if i == j: continue
            
            diff = table[i][j] - table[j][i]
            if diff > 0:
                result[i] += 1
            
            elif diff == 0:
                
                if gift_idx[i] > gift_idx[j]:
                    
                    result[i] += 1
                    
    return max(result)