def solution(picks, minerals):
    answer = 0
    max_pick = 0
    for x in picks:
        max_pick += x
    # 캘 수 있는 광물의 개수
    max_minerals = max_pick * 5
    
    if len(minerals) > max_minerals: # 주어진 광물이 캘 수 있는 광물 수보다 크면
        minerals = minerals[:max_minerals]
        
    cnt_min = [[0, 0, 0] for _ in range((len(minerals) + 4) // 5)] # dia, iron, stone
    
    for i in range(len(minerals)):
        if minerals[i] == 'diamond': 
            cnt_min[i//5][0] += 1
        elif minerals[i] == 'iron': 
            cnt_min[i//5][1] += 1
        else : 
            cnt_min[i//5][2] += 1
    
    cnt_min.sort(key=lambda x:(-x[0],-x[1],-x[2]))
    
    #정렬된 광물들을 다이아,철,돌 곡괭이 순서대로 캔다.
    fatigue = [[1, 1, 1],        # 다이아 곡괭이
            [5, 1, 1],        # 철 곡괭이
            [25, 5, 1]]     # 돌 곡괭이
										
    for dia, iron, stone in cnt_min:
        for i in range(3):
            if picks[i] > 0:
                picks[i] -= 1
                answer += dia * fatigue[i][0] + iron * fatigue[i][1] + stone * fatigue[i][2]
                break
        
    return answer