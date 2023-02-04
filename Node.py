class Node:
    def __init__(self):
        self.position = (None, None)
        self.neighbours = [None, None, None, None]
        """
        [Up, Down, Left, Right]
        """

    def __str__(self):
        return str(self.position)

    def __repr__(self):
        return self.__str__()

    # def __eq__(self, other):
    #     return self.position[0] == other.position[0] or self.position[1] == other.position[1]
    #
    def __lt__(self, other):
        return self.position[0] < other.position[0] or self.position[1] < other.position[1]

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)
    #
    # def __gt__(self, other):
    #     return not self.__lt__(other) and not self.__eq__(other)
    #
    # def __ge__(self, other):
    #     return self.__gt__(other) or self.__eq__(other)

