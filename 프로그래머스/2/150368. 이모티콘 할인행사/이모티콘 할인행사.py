def solution(users, emoticons):
    
    answer = [0, 0]
    discount_rates = [10, 20, 30, 40]
    discount_combinations = []

    def dfs(tmp, d):  # 모든 경우의 할인율 조합을 구함
        
        if d == len(tmp):
            
            discount_combinations.append(tmp[:])
            return
        
        for discount_rate in discount_rates:
            tmp[d] = discount_rate
            dfs(tmp, d + 1)

    dfs([0] * len(emoticons), 0)

    for discount_combination in discount_combinations:
        
        cnt = 0
        sales = 0
        
        for discount_limit, price_limit in users:
            
            pay = 0
            
            for emoticon, rate in zip(emoticons, discount_combination):
                
                if rate >= discount_limit:
                    
                    pay += emoticon * (100 - rate) // 100 
            
            # 매출액
            if pay >= price_limit: cnt += 1
            # 가입자 수
            else: sales += pay
            
        if cnt > answer[0] or (cnt == answer[0] and sales > answer[1]):
            answer = [cnt, sales]

    return answer