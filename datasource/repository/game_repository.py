from datasource.storage import Storage
from datasource.mapper.current_game_mapper import CurrentGameMapper
from domain.model.current_game import CurrentGame as DomainCurrentGame


class GameRepository:
    def __init__(self, storage: Storage, mapper: CurrentGameMapper):
        self._storage = storage
        self._mapper = mapper

    def save(self, domain_game: DomainCurrentGame) -> None:
        """
        Сохраняет текущую игру в хранилище.
        Доменная модель преобразуется в модель источника данных.
        """
        datasource_game = self._mapper.to_datasource(domain_game)

        self._storage.save(
            datasource_game.game_id,
            {
                "game_id": datasource_game.game_id,
                "board": {"cells": datasource_game.board.cells},
            },
        )

    def get(self, game_id: str) -> DomainCurrentGame | None:
        """
        Получает игру из хранилища и преобразует
        её обратно в доменную модель.
        """
        data = self._storage.get(game_id)

        if data is None:
            return None

        datasource_game = self._mapper.from_dict(data)

        return self._mapper.to_domain(datasource_game)
