import unittest
from src.lab3.task2_oop import AgeGroupsAdapter


class AgeGroupAdapterTestCase(unittest.TestCase):
    ages_data = [18, 25, 35, 45,60, 80, 100]
    people_data = [('Кошельков Захар Брониславович',105),
                   ('Дьячков Нисон Иринеевич',88),
                   ('Иванов Варлам Якунович',88),
                   ('Старостин Ростислав Ермолаевич',50),
                   ('Ярилова Розалия Трофимовна',29),
                   ('Соколов Андрей Сергеевич',15),
                   ('Егоров Алан Петрович',7),
                   ('Говоров Павел Игоревич',18)]


    def test_get_person_age_group_1(self):
        age_group_adapter1 = AgeGroupsAdapter(people_data=self.people_data, ages_data=self.ages_data)
        test_user_data = ('Говоров Павел Игоревич',18)
        age_group_adapter1.get_person_age_group(test_user_data)
        self.assertEqual(age_group_adapter1.ages_groups_dict[(0,18)], [test_user_data])


    def test_get_person_age_group_2(self):
        age_group_adapter2 = AgeGroupsAdapter(people_data=self.people_data, ages_data=self.ages_data)
        test_user_data = ('Иванов Варлам Якунович',88)
        age_group_adapter2.get_person_age_group(test_user_data)
        self.assertEqual(age_group_adapter2.ages_groups_dict[(81,100)], [test_user_data])


    def test_group_all_data(self):
        age_group_adapter3 = AgeGroupsAdapter(people_data=self.people_data, ages_data=self.ages_data)
        age_group_adapter3.group_all_data()
        dict_to_check = {(0, 18): [('Соколов Андрей Сергеевич', 15), ('Егоров Алан Петрович', 7), ('Говоров Павел Игоревич', 18)],
                         (19, 25): [],
                         (26, 35): [('Ярилова Розалия Трофимовна', 29)],
                         (36, 45): [],
                         (46, 60): [('Старостин Ростислав Ермолаевич', 50)],
                         (61, 80): [],
                         (81, 100): [('Дьячков Нисон Иринеевич', 88), ('Иванов Варлам Якунович', 88)], (101, 123): [('Кошельков Захар Брониславович', 105)]}
        self.assertEqual(age_group_adapter3.ages_groups_dict, dict_to_check)




