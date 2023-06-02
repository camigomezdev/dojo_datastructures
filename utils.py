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
    country_input = input(f'{Fore.BLUE}Ingrese la ciudad para su consulta: {Style.RESET_ALL}')

    students_by_country = [
        dict
        for dict in DICT_CSV
        if country_input.lower() == clean_string(dict['pais'])
    ]
    pprint(students_by_country)

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