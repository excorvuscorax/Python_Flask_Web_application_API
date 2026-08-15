from dataclasses import dataclass, field

BOARD_SIZE = 3
EMPTY = 0


@dataclass
class Board:
    cells: list[list[int]] = field(
        default_factory=lambda: [
            [EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)
        ]
    )
