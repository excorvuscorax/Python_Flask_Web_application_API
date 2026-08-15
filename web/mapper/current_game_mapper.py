from domain.model.board import Board
from domain.model.current_game import CurrentGame

from web.model.board import WebBoard
from web.model.current_game import WebCurrentGame

BOARD_SIZE = 3


def _flat_to_matrix(cells: list[int]) -> list[list[int]]:
    return [cells[i : i + BOARD_SIZE] for i in range(0, len(cells), BOARD_SIZE)]


def _matrix_to_flat(matrix: list[list[int]]) -> list[int]:
    return [cell for row in matrix for cell in row]


def to_domain(web_game: WebCurrentGame) -> CurrentGame:
    domain_board = Board(cells=_flat_to_matrix(web_game.board.cells))

    return CurrentGame(game_id=web_game.game_id, board=domain_board)


def to_web(domain_game: CurrentGame) -> WebCurrentGame:
    web_board = WebBoard(cells=_matrix_to_flat(domain_game.board.cells))

    return WebCurrentGame(game_id=domain_game.game_id, board=web_board)
