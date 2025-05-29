class Solution:
    
    def minTimeToReach(self, moveTime: list[list[int]]) -> int:
        
        import heapq

        n, m = len(moveTime), len(moveTime[0])

        INF = float('inf')

        dist = [[[INF] * 2 for _ in range(m)] for _ in range(n)]
        dist[0][0][0] = 0

        direction = [(-1,0), (1,0), (0,1), (0,-1)]
        heap = [(0,0,0,0)]

        while heap:

            t, x, y, is_even = heapq.heappop(heap)

            if (x, y) == (n-1, m-1): return t
            
            for dx, dy in direction:

                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < m:

                    cost = 1 if is_even == 0 else 2
                    new_t = max(t, moveTime[nx][ny]) + cost
                    next_even = 1 - is_even
                    
                    if new_t < dist[nx][ny][next_even]:

                        dist[nx][ny][next_even] = new_t
                        heapq.heappush(heap, (new_t, nx, ny, next_even)) 