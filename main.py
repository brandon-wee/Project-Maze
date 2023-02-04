import time
from PIL import Image
from Maze import Maze
from Algorithms import *
import sys

sys.setrecursionlimit(1000000000)


def flip(image):
    for j in range(image.size[1]):
        for i in range(image.size[0]):
            im.putpixel((i, j), not im.getpixel((i, j)))


def colour(im, start, end, new_colour, e, num):
    if start.position[0] == end.position[0]:
        for i in range(min(start.position[1], end.position[1]), max(start.position[1], end.position[1]) + 1):
            im.putpixel((start.position[0], i), tuple(new_colour))
            new_colour[0] = (e * 128) // num + 50
            # new_colour[1] = (e * 128) // num + 50
            # new_colour[2] = (e * 128) // num + 50
            e += 1
            # e -= 1
    else:
        for i in range(min(start.position[0], end.position[0]), max(start.position[0], end.position[0]) + 1):
            im.putpixel((i, start.position[1]), tuple(new_colour))
            new_colour[0] = (e * 128) // num + 50
            # new_colour[1] = (e * 128) // num + 50
            # new_colour[2] = (e * 128) // num + 50
            e += 1
            # e -= 1
    return e


def traversal(name):
    with Image.open(f"{name}.png") as im:

        # Creating maze
        print("Converting maze into graph...")
        setupStart = time.time()
        maze = Maze(im)
        maze.connect_maze()
        setupEnd = time.time()
        print(f"Creation time: {setupEnd - setupStart} seconds")
        # print(maze.nodes)
        print(f"Number of nodes: {len(maze.nodes)}")

        # Traversing maze
        trail = {}
        algo = input("\nEnter traversal algorithm (dfs, bfs, dijkstra, aStar): ")
        print("Traversing maze...")
        setupStart = time.time()

        # Traversal Algorithms
        # recur_ff(im, maze, maze.start, None, trail)
        if algo == "bfs":
            iter_bfs(maze, maze.start, trail)
        elif algo == "dfs":
            iter_dfs(maze, maze.start, trail)
        elif algo == "dijkstra":
            iter_dijkstra(maze, maze.start, trail)
        elif algo == "aStar":
            iter_aStar(maze, maze.start, trail)

        setupEnd = time.time()

        print(f"Traversal time: {setupEnd - setupStart} seconds")

        # Colouring maze
        print("\nColouring maze...")

        setupStart = time.time()
        num = 1
        current = trail[maze.end]
        while current != maze.start:
            if current.position[0] == trail[current].position[0]:
                num += abs(current.position[1] - trail[current].position[1])
            else:
                num += abs(current.position[0] - trail[current].position[0])

            current = trail[current]
        # print(trail)
        im.putpixel(maze.end.position, tuple(BLUE))
        current = trail[maze.end]
        e = 0

        while current != maze.start:
            # print(BLUE)
            e = colour(im, current, trail[current], BLUE, e, num)
            current = trail[current]

        im.putpixel(maze.start.position, tuple(BLUE))
        setupEnd = time.time()

        print(f"Colouring time: {setupEnd - setupStart} seconds")
        im.save(f"{name} {algo} traversal.png")


def visualize(name):
    BLUE = (0, 0, 255)
    with Image.open(f"{name}.png") as im:

        # Creating maze
        print("Converting maze into graph...")
        setupStart = time.time()
        maze = Maze(im)
        maze.connect_maze()
        setupEnd = time.time()
        print(f"Creation time: {setupEnd - setupStart} seconds")
        # print(maze.nodes)
        print(f"Number of nodes: {len(maze.nodes)}")

        trail = {}
        algo = input("\nEnter traversal algorithm (dfs, bfs, dijkstra, aStar): ")
        print("Traversing maze...")
        setupStart = time.time()

        # Traversal Algorithms
        # recur_ff(im, maze, maze.start, None, trail)
        if algo == "bfs":
            iter_bfs_colour(im, maze, maze.start, BLUE, trail)
        elif algo == "dfs":
            iter_dfs_colour(im, maze, maze.start, BLUE, trail)
        elif algo == "dijkstra":
            iter_dijkstra_colour(im, maze, maze.start, BLUE, trail)
        elif algo == "aStar":
            iter_aStar_colour(im, maze, maze.start, BLUE, trail)

        setupEnd = time.time()
        print(f"Traversal time: {setupEnd - setupStart} seconds")
        im.save(f"{name} {algo} visual3.png")


if __name__ == "__main__":
    WHITE = [255, 255, 255]
    GREEN = [0, 255, 0]
    BLUE = [0, 0, 255]
    new_colour = [0, 0, 0]
    name = input("Enter maze file name: ")
    mode = input("Traversal or Visualize algorithm: ")

    if mode == "Traversal":
        traversal(name)
    else:
        visualize(name)
