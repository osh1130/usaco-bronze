from collections import deque

def bfs(start):
    queue = deque()
    visited = set()

    queue.append((start, 1))  # 节点 + 当前“爆炸半径”或“步数”
    visited.add(start)

    while queue:
        node, radius = queue.popleft()

        # 拓展所有下一层能走的节点（题目决定规则）
        for neighbor in get_neighbors(node, radius):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, radius + 1))

    return visited

from collections import deque

def bfs(start, bales):
    visited = set()
    queue = deque()
    queue.append((start, 1))
    visited.add(start)

    while queue:
        pos, radius = queue.popleft()

        # 向左
        i = bales.index(pos) - 1
        while i >= 0 and bales[i] >= pos - radius:
            if bales[i] not in visited:
                visited.add(bales[i])
                queue.append((bales[i], radius + 1))
            i -= 1

        # 向右
        i = bales.index(pos) + 1
        while i < len(bales) and bales[i] <= pos + radius:
            if bales[i] not in visited:
                visited.add(bales[i])
                queue.append((bales[i], radius + 1))
            i += 1

    return len(visited)
