class Node:
    def __init__(self, frequency, data=None, left=None, right=None):
        self.frequency = frequency
        self.data = data
        self.left = left
        self.right = right

    @classmethod
    def from_children(cls, left, right):
        freq = left.frequency + right.frequency
        return cls(frequency=freq, left=left, right=right)

    def is_leaf(self):
        return self.data is not None

    def __repr__(self):
        return f"({self.data}:{self.frequency})"

    def __lt__(self, other):
        return self.frequency < other.frequency
