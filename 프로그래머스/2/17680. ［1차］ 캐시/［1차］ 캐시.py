
def solution(cachesize, cities):

    from collections import deque

    dq = deque(maxlen=cachesize)
    answer = 0
    cities = [city.lower() for city in cities]

    for city in cities:

        if city in dq:
            
            dq.remove(city) 
            dq.append(city)
            answer += 1

        else:

            answer += 5
            dq.append(city)

    return answer