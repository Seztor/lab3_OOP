import typing as tp
from collections import Counter
import codecs


class FilmRecommendation:
    '''Класс для поиска рекомендованных фильмов'''

    def __init__(self, films_data: tp.List[tp.Tuple[int,str]], users_data: tp.List[tp.List[int]]):
        '''Объявление атрибутов класса'''
        self.films_data = films_data
        self.users_data = users_data


    def search_users_with_similar_films(self, films_data_solo_user: tp.List[int]) -> tp.List[int]:
        '''Поиск пользователей со схожими уже просмотренными фильмами'''
        set_solo_user_data = set(films_data_solo_user)
        list_appropriate_users_id = []
        for ind, items in enumerate(self.users_data):
            set_items = set(items)
            if len(set_items & set_solo_user_data) >= len(set_items) / 2:
                list_appropriate_users_id.append(ind)
        return list_appropriate_users_id


    def get_films_not_watched(self, films_data_solo_user: tp.List[int]) -> tp.List[int]:
        '''Возвращает список тех фильмов, которые еще не просмотрены'''
        list_appropriate_users_id = self.search_users_with_similar_films(films_data_solo_user)
        set_films_from_appropriate_users = set(item for i in list_appropriate_users_id for item in self.users_data[i])
        return list(set_films_from_appropriate_users - set(films_data_solo_user))


    def get_all_films_watched_by_users(self, user_films_list: tp.List[int]) -> tp.List[int]:
        '''Возвращает список всех просмотренных фильмов'''
        set_user_films = set(user_films_list)
        return [item for films in self.users_data for item in films if item in set_user_films]


    def get_recommended_film(self, films_list: tp.List[int]) -> str:
        '''Получение фильма для просмотра'''
        list_films_user_not_watch = self.get_films_not_watched(films_list)
        if not list_films_user_not_watch:
            return "Нет, подходящих"
        list_all_watched_films = self.get_all_films_watched_by_users(list_films_user_not_watch)
        counted_films = Counter(list_all_watched_films)
        id_film_recommended = int(counted_films.most_common(1)[0][0])
        return self.films_data[id_film_recommended-1][1]

if __name__ == "__main__":

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
    filmAdapter = FilmRecommendation(films_data=films_data, users_data=users_data)
    try:
        my_watched_films = list(map(int, input().split(',')))
    except Exception as e:
        print("Ошибка ввода данных:", e)
    my_film = filmAdapter.get_recommended_film(my_watched_films)
    print(my_film)

    file_users_data.close()
    file_films_data.close()







