def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    camera = [routes[0][1]]

    for s,e in routes:
        if s <= camera[-1]:
            continue
        else:
            camera.append(e)
        
    answer += len(camera)

    return answer

solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])