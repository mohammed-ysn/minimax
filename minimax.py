from typing import Optional


class Node:
    def __init__(self, utility: Optional[float] = None) -> None:
        self.utility = utility
        self.children: list[Node] = []

    def add_child(self, child: Optional["Node"] = None) -> "Node":
        if child is None:
            child = Node()
        self.children.append(child)
        return child

    def generate_children(self) -> list["Node"]:
        return self.children

    def is_terminal(self) -> bool:
        return self.utility is not None

    def evaluate(self) -> float:
        assert self.utility is not None
        return self.utility

    def __str__(self, level=0):
        ret = "----" * level + f"Node(utility={self.utility})\n"
        if self.children:
            for child in self.children:
                ret += child.__str__(level + 1)
        return ret


def minimax(node: Node, depth: int, maximisingPlayer: bool, alpha, beta) -> float:
    if depth == 0 or node.is_terminal():
        return node.evaluate()

    if maximisingPlayer:
        value = -float("inf")
        for child in node.generate_children():
            child_value = minimax(child, depth - 1, False, alpha, beta)
            if child_value > value:
                value = child_value
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        node.utility = value
        return value
    else:
        value = float("inf")
        for child in node.generate_children():
            child_value = minimax(child, depth - 1, True, alpha, beta)
            if child_value < value:
                value = child_value
            beta = min(beta, value)
            if alpha >= beta:
                break
        node.utility = value
        return value


# construct tree
leaf_utils = [
    1,
    -15,
    2,
    19,
    18,
    23,
    4,
    3,
    2,
    1,
    7,
    8,
    9,
    10,
    -2,
    5,
    -1,
    -30,
    4,
    7,
    20,
    -1,
    -1,
    -5,
]

root = Node()
i = 0
for _ in range(3):
    n1 = root.add_child()
    for _ in range(2):
        n2 = n1.add_child()
        for _ in range(2):
            n3 = n2.add_child()
            for _ in range(2):
                n4 = n3.add_child(Node(leaf_utils[i]))
                i += 1

# max starts the game
minimax(root, depth=4, maximisingPlayer=True, alpha=-float("inf"), beta=float("inf"))

# min starts the game
# minimax(root, depth=4, maximisingPlayer=False, alpha=-float("inf"), beta=float("inf"))

print(root)
