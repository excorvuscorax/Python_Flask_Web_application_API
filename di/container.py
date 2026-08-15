from datasource.mapper.current_game_mapper import CurrentGameMapper
from datasource.repository.game_repository import GameRepository
from datasource.storage import Storage

from domain.service.game_service_impl import GameServiceImpl


class Container:
    def __init__(self):
        self.storage = Storage()

        self.current_game_mapper = CurrentGameMapper()

        self.game_repository = GameRepository(
            self.storage,
            self.current_game_mapper,
        )

        self.game_service = GameServiceImpl(self.game_repository)
