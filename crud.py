"""CRUD operations to populate the ratings database in the movie ratings app."""

from model import db, User, Movie, Rating, connect_to_db


def create_user(email, password, name):
    """Create and return a new user."""

    user = User(email=email, password=password, name=name)

    db.session.add(user)
    db.session.commit()

    return user


def create_movie(title, overview, release_date, poster_path, genre):
    """Create and return a new movie."""

    movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path, genre=genre)

    db.session.add(movie)
    db.session.commit()

    return movie


def get_movies():
    """Gets all movies in the database."""

    return Movie.query.all()


def get_movie_by_id(movie_id):

    return Movie.query.get(movie_id)


def create_rating(score, movie, user):
    """Create and return a new rating."""

    rating = Rating(score=score, movie=movie, user=user,)

    db.session.add(rating)
    db.session.commit()

    return rating













if __name__ == '__main__':
    from server import app
    connect_to_db(app)