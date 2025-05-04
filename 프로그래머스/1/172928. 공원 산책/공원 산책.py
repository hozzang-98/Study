def solution(park, routes):
    h, w = len(park), len(park[0])
    directions = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}

    # 시작 위치 찾기
    for i in range(h):
        for j in range(w):
            if park[i][j] == 'S':
                x, y = i, j

    for route in routes:
        dir, step = route.split()
        dx, dy = directions[dir]
        step = int(step)

        nx, ny = x, y
        valid = True
        for i in range(1, step + 1):
            tx = x + dx * i
            ty = y + dy * i
            if not (0 <= tx < h and 0 <= ty < w) or park[tx][ty] == 'X':
                valid = False
                break

        if valid:
            x += dx * step
            y += dy * step

    return [x, y]