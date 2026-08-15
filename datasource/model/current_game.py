from dataclasses import dataclass, field

from datasource.model.board import Board


@dataclass
class CurrentGame:
    board: Board = field(default_factory=Board)
    game_id: str = ""
