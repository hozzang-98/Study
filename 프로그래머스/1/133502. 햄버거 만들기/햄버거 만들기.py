def solution(ingredient):

    answer = 0
    burger = []
    # 1: 빵, 2: 야채, 3: 고기
    for ing in ingredient:

        burger.append(ing)
        if burger[-4:] == [1,2,3,1]:

            answer += 1
            for i in range(4):
                burger.pop()
    
    return answer