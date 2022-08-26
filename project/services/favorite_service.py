from typing import Optional

from project.dao import FavoritesDAO


class FavoriteService:
    def __init__(self, dao: FavoritesDAO) -> None:
        self.dao = dao

    def get_favorite_all_by_user(self, user_id, page: Optional[int] = None):
        return self.dao.get_favorite_user_all(user_id=user_id, page=page)

    def add_favorite(self, user_id, movie_id):
        return self.dao.add_favorite(user_id=user_id, movie_id=movie_id)

    def delete_favorite(self, user_id, movie_id):
        return self.dao.delete_favorite(user_id=user_id, movie_id=movie_id)


