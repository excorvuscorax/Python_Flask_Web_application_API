from abc import ABC, abstractmethod

from domain.model.current_game import CurrentGame


class GameService(ABC):

    @abstractmethod
    def make_computer_move(self, current_game: CurrentGame) -> CurrentGame:
        """Выполняет следующий ход компьютера."""
        pass

    @abstractmethod
    def validate_board(self, current_game: CurrentGame) -> bool:
        """Проверяет корректность игрового поля."""
        pass

    @abstractmethod
    def is_game_finished(self, current_game: CurrentGame) -> bool:
        """Проверяет, завершена ли игра."""
        pass
