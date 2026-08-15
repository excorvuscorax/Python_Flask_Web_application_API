from datasource.model.board import Board as DatasourceBoard
from datasource.model.current_game import CurrentGame as DatasourceCurrentGame

from domain.model.board import Board as DomainBoard
from domain.model.current_game import CurrentGame as DomainCurrentGame


class CurrentGameMapper:

    def to_datasource(self, domain_game: DomainCurrentGame) -> DatasourceCurrentGame:

        board = DatasourceBoard(cells=[row.copy() for row in domain_game.board.cells])

        return DatasourceCurrentGame(board=board, game_id=domain_game.game_id)

    def to_domain(self, datasource_game: DatasourceCurrentGame) -> DomainCurrentGame:

        board = DomainBoard(cells=[row.copy() for row in datasource_game.board.cells])

        return DomainCurrentGame(board=board, game_id=datasource_game.game_id)
