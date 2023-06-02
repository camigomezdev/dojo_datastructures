import csv
from pprint import pprint
from unicodedata import normalize
from colorama import Fore, Style

def csv_to_dict():
    with open('data.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        return list(csv_reader)

DICT_CSV = csv_to_dict()

def clean_string(sentence):
    normal_str = normalize('NFKD',sentence)
    clean_str = normal_str.encode('ASCII', 'ignore').decode('ASCII')
    return clean_str.casefold()

def get_all_students_by_city():
    city_input = input(f'{Fore.BLUE}Ingrese la ciudad para su consulta: {Style.RESET_ALL}')

    students_by_city = [
        dict
        for dict in DICT_CSV
        if city_input.lower() == clean_string(dict['ciudad'])
    ]
    pprint(students_by_city)

def get_all_students_by_country():
    country_input = input(f'{Fore.BLUE}Ingrese el pais para su consulta: {Style.RESET_ALL}')

    students_by_country = [
        dict
        for dict in DICT_CSV
        if country_input.lower() == clean_string(dict['pais'])
    ]
    pprint(students_by_country)

def get_all_students_by_age():
    range_age_input = input(f'{Fore.BLUE}Ingrese el rango de edad para su consuta (edad-edad): {Style.RESET_ALL}').split('-')

    students_by_age = [
        dict
        for dict in DICT_CSV
        if range_age_input[0] <= dict['edad'] <= range_age_input[1]
    ]
    pprint(students_by_age)

def get_all_hometowns():
    cities_of_students = []
    for dict in DICT_CSV:
        if dict['ciudad'] not in cities_of_students:
            cities_of_students.append(dict['ciudad'])            
    pprint(cities_of_students)

def get_careers():
    careers_of_student = []
    for dict in DICT_CSV:
        if dict['carrera'] not in careers_of_student:
            careers_of_student.append(dict['carrera'])
    return careers_of_student

def get_average_age_by_career():
    careers = get_careers()
    averages_age = []
    for career in careers:
        count_std = 0
        sum_age = 0
        for dict in DICT_CSV:
            if career == dict['carrera']:
                sum_age += int(dict['edad'])
                count_std +=1
        averages_age.append(int(sum_age/count_std))

    result = {}
    for key,value in zip(careers,averages_age): 
        if key not in result:
            result[key]=value

    pprint(result)

def get_average_status_student_by_career():
    pass

def get_group_students_with_ranges_age():
    pass

def get_the_most_city_with_careers():
    pass