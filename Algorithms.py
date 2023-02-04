import collections
import heapq

def recur_ff(im, maze, xy, f=None, visited=None):
    if visited is None:
        visited = {}

    if xy not in visited:
        visited[xy] = f
        # print(visited)
        if xy == maze.end:
            return visited

        for neighbour in xy.neighbours:
            if neighbour is not None and neighbour not in visited and maze.end not in visited:
                recur_ff(im, maze, neighbour, xy, visited)

    return visited


def iter_bfs(maze, xy, visited=None):
    queue = collections.deque([(xy, None)])
    while queue:
        now = queue.popleft()
        visited[now[0]] = now[1]
        f = now[0]
        if maze.end in visited:
            return visited

        for neighbour in f.neighbours:
            if neighbour is not None and neighbour not in visited and maze.end not in visited:
                if neighbour == maze.end:
                    visited[neighbour] = f
                    return visited
                queue.append((neighbour, f))


def iter_dfs(maze, xy, visited=None):
    stack = [(xy, None)]
    while stack:
        # print(len(queue))
        now = stack.pop()
        visited[now[0]] = now[1]
        f = now[0]
        if maze.end in visited:
            return visited

        for neighbour in f.neighbours:
            if neighbour is not None and neighbour not in visited and maze.end not in visited:
                stack.append((neighbour, f))



def iter_dijkstra(maze, xy, visited = None):
    priority_queue = []
    heapq.heappush(priority_queue, (0, xy, None))

    nodeCosts = collections.defaultdict(lambda: float('inf'))
    nodeCosts[xy] = 0

    while priority_queue:
        # print(1, priority_queue, visited, dict(nodeCosts))
        now = heapq.heappop(priority_queue)
        visited[now[1]] = now[2]
        f = now[1]
        if maze.end == f:
            return visited

        # print(2, priority_queue, visited, dict(nodeCosts))
        for index, neighbour in enumerate(f.neighbours):
            if neighbour is not None and neighbour not in visited and maze.end not in visited:
                if 0 <= index <= 1:
                    newCost = nodeCosts[f] + abs(neighbour.position[1] - f.position[1])
                    if newCost < nodeCosts[neighbour]:
                        nodeCosts[neighbour] = newCost
                        heapq.heappush(priority_queue, (newCost, neighbour, f))
                else:
                    newCost = nodeCosts[f] + abs(neighbour.position[0] - f.position[0])
                    if newCost < nodeCosts[neighbour]:
                        nodeCosts[neighbour] = newCost
                        heapq.heappush(priority_queue, (newCost, neighbour, f))

                # print(neighbour, newCost)

def iter_aStar(maze, xy, visited = None):
    priority_queue = []
    heapq.heappush(priority_queue, (0, xy, None))

    nodeCosts = collections.defaultdict(lambda: float('inf'))
    nodeCosts[xy] = 0

    while priority_queue:
        # print(1, priority_queue, visited, dict(nodeCosts))
        now = heapq.heappop(priority_queue)
        visited[now[1]] = now[2]
        f = now[1]
        if maze.end == f:
            return visited

        # print(2, priority_queue, visited, dict(nodeCosts))
        for index, neighbour in enumerate(f.neighbours):
            if neighbour is not None and neighbour not in visited and maze.end not in visited:
                heuristic = int(((neighbour.position[0] - maze.end.position[0]) ** 2 + (neighbour.position[1] - maze.end.position[1]) ** 2) ** 1/2)
                if 0 <= index <= 1:
                    newCost = nodeCosts[f] + abs(neighbour.position[1] - f.position[1]) + heuristic
                    if newCost < nodeCosts[neighbour]:
                        nodeCosts[neighbour] = newCost
                        heapq.heappush(priority_queue, (newCost, neighbour, f))
                else:
                    newCost = nodeCosts[f] + abs(neighbour.position[0] - f.position[0]) + heuristic
                    if newCost < nodeCosts[neighbour]:
                        nodeCosts[neighbour] = newCost
                        heapq.heappush(priority_queue, (newCost, neighbour, f))


