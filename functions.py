import sqlite3


# датабазные функции
def get_data_from_base():
    con = sqlite3.connect('netflix.db')  # Подключаемся к БД
    cur = con.cursor()  # Запускаем курсор, с помощью которого мы будем получать данные из БД
    sqlite_query = f"Select title, country, release_year, description FROM netflix ORDER BY release_year DESC"
    result = cur.execute(sqlite_query)  # Выполняем запрос с помощью курсора
    data = cur.fetchall()  # С помощью этой функции получаем результат запроса в виде списка кортежей
    con.close()  # После выполнения запросов обязательно закрываем соединение с БД
    return data


def get_title_year_from_base():
    con = sqlite3.connect('netflix.db')  # Подключаемся к БД
    cur = con.cursor()  # Запускаем курсор, с помощью которого мы будем получать данные из БД
    sqlite_query = f"Select title, release_year FROM netflix LIMIT 100"
    result = cur.execute(sqlite_query)  # Выполняем запрос с помощью курсора
    data = cur.fetchall()  # С помощью этой функции получаем результат запроса в виде списка кортежей
    con.close()  # После выполнения запросов обязательно закрываем соединение с БД
    return data


def get_data_for_age_rating():
    con = sqlite3.connect('netflix.db')  # Подключаемся к БД
    cur = con.cursor()  # Запускаем курсор, с помощью которого мы будем получать данные из БД
    sqlite_query = f"Select title, rating, description FROM netflix"
    result = cur.execute(sqlite_query)  # Выполняем запрос с помощью курсора
    data = cur.fetchall()  # С помощью этой функции получаем результат запроса в виде списка кортежей
    con.close()  # После выполнения запросов обязательно закрываем соединение с БД
    return data


def get_genre_from_base():
    con = sqlite3.connect('netflix.db')  # Подключаемся к БД
    cur = con.cursor()  # Запускаем курсор, с помощью которого мы будем получать данные из БД
    sqlite_query = f"Select title, listed_in, description, release_year FROM netflix ORDER BY release_year DESC"
    result = cur.execute(sqlite_query)  # Выполняем запрос с помощью курсора
    data = cur.fetchall()  # С помощью этой функции получаем результат запроса в виде списка кортежей
    con.close()  # После выполнения запросов обязательно закрываем соединение с БД
    return data


def get_actors_from_base():
    con = sqlite3.connect('netflix.db')  # Подключаемся к БД
    cur = con.cursor()  # Запускаем курсор, с помощью которого мы будем получать данные из БД
    sqlite_query = f"Select title, netflix.cast FROM netflix"
    result = cur.execute(sqlite_query)  # Выполняем запрос с помощью курсора
    data = cur.fetchall()  # С помощью этой функции получаем результат запроса в виде списка кортежей
    con.close()  # После выполнения запросов обязательно закрываем соединение с БД
    return data


def get_all_from_base():
    con = sqlite3.connect('netflix.db')  # Подключаемся к БД
    cur = con.cursor()  # Запускаем курсор, с помощью которого мы будем получать данные из БД
    sqlite_query = f"Select title, type, release_year, listed_in, description FROM netflix"
    result = cur.execute(sqlite_query)  # Выполняем запрос с помощью курсора
    data = cur.fetchall()  # С помощью этой функции получаем результат запроса в виде списка кортежей
    con.close()  # После выполнения запросов обязательно закрываем соединение с БД
    return data


# эппроутовские функции
def get_movie_by_genre(genre):
    genres = []
    for item in get_genre_from_base():
        if genre.lower() in item[1].lower():
            g = {
                "title": item[0],
                "description": item[2],
            }
            if len(genres) < 10:
                genres.append(g)
    return genres


def get_movie_by_rating():
    movies = []
    for item in get_data_for_age_rating():
        r = {
            "title": item[0],
            "rating": item[1],

        }
        movies.append(r)
    return movies


def new_rating():
    movies = []
    for item in get_movie_by_rating():
        if item['rating'] in ('G', 'TV-G'):
            item['rating'] = 'children, family'
        elif item['rating'] in ('PG', 'TV-PG', 'TV-14', 'PG-13'):
            item['rating'] = 'family'
        elif item['rating'] in ('R', 'TV-MA', 'NC-17'):
            item['rating'] = 'adult'
        movies.append(item)
    return movies


def rating_by_keyword(rating):
    keywords = []
    for item in new_rating():
        if rating in item['rating']:
            keywords.append(item)
    return keywords


def get_movie_by_title(title):
    for item in get_data_from_base():
        d = {
            "title": item[0],
            "country": item[1],
            "release_year": item[2],
            "description": item[3]
        }
        if title in d["title"]:
            return d


def get_movie_title_year():
    s = []
    for item in get_title_year_from_base():
        d = {
            "title": item[0],
            "release_year": item[1],
        }
        s.append(d)
    return s


def get_movie_by_year(from_year: int, to_year: int):
    years = []
    for item in get_movie_title_year():
        if from_year <= item["release_year"] <= to_year:
            years.append(item)
    return years


# ШАГ 5
def actors_cast(one, two):
    actors = []
    for item in get_actors_from_base():
        if one in item[1] and two in item[1]:
            actors.append(item)
    if len(actors) > 2:
        return actors
    else:
        pass


# ШАГ 6
def get_type(type, year: int, genre):
    movies = []
    for item in get_all_from_base():
        if type.lower() in item[1].lower() and year == item[2] and genre.lower() in item[3].lower():
            types = {
                "title": item[0],
                "description": item[4],
            }
            movies.append(types)
    return movies
