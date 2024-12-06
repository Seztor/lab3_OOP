import typing as tp


class AgeGroupsAdapter:
    '''Класс позволяющих разделять людей на возрастные группы'''

    def __init__(self, ages_data: tp.List[int], people_data: tp.List[tp.Tuple[str,int]]):
        '''Инициализация класса'''
        self.ages_data = [-1] + ages_data + [123]
        self.people_data = people_data
        self.ages_groups_dict = {(self.ages_data[i]+1,self.ages_data[i+1]):list() for i in range(len(self.ages_data)-1)}

    def get_person_age_group(self, person_data: tp.Tuple[str,int]):
        '''Получение возрастной группы человека'''
        _, age = person_data
        for i in range(len(self.ages_data)-1):
            if self.ages_data[i] < age <= self.ages_data[i+1]:
                self.ages_groups_dict[(self.ages_data[i]+1, self.ages_data[i+1])].append(person_data)


    def group_all_data(self):
        '''Сгрупировать людей по возрасту'''
        for person_data in self.people_data:
            self.get_person_age_group(person_data)


    def display_data(self):
        self.group_all_data()
        for i in range(len(self.ages_groups_dict.items())-1,-1,-1):
            age_range, names = list(self.ages_groups_dict.items())[i]
            st_age, end_age = age_range
            if names:
                if i==len(self.ages_groups_dict.items())-1:

                    print(f"{st_age}+:",   ", ".join([f"{item[0]} ({item[1]})" for item in names]))
                    print()
                else:
                    print(f"{st_age}-{end_age}:",  ", ".join([f"{item[0]} ({item[1]})" for item in names]))
                    print()


if __name__ == "__main__":
    '''Получение данных'''
    ages_data = list(map(int, input().split()))
    st = input()
    people_data = []
    while st != 'END':
        try:
            temp_data = st.split(',')
            temp_name = temp_data[0].strip()
            temp_age = int(temp_data[1])
            people_data.append( (temp_name, temp_age) )
        except Exception as e:
            print("Ошибка ввода:",e)
        st = input()

    '''Создание класса и получение групп возрастов'''
    ageGroupAdapter = AgeGroupsAdapter(ages_data=ages_data, people_data=people_data)
    ageGroupAdapter.display_data()







