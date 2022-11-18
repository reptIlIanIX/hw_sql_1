import sqlite3


def get_data_from_base():
    con = sqlite3.connect('netflix.db')  # Подключаемся к БД
    cur = con.cursor()  # Запускаем курсор, с помощью которого мы будем получать данные из БД
    sqlite_query = f"Select title, country, release_year, description FROM netflix ORDER BY release_year DESC"
    result = cur.execute(sqlite_query)  # Выполняем запрос с помощью курсора
    data = cur.fetchall()  # С помощью этой функции получаем результат запроса в виде списка кортежей
    con.close()  # После выполнения запросов обязательно закрываем соединение с БД
    return data


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


def get_title_year_from_base():
    con = sqlite3.connect('netflix.db')  # Подключаемся к БД
    cur = con.cursor()  # Запускаем курсор, с помощью которого мы будем получать данные из БД
    sqlite_query = f"Select title, release_year FROM netflix LIMIT 100"
    result = cur.execute(sqlite_query)  # Выполняем запрос с помощью курсора
    data = cur.fetchall()  # С помощью этой функции получаем результат запроса в виде списка кортежей
    con.close()  # После выполнения запросов обязательно закрываем соединение с БД
    return data


print(get_title_year_from_base())


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


print(get_movie_by_year(2010, 2016))
