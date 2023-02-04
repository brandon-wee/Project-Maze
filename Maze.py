from Node import Node


class Maze:

    def __init__(self, im):
        self.image = im
        self.start = Node()
        self.end = Node()
        self.nodes = []
        self.node_locations = {}

    def get_start(self):
        for i in range(self.image.size[0]):
            if self.image.getpixel((i, 0)) == 1:
                self.create_node((i, 0))
                self.start = self.node_locations[(i, 0)]
                return None

    def get_end(self):
        for i in range(self.image.size[0]):
            if self.image.getpixel((i, self.image.size[1] - 1)) == 1:
                self.create_node((i, self.image.size[1] - 1))
                self.end = self.node_locations[(i, self.image.size[1] - 1)]
                return None

    def connect_left(self, s, e):
        s.neighbours[2] = e
        e.neighbours[3] = s

    def connect_up(self, s, e):  # When called, connects s to e, s is directly below e
        s.neighbours[0] = e
        e.neighbours[1] = s

    def create_node(self, pos):
        current_node = Node()
        current_node.position = pos
        self.nodes.append(current_node)
        self.node_locations[pos] = current_node
        self.node_locations[pos] = current_node
        for i in range(pos[1] - 1, -1, -1):
            if self.image.getpixel((pos[0], i)) == 0:
                break

            if (pos[0], i) in self.node_locations:
                self.connect_up(current_node, self.node_locations[(pos[0], i)])
                break

        for i in range(pos[0] - 1, -1, -1):
            if self.image.getpixel((i, pos[1])) == 0:
                break

            if (i, pos[1]) in self.node_locations:
                self.connect_left(current_node, self.node_locations[(i, pos[1])])
                break

    def connect_maze(self):
        self.get_start()
        for j in range(1, self.image.size[1] - 1):
            for i in range(1, self.image.size[0] - 1):
                # Write code here...
                now = (i, j)
                if self.image.getpixel(now) != 0:
                    up = down = left = right = False
                    white = 0
                    if self.image.getpixel((now[0], now[1] + 1)) == 1:
                        down = True
                        white += 1

                    if self.image.getpixel((now[0] + 1, now[1])) == 1:
                        right = True
                        white += 1

                    if self.image.getpixel((now[0], now[1] - 1)) == 1:
                        up = True
                        white += 1

                    if self.image.getpixel((now[0] - 1, now[1])) == 1:
                        left = True
                        white += 1

                    if white >= 3 or (white == 2 and not ((left and right) or (up and down))) or white == 1:
                        self.create_node(now)

        self.get_end()
