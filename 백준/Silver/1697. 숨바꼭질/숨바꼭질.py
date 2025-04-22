from collections import deque

n, k = map(int, input().split())

max_num = 100000

visited = [0] * (max_num + 1)

def bfs():

    q = deque()
    q.append(n)

    while q:

        x = q.popleft()

        if x == k:
            
            print(visited[x])
            break

        for way in (x-1, x+1, x*2):

            if 0 <= way <= max_num and not visited[way]:

                visited[way] = visited[x] + 1

                q.append(way)

bfs()