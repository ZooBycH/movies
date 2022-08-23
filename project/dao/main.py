from typing import Optional, List

from flask_sqlalchemy import BaseQuery
from sqlalchemy import desc
from werkzeug.exceptions import NotFound

from project.dao.base import BaseDAO, T
from project.models import Genre, Movie, Director, User, FavoritesMovie


class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre


class DirectorsDAO(BaseDAO[Director]):
    __model__ = Director


class MoviesDAO(BaseDAO[Movie]):
    __model__ = Movie

    def get_all_order_by(self, filter: Optional[str] = None, page: Optional[int] = None) -> List[T]:
        stmt: BaseQuery = self._db_session.query(self.__model__)

        if filter == 'new':
            stmt = stmt.order_by(desc(self.__model__.year))
        else:
            stmt = stmt.order_by(self.__model__.year)
        if page:
            try:
                return stmt.paginate(page, self._items_per_page).items
            except NotFound:
                return []
        return stmt.all()


class UsersDAO(BaseDAO[User]):
    __model__ = User

    def create_user(self, email, password):
        user = User(
            email=email,
            password=password
        )
        try:
            self._db_session.add(
                user
            )
            self._db_session.commit()
            print("Пользователь создан")
            return user
        except Exception as e:
            self._db_session.rollback()
            print(e)

    def get_user_by_email(self, email):
        return self._db_session.query(self.__model__).filter(self.__model__.email == email).one()

    def update_user(self, data, email):
        try:
            self._db_session.query(self.__model__).filter(self.__model__.email == email).update(data)
            self._db_session.commit()
            print("Пользователь успешно обновлен")
        except Exception as e:
            print(f"Ошибка обновления {e}")
            self._db_session.rollback()


class FavoritesDAO(BaseDAO[FavoritesMovie]):
    __model__ = FavoritesMovie

    def get_favorite_user_all(self, user_id, page: Optional[int] = None):
        stmt: BaseQuery = self._db_session.query(self.__model__)
        stmt = stmt.filter(FavoritesMovie.user_id == user_id)
        if page:
            try:
                return stmt.paginate(page, self._items_per_page).items
            except NotFound:
                return []
        return stmt.all()

    def add_favorite(self, user_id, movie_id):
        favorite = FavoritesMovie(
            user_id=user_id,
            movie_id=movie_id
        )
        try:
            self._db_session.add(favorite)
            self._db_session.commit()
            print("Запись создана")
            return favorite
        except Exception as e:
            print(e)
            self._db_session.rollback()

    def delete_favorite(self, user_id, movie_id):
        stmt: BaseQuery = self._db_session.query(self.__model__)
        stmt = stmt.filter(FavoritesMovie.user_id == user_id, FavoritesMovie.movie_id == movie_id)
        favorite = stmt.one()
        self._db_session.delete(favorite)
        self._db_session.commit()




