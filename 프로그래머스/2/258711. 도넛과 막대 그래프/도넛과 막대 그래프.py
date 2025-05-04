def solution(edges):
    s = 0
    d_cnt = 0 # 도넛
    b_cnt = 0 # 막대
    e_cnt = 0 # 8자
    edge_cnt_dic = {} # edge_num : [in_cnt, out_cnt]

    for edge_in, edge_out in edges:
    
        if not edge_in in edge_cnt_dic.keys():

            edge_cnt_dic[edge_in] = [0,0]

        if not edge_out in edge_cnt_dic.keys():

            edge_cnt_dic[edge_out] = [0,0]

        edge_cnt_dic[edge_in][0] += 1
        edge_cnt_dic[edge_out][1] += 1


    for k,v in edge_cnt_dic.items():

        out_ = v[0]
        in_ = v[1]

        if (out_ >= 2)  & (in_ == 0):

            s = k

        elif (out_ == 0) & (in_ > 0):

            b_cnt += 1

        elif (out_ >= 2) & (in_ >= 2):

            e_cnt += 1
        
    answer = [s,d_cnt,b_cnt,e_cnt]
    d_cnt = edge_cnt_dic[s][0] - b_cnt - e_cnt

    answer = [s,d_cnt,b_cnt,e_cnt]
    
    return answer