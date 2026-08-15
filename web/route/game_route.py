from flask import Blueprint, request, jsonify, render_template

from web.model.current_game import WebCurrentGame
from web.mapper.current_game_mapper import to_domain, to_web

game_blueprint = Blueprint("game", __name__)


def register_game_route(service):

    @game_blueprint.route("/")
    def index():
        return render_template("index.html")

    @game_blueprint.route("/game/<uuid>", methods=["POST"])
    def make_move(uuid):

        data = request.get_json()

        web_game = WebCurrentGame.from_dict(data)
        web_game.uuid = uuid

        domain_game = to_domain(web_game)

        if not service.validate_board(domain_game):
            return jsonify({"error": "Board is invalid"}), 400

        if service.is_game_finished(domain_game):
            return jsonify({"error": "Game is already finished"}), 400

        updated_game = service.make_computer_move(domain_game)

        result = to_web(updated_game)

        return jsonify(result.to_dict())

    return game_blueprint
