from pathlib import Path
from src.game_env.node import Node
from collections import defaultdict
from enum import Enum


class Player(Enum):
    orange = "orange"
    white = "white"

    def __str__(self) -> str:
        return self.value


class Phase(Enum):
    placing = "placing"
    moving = "moving"
    capturing = "capturing"

    def __str__(self) -> str:
        return self.value


class Action(Enum):
    move = "move"
    remove = "remove"
    undo = "undo"

    def __str__(self) -> str:
        return self.value


ICONS = {
    Player.orange: Path("assets/orangeplayer.png"),
    Player.white: Path("assets/whiteplayer.png"),
}
INITIAL_POSITIONS = {Player.orange: "h2", Player.white: "h4"}
CELL_SIZE = 80
MARGIN = 50
MIN_DRAW_MOVES = 50
NODES = [
    Node("a0"),
    Node("d0"),
    Node("g0"),
    Node("b1"),
    Node("d1"),
    Node("f1"),
    Node("c2"),
    Node("d2"),
    Node("e2"),
    Node("a3"),
    Node("b3"),
    Node("c3"),
    Node("e3"),
    Node("f3"),
    Node("g3"),
    Node("c4"),
    Node("d4"),
    Node("e4"),
    Node("b5"),
    Node("d5"),
    Node("f5"),
    Node("a6"),
    Node("d6"),
    Node("g6"),
]
EDGES: list[tuple[Node, Node]] = [
    # Horizontal edges
    (Node("a0"), Node("d0")),
    (Node("d0"), Node("g0")),
    (Node("b1"), Node("d1")),
    (Node("d1"), Node("f1")),
    (Node("c2"), Node("d2")),
    (Node("d2"), Node("e2")),
    (Node("a3"), Node("b3")),
    (Node("b3"), Node("c3")),
    (Node("e3"), Node("f3")),
    (Node("f3"), Node("g3")),
    (Node("c4"), Node("d4")),
    (Node("d4"), Node("e4")),
    (Node("b5"), Node("d5")),
    (Node("d5"), Node("f5")),
    (Node("a6"), Node("d6")),
    (Node("d6"), Node("g6")),
    # Vertical edges
    (Node("a0"), Node("a3")),
    (Node("a3"), Node("a6")),
    (Node("b1"), Node("b3")),
    (Node("b3"), Node("b5")),
    (Node("c2"), Node("c3")),
    (Node("c3"), Node("c4")),
    (Node("d0"), Node("d1")),
    (Node("d1"), Node("d2")),
    (Node("d4"), Node("d5")),
    (Node("d5"), Node("d6")),
    (Node("e2"), Node("e3")),
    (Node("e3"), Node("e4")),
    (Node("f1"), Node("f3")),
    (Node("f3"), Node("f5")),
    (Node("g0"), Node("g3")),
    (Node("g3"), Node("g6")),
]


# Create a lookup table
NODE_LOOKUP = defaultdict(list[Node])
for edge in EDGES:
    NODE_LOOKUP[edge[0]].append(edge[1])
    NODE_LOOKUP[edge[1]].append(edge[0])

TRAINING_PARAMETERS = dict(
    # Global variables
    RENDER=True,
    INTERACTABLES=[],
    DIFFICULTY={
        Player.orange: 5,
        Player.white: 5,
    },
    STUPIDITY=0.0,
    MAX_N_OPERATIONS=None,
    N_PROCESS=-1,
)

EVALUATION_COEFFICIENTS = {
    "placing": {
        "sparsity": 0.1,
        "n_pieces": 0.2,
        "n_mills": 1.0,
        "entropy": 0.1,
    },
    "moving": {
        "sparsity": 0.0,
        "n_pieces": 1.0,
        "n_mills": 0.8,
        "entropy": 0.3,
    },
    "flying": {
        "sparsity": 0.0,
        "n_pieces": 1.0,
        "n_mills": 1.0,
        "entropy": 0.1,
    },
}


N_REPITITIONS = 1
