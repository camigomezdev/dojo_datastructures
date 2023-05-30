import csv

def csv_to_dict():
    with open('data.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        return list(csv_reader)

dict_csv = csv_to_dict()

def get_all_students_by_city():
    pass

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