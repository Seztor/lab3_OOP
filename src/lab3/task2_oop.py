from  src.lab3.AgeGroupsAdapter import AgeGroupsAdapter


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