# Colouring algorithms to visualize nodes that are being expanded on

def iter_bfs_colour(im, maze, xy, colour = (0, 0, 255), visited=None):
    queue = collections.deque([(xy, None)])
    while queue:
        now = queue.popleft()
        visited[now[0]] = now[1]
        f = now[0]
        im.putpixel(f.position, colour)
        if maze.end in visited:
            return visited

        for neighbour in f.neighbours:
            if neighbour is not None and neighbour not in visited and maze.end not in visited:
                if neighbour == maze.end:
                    visited[neighbour] = f
                    return visited
                queue.append((neighbour, f))


def iter_dfs_colour(im, maze, xy, colour = (0, 0, 255), visited=None):
    stack = [(xy, None)]
    while stack:
        # print(len(queue))
        now = stack.pop()
        visited[now[0]] = now[1]
        f = now[0]
        im.putpixel(f.position, colour)
        if maze.end in visited:
            return visited

        for neighbour in f.neighbours:
            if neighbour is not None and neighbour not in visited and maze.end not in visited:
                stack.append((neighbour, f))



def iter_dijkstra_colour(im, maze, xy, colour = (0, 0, 255), visited = None):
    priority_queue = []
    heapq.heappush(priority_queue, (0, xy, None))

    nodeCosts = collections.defaultdict(lambda: float('inf'))
    nodeCosts[xy] = 0

    while priority_queue:
        # print(1, priority_queue, visited, dict(nodeCosts))
        now = heapq.heappop(priority_queue)
        visited[now[1]] = now[2]
        f = now[1]
        if maze.end == f:
            return visited

        im.putpixel(f.position, colour)
        # print(2, priority_queue, visited, dict(nodeCosts))
        for index, neighbour in enumerate(f.neighbours):
            if neighbour is not None and neighbour not in visited and maze.end not in visited:
                if 0 <= index <= 1:
                    newCost = nodeCosts[f] + abs(neighbour.position[1] - f.position[1])
                    if newCost < nodeCosts[neighbour]:
                        nodeCosts[neighbour] = newCost
                        heapq.heappush(priority_queue, (newCost, neighbour, f))
                else:
                    newCost = nodeCosts[f] + abs(neighbour.position[0] - f.position[0])
                    if newCost < nodeCosts[neighbour]:
                        nodeCosts[neighbour] = newCost
                        heapq.heappush(priority_queue, (newCost, neighbour, f))

                # print(neighbour, newCost)

def iter_aStar_colour(im, maze, xy, colour = (0, 0, 255), visited = None):
    priority_queue = []
    heapq.heappush(priority_queue, (0, xy, None))

    nodeCosts = collections.defaultdict(lambda: float('inf'))
    nodeCosts[xy] = 0

    while priority_queue:
        # print(1, priority_queue, visited, dict(nodeCosts))
        now = heapq.heappop(priority_queue)
        visited[now[1]] = now[2]
        f = now[1]
        if maze.end == f:
            return visited

        im.putpixel(f.position, colour)
        # print(2, priority_queue, visited, dict(nodeCosts))
        for index, neighbour in enumerate(f.neighbours):
            if neighbour is not None and neighbour not in visited and maze.end not in visited:
                heuristic = int(((neighbour.position[0] - maze.end.position[0]) ** 2 + (neighbour.position[1] - maze.end.position[1]) ** 2) ** 1/2)
                if 0 <= index <= 1:
                    newCost = nodeCosts[f] + abs(neighbour.position[1] - f.position[1]) + heuristic
                    if newCost < nodeCosts[neighbour]:
                        nodeCosts[neighbour] = newCost
                        heapq.heappush(priority_queue, (newCost, neighbour, f))
                else:
                    newCost = nodeCosts[f] + abs(neighbour.position[0] - f.position[0]) + heuristic
                    if newCost < nodeCosts[neighbour]:
                        nodeCosts[neighbour] = newCost
                        heapq.heappush(priority_queue, (newCost, neighbour, f))