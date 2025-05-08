class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        import heapq

        n, m = len(moveTime), len(moveTime[0])
        
        INF = float('inf')
        dist = [[INF] * m for _ in range(n)]
        dist[0][0] = 0

        heap = [(0, 0, 0)]  # (시간, x, y)
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]

        while heap:
            t, x, y = heapq.heappop(heap)

            if t > dist[x][y]:  # 💥 누락되면 오답 가능
                continue

            if (x, y) == (n - 1, m - 1):
                return t

            for i, j in zip(dx, dy):
                nx, ny = x + i, y + j
                if 0 <= nx < n and 0 <= ny < m:
                    next_t = max(t, moveTime[nx][ny]) + 1
                    if next_t < dist[nx][ny]:
                        dist[nx][ny] = next_t
                        heapq.heappush(heap, (next_t, nx, ny))