from domain.model.board import Board
from domain.model.current_game import CurrentGame
from domain.repository.game_repository import GameRepository
from domain.service.game_service import GameService

EMPTY = 0
HUMAN = 1
COMPUTER = 2

BOARD_SIZE = 3


class GameServiceImpl(GameService):

    def __init__(self, repository: GameRepository):
        self._repository = repository

    def make_computer_move(self, current_game: CurrentGame) -> CurrentGame:

        board = current_game.board

        best_score = float("-inf")
        best_move = None

        for row in range(BOARD_SIZE):
            for column in range(BOARD_SIZE):

                if board.cells[row][column] == EMPTY:

                    board.cells[row][column] = COMPUTER

                    score = self._minimax(board, False)

                    board.cells[row][column] = EMPTY

                    if score > best_score:
                        best_score = score
                        best_move = (row, column)

        if best_move:

            row, column = best_move
            board.cells[row][column] = COMPUTER

            self._repository.save(current_game)

        return current_game

    def _minimax(self, board: Board, computer_turn: bool) -> int:

        winner = self._check_winner(board)

        if winner == COMPUTER:
            return 1

        if winner == HUMAN:
            return -1

        if self._is_board_full(board):
            return 0

        if computer_turn:

            best_score = float("-inf")

            for row in range(BOARD_SIZE):
                for column in range(BOARD_SIZE):

                    if board.cells[row][column] == EMPTY:

                        board.cells[row][column] = COMPUTER

                        best_score = max(best_score, self._minimax(board, False))

                        board.cells[row][column] = EMPTY

            return best_score

        best_score = float("inf")

        for row in range(BOARD_SIZE):
            for column in range(BOARD_SIZE):

                if board.cells[row][column] == EMPTY:

                    board.cells[row][column] = HUMAN

                    best_score = min(best_score, self._minimax(board, True))

                    board.cells[row][column] = EMPTY

        return best_score

    def validate_board(self, current_game: CurrentGame) -> bool:

        cells = [cell for row in current_game.board.cells for cell in row]

        if any(cell not in (EMPTY, HUMAN, COMPUTER) for cell in cells):
            return False

        human_moves = cells.count(HUMAN)
        computer_moves = cells.count(COMPUTER)

        if human_moves - computer_moves not in (0, 1):
            return False

        return True

    def is_game_finished(self, current_game: CurrentGame) -> bool:

        return self._check_winner(
            current_game.board
        ) is not None or self._is_board_full(current_game.board)

    def _check_winner(self, board: Board):

        for line in self._get_winning_lines(board):

            if line[0] != EMPTY and len(set(line)) == 1:
                return line[0]

        return None

    def _get_winning_lines(self, board: Board):

        cells = board.cells

        lines = []

        lines.extend(cells)

        lines.extend(
            [
                [cells[row][column] for row in range(BOARD_SIZE)]
                for column in range(BOARD_SIZE)
            ]
        )

        lines.append([cells[i][i] for i in range(BOARD_SIZE)])

        lines.append([cells[i][BOARD_SIZE - i - 1] for i in range(BOARD_SIZE)])

        return lines

    def _is_board_full(self, board: Board) -> bool:

        return all(cell != EMPTY for row in board.cells for cell in row)
