import uuid
from dataclasses import dataclass, field

from domain.model.board import Board


def generate_game_id() -> str:
    return str(uuid.uuid4())


@dataclass
class CurrentGame:
    board: Board = field(default_factory=Board)
    game_id: str = field(default_factory=generate_game_id)
