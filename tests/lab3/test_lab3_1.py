import unittest
from src.lab3.FilmRecommendationAdapter import FilmRecommendationAdapter


class FilmsAdapterTestCase(unittest.TestCase):
    films_data = [(1, 'Хатико'), (2, 'Мстители'), (3, 'Титаник'), (4, 'Джуманджи'), (5, 'Хакер')]
    users_data = [[1, 3, 5, 2], [2, 3, 4], [1], [3], [4, 4, 5], [1, 2, 3, 4, 5], [2, 3, 4]]
    film_adapter = FilmRecommendationAdapter(films_data=films_data, users_data=users_data)


    def test_search_users_with_similar_films(self):
        test_user_data = [2,3]
        arr_to_check = self.film_adapter.search_users_with_similar_films(test_user_data)
        self.assertListEqual(arr_to_check, [0, 1, 3, 6])


    def test_get_films_not_watched(self):
        test_user_data = [1, 2]
        films_not_watched = self.film_adapter.get_films_not_watched(test_user_data)
        self.assertListEqual(films_not_watched, [3,5])


    def test_get_all_films_watched_by_users(self):
        all_films_watched = self.film_adapter.get_all_films_watched_by_users([1,2,3,4,5])
        arr_to_check = [1, 3, 5, 2, 2, 3, 4, 1, 3, 4, 4, 5, 1, 2, 3, 4, 5, 2, 3, 4]
        self.assertListEqual(all_films_watched, arr_to_check)


    def test_get_recommended_film(self):
        film = self.film_adapter.get_recommended_film([3,4])
        self.assertEqual(film, "Мстители")

