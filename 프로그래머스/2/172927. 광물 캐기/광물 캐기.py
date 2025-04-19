def solution(picks, minerals):
    answer = 0
    max_pick = 0
    for x in picks:
        max_pick += x
    # 캘 수 있는 광물의 개수
    max_minerals = max_pick * 5
    
    if len(minerals) > max_minerals: # 주어진 광물이 캘 수 있는 광물 수보다 크면
        minerals = minerals[:max_minerals]
        
    cnt_min = [[0,0,0] for _ in range((len(minerals) //5 +1))] # dia, iron, stone
    
    for i in range(len(minerals)):
        if minerals[i] == 'diamond': 
            cnt_min[i//5][0] += 1
        elif minerals[i] == 'iron': 
            cnt_min[i//5][1] += 1
        else : 
            cnt_min[i//5][2] += 1
    
    cnt_min.sort(key=lambda x:(-x[0],-x[1],-x[2]))
    
    #정렬된 광물들을 다이아,철,돌 곡괭이 순서대로 캔다.
    for i in cnt_min:
         dia,iron,stone = i
         for j in range(len(picks)):
            if picks[j]>0 and j==0:
                picks[j]-=1
                answer += dia + iron + stone
                break
            elif picks[j]>0 and j==1:
                picks[j]-=1
                answer += (5*dia) + iron + stone
                break
            elif picks[j]>0 and j==2:
                picks[j]-=1
                answer += (25*dia) + (5*iron) + stone
                break
        
    return answer