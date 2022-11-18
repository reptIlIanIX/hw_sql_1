from flask import Flask, jsonify, json

from functions import get_movie_by_title

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route("/movies/<title>")
def page_movies(title):
    movie = get_movie_by_title(title)
    return jsonify(movie)


if __name__ == '__main__':
    app.run()
