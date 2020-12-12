from typing import List, Tuple
from week06.node import Node
import heapq


class Tree:

    def __init__(self, frequencies: List[Tuple[chr, int]]):

        nodes = Tree.__transform_to_nodes(frequencies=frequencies)

        heapq.heapify(nodes)

        self.root = Tree.__reduce_to_tree(nodes)
        self.__dict = dict()

        self.walk_and_translate(self.root)

    @staticmethod
    def __transform_to_nodes(frequencies: List[Tuple[chr, int]]) -> List[Node]:
        nodes = []

        for (char, freq) in frequencies:
            node = Node(data=char, frequency=freq)
            nodes.append(node)

        return nodes

    @staticmethod
    def __reduce_to_tree(nodes):
        while len(nodes) > 1:

            left_child = heapq.heappop(nodes)
            right_child = heapq.heappop(nodes)

            node = Node.from_children(left=left_child, right=right_child)
            heapq.heappush(nodes, node)

        return nodes[0]

    def walk_and_translate(self, node: Node, path=''):

        if node.is_leaf():
            self.__dict[node.data] = path
            return
        else:
            self.walk_and_translate(node.left, path=path + '0')
            self.walk_and_translate(node.right, path=path + '1')

    def get_translated(self):
        return self.__dict