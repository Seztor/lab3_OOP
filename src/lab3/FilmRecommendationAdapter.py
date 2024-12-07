import typing as tp
from collections import Counter


class FilmRecommendationAdapter:
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
        '''Возвращает список тех фильмов, которые еще не просмотрены из подборки рекомендованных фильмов'''
        list_appropriate_users_id = self.search_users_with_similar_films(films_data_solo_user)
        set_films_from_appropriate_users = set(item for i in list_appropriate_users_id for item in self.users_data[i])
        return list(set_films_from_appropriate_users - set(films_data_solo_user))


    def get_all_films_watched_by_users(self, user_films_list: tp.List[int]) -> tp.List[int]:
        '''Возвращает список всех просмотренных фильмов, которые содержатся в заданном списке'''
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