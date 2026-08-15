from flask import Flask

from di.container import Container
from web.route.game_route import register_game_route

container = Container()

app = Flask(__name__, template_folder="web/templates")

app.register_blueprint(register_game_route(container.game_service))


if __name__ == "__main__":
    app.run(debug=True)
