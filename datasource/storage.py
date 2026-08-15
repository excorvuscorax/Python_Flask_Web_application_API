import copy
import threading


class Storage:

    def __init__(self):
        self._games = {}
        self._lock = threading.Lock()

    def save(self, game_id: str, game_data: dict) -> None:
        with self._lock:
            self._games[game_id] = copy.deepcopy(game_data)

    def get(self, game_id: str) -> dict | None:
        with self._lock:
            game = self._games.get(game_id)

            if game is None:
                return None

            return copy.deepcopy(game)
