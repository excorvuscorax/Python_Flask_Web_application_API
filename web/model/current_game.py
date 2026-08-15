from dataclasses import dataclass

from web.model.board import WebBoard


@dataclass
class WebCurrentGame:
    game_id: str
    board: WebBoard

    def to_dict(self) -> dict:
        return {"uuid": self.game_id, "board": self.board.to_dict()}

    @staticmethod
    def from_dict(data: dict) -> "WebCurrentGame":
        return WebCurrentGame(game_id="", board=WebBoard.from_dict(data["board"]))
