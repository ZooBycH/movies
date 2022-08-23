from flask import request
from flask_restx import Namespace, Resource

from project.container import favorite_service, user_service
from project.setup.api.models import favorite

api = Namespace('favorites')


@api.route('/movies/')
class FavoriteView(Resource):
    @api.marshal_with(favorite, as_list=True, code=200, description='OK')
    def get(self):
        token = request.headers["Authorization"].split("Bearer ")[-1]
        user = user_service.get_user_by_token(token)
        return favorite_service.get_favorite_all_by_user(user.id)


@api.route('/movies/<int:movie_id>')
class FavoritesView(Resource):
    @api.marshal_with(favorite, as_list=True, code=200, description='OK')
    def post(self, movie_id):
        token = request.headers["Authorization"].split("Bearer ")[-1]
        user = user_service.get_user_by_token(token)
        return favorite_service.add_favorite(user.id, movie_id), 201

    def delete(self, movie_id):
        token = request.headers["Authorization"].split("Bearer ")[-1]
        user = user_service.get_user_by_token(token)
        favorite_service.delete_favorite(user.id, movie_id)
        return "Ok", 204
