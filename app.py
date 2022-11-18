from flask import Flask, jsonify

from functions import get_movie_by_title, get_movie_by_year, rating_by_keyword, get_movie_by_genre

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route("/movies/<title>")
def page_movies(title):
    movie = get_movie_by_title(title)
    return jsonify(movie)


@app.route("/movies/<int:from_year>/to/<int:to_year>")
def range_year_movies(from_year, to_year):
    year_range = get_movie_by_year(from_year, to_year)
    return jsonify(year_range)


@app.route("/rating/<rating>")
def children_rating(rating):
    all_ratings = rating_by_keyword(rating)
    return jsonify(all_ratings)


@app.route("/genre/<genre>")
def movie_by_genre(genre):
    genres = get_movie_by_genre(genre)
    return jsonify(genres)


if __name__ == '__main__':
    app.run()
