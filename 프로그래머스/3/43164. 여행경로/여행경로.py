def solution(tickets):
    from collections import deque, defaultdict
    # 그래프를 딕셔너리로 초기화
    graph = defaultdict(list)
    for start, end in tickets:
        graph[start].append(end)
    
    # 각 출발지에서 도착지를 알파벳 순으로 정렬
    for key in graph:
        graph[key].sort(reverse=True)
    
    # BFS를 사용해 경로를 찾기
    stack = ["ICN"]
    path = []

    while stack:
        current = stack[-1]

        # 더 갈 수 있는 경로가 없으면 경로에 추가
        if not graph[current]:
            path.append(stack.pop())
        else:
            # 방문할 수 있는 경로가 있으면, 그 경로로 이동
            stack.append(graph[current].pop())
    
    # 경로를 뒤집어 반환 (DFS와 달리 거꾸로 쌓이기 때문)
    return path[::-1]