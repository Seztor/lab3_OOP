import typing as tp
from src.lab3.FilmRecommendationAdapter import FilmRecommendationAdapter
import codecs


if __name__ == "__main__":

    '''Открытие файлов'''
    file_users_data = open("users_list.txt")
    file_films_data = codecs.open("films_list.txt", encoding="utf_8_sig")

    T = tp.TypeVar("T")

    '''Получение данных с файлов'''
    users_data = [list(map(int, items.split(','))) for items in file_users_data.readlines()]

    films_data = []
    for items in file_films_data.readlines():
        items = items.strip().replace(',','$',1).split('$')
        id_film = int(items[0])
        name_film = items[1].strip()
        films_data.append((id_film, name_film))


    '''Создание класса и получение фильма'''
    filmAdapter = FilmRecommendationAdapter(films_data=films_data, users_data=users_data)

    try:
        my_watched_films = list(map(int, input().split(',')))
    except Exception as e:
        print("Ошибка ввода данных:", e)

    film_to_watch = filmAdapter.get_recommended_film(my_watched_films)
    print(film_to_watch)

    file_users_data.close()
    file_films_data.close()

