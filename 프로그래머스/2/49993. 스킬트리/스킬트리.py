def solution(skill, skill_trees):
    
    answer = 0
    
    for skill_tree in skill_trees:
        
        temp = ''
        
        for char in skill_tree: 
            
            if char in skill: # 스킬이 스킬트리에 있으면 추가
                
                temp += char
                
        if temp == skill[:len(temp)]: # 스킬들이 스킬트리 순서대로 되어있으면 count
            
            answer += 1
            
    return answer