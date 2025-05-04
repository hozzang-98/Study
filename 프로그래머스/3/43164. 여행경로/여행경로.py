def solution(tickets):

    from collections import defaultdict

    airport_graph = defaultdict(list)

    for start, end in tickets:

        airport_graph[start].append(end)

    answer = []

    # 후입 선출
    stack = ['ICN']

    for key in airport_graph.keys():

        airport_graph[key].sort(reverse=True)

    while stack:

        node = stack.pop()

        if airport_graph[node]:

            stack.append(node)
            stack.append(airport_graph[node].pop())

        else:
            
            answer.append(node)


    return answer[::-1]