def solution(players, m, k):
    
    answer = 0

    server = [0 for i in range(len(players))]
    
    for idx, player in enumerate(players):

        need_server_cnt = 0

        if player >= m:

            need_server_cnt = player // m
            
            if server[idx] < need_server_cnt:

                add_server_cnt = need_server_cnt - server[idx]

                if need_server_cnt * m <= player < (need_server_cnt+1) * m:

                    answer += add_server_cnt
                    
                    for i in range(k):

                        if idx + i < len(server):

                            server[idx+i] += add_server_cnt
                        
                        else: break
                        
    return answer