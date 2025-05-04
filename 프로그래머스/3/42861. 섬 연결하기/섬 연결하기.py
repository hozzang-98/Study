import heapq

def solution(n, costs):

    answer = 0 
    graph = {i:[] for i in range(n)}
    
    for i1, i2, cost in costs:

        graph[i1].append((cost, i2))
        graph[i2].append((cost, i1))

    heap = [(0,0)]

    visited = set()
   
    while len(visited) < n:

        cost, island = heapq.heappop(heap) # 최소비용

        if island in visited:

            continue

        visited.add(island)
        answer += cost

        for cost, new_island in graph[island]:

            if new_island not in visited:

                heapq.heappush(heap, (cost, new_island))

    return answer