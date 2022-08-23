from sqlalchemy import Column, String, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from project.setup.db import models, db


class Genre(models.Base):
    __tablename__ = 'genres'

    name = Column(String(100), unique=True, nullable=False)


class Director(models.Base):
    __tablename__ = 'directors'

    name = Column(String(100), unique=True, nullable=False)


class Movie(models.Base):
    __tablename__ = 'movies'

    title = Column(String(100))
    description = Column(String)
    trailer = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    genre_id = Column(Integer, ForeignKey(f"{Genre.__tablename__}.id"), nullable=False)
    director_id = Column(Integer, ForeignKey(f"{Director.__tablename__}.id"), nullable=False)

    genre = relationship("Genre")
    director = relationship("Director")
    favorites_movies = relationship("FavoritesMovie")


class User(models.Base):
    __tablename__ = "users"

    email = Column(String(100), unique=True)
    password = Column(String(300), nullable=False)
    name = Column(String(100))
    surname = Column(String(100))
    favorite_genre = Column(Integer, ForeignKey(f"{Genre.__tablename__}.id"))
    favorite_genre_object = relationship("Genre")
    favorite_movies = relationship("Movie", secondary="favorite_movies")


class FavoritesMovie(models.BaseManyToMany):
    __tablename__ = 'favorite_movies'

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True, autoincrement=False)
    movie_id = Column(Integer, ForeignKey("movies.id"), primary_key=True, autoincrement=False)

    movies = relationship("Movie")


