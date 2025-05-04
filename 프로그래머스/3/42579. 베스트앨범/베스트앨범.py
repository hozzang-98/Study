def solution(genres, plays):
    dic = {} # 노래 별 재생 횟수, 인덱스
    total_dic = {} # 전체 재생 횟수
    answer = []
    for i in range(len(genres)):
        if genres[i] in dic:
            dic[genres[i]] += [(plays[i],i)]
        else:
            dic[genres[i]] = [(plays[i],i)]

    for i in range(len(genres)):
        if genres[i] in total_dic:
            total_dic[genres[i]] += plays[i]
        else:
            total_dic[genres[i]] = plays[i]

    total_dic = sorted(total_dic.items(),key=lambda x:x[1],reverse=True)

    for genre, num_play in total_dic:
        dic[genre] = sorted(dic[genre],key=lambda x:(-x[0],x[1]))
        answer += [idx for (play,idx) in dic[genre][:2]]
        
    return answer