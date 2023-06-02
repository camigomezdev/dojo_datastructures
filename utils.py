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
    
    students_by_city = []
    count_students = 0
    for dict in DICT_CSV:
        if city_input.lower() == clean_string(dict['ciudad']):
            students_by_city.append(dict)
            count_students += 1

    pprint(students_by_city)
    print(f'{Fore.GREEN}Cantidad de estudiantes en la ciudad {city_input}: {count_students}{Style.RESET_ALL}')

def get_all_students_by_country():
    pass

def get_all_students_by_age():
    pass

def get_all_hometowns():
    pass

def get_average_age_by_career():
    pass

def get_average_status_student_by_career():
    pass

def get_group_students_with_ranges_age():
    pass

def get_the_most_city_with_careers():
    pass