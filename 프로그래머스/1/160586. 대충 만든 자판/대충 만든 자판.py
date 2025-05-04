def solution(keymap, targets):
    
    answer = []

    for target in targets:
        
        count = 0

        for s in target:
            
            flag = False
            now = 101

            for key in keymap:

                if s in key:
                    now = min(key.index(s)+1, now)
                    flag = True

            if not flag:
                
                count = -1
                break


            count += now

        answer.append(count)
        

    return answer