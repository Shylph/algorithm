# 유향 그래프 ->(오른쪽 방향)  무향은 대칭임
# a - b - d
#       - e - f
#             ^
#   - c - - - ^

# 인접 리스트
graph = {'A': {'B', 'C'},
         'B': {'A', 'D', 'E'},
         'C': {'A', 'F'},
         'D': {'B'},
         'E': {'B', 'F'},
         'F': {'C', 'E'}}


# Breadth-first-search, BFS
def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited


print(bfs(graph, 'A'))
# ['A', 'C', 'B', 'F', 'D', 'E']


# 경로 찾기
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    result = []

    while queue:
        n, path = queue.pop(0)
        if n == goal:
            result.append(path)
        else:
            for m in graph[n] - set(path):
                queue.append((m, path + [m]))
    return result


# 최단 경로는 bfs 의 첫번쨰
bfs_paths(graph, 'A', 'F')
# [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]
bfs_paths(graph, 'D', 'F')


# [['D', 'B', 'E', 'F'], ['D', 'B', 'A', 'C', 'F']]


# Depth-first-search
def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited


dfs(graph, 'A')
# ['A', 'B', 'E', 'F', 'C', 'D']


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    result = []

    while stack:
        n, path = stack.pop()
        if n == goal:
            result.append(path)
        else:
            for m in graph[n] - set(path):
                stack.append((m, path + [m]))
    return result

# !!!깊이 우선 탐색은 너비 우선 탐색과는 달리 최단 경로를 가장 먼저 찾지 못할 수도 있다.
dfs_paths(graph, 'A', 'F')
# [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]
dfs_paths(graph, 'D', 'F')
# [['D', 'B', 'A', 'C', 'F'], ['D', 'B', 'E', 'F']]


# 인접 행렬
graph2 = [  # A B C D E F
    [0, 1, 1, 0, 0, 0],  # A
    [1, 0, 0, 1, 1, 0],  # B
    [0, 1, 0, 0, 0, 0],  # C
    [0, 1, 0, 0, 0, 0],  # D
    [0, 1, 0, 0, 0, 1],  # E
    [0, 0, 1, 0, 1, 0],  # F
]
