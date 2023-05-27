import csv

def load_data():
    """
    Load student data from the CSV file.

    Returns:
        list: A list of dictionaries containing student data.
    """
    data = []
    with open('data.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data

def generate_report(data):
    """
    Generate a report based on the student data.

    Args:
        data (list): A list of dictionaries containing student data.

    Raises:
        ValueError: If an invalid option is entered.

    Returns:
        None
    """
    while True:
        print("MENU:")
        print("1. Get all students from a given city")
        print("2. Get all students from a given country")
        print("3. Get all students within an age range")
        print("4. Get all cities of residence of the students")
        print("5. Identify the average age per major")
        print("6. Indicate for each major if the student is above or below the average age")
        print("7. Group the students into different age ranges")
        print("8. Identify the city with the highest variety of majors among the students")
        print("9. Exit")

        option = input("Enter the desired option: ")

        if option == "1":
            city = input("Enter the city: ")
            students_city = [student for student in data if student['ciudad'] == city]
            generate_students_report(students_city, "students_city.csv")
            print("Report generated: students_city.csv\n")
        elif option == "2":
            country = input("Enter the country: ")
            students_country = [student for student in data if student['pais'] == country]
            generate_students_report(students_country, "students_country.csv")
            print("Report generated: students_country.csv\n")
        elif option == "3":
            age_range = input("Enter the age range (e.g., 18-25): ")
            age_min, age_max = map(int, age_range.split('-'))
            students_age = [student for student in data if age_min <= int(student['edad']) <= age_max]
            generate_students_report(students_age, "students_age.csv")
            print("Report generated: students_age.csv\n")
        elif option == "4":
            residence_cities = {student['ciudad'] for student in data}
            print("Cities of residence of the students:")
            for city in residence_cities:
                print(city)
            print()
        elif option == "5":
            average_age_major = {}
            for student in data:
                major = student['carrera']
                age = int(student['edad'])
                if major in average_age_major:
                    average_age_major[major]['sum_ages'] += age
                    average_age_major[major]['num_students'] += 1
                else:
                    average_age_major[major] = {'sum_ages': age, 'num_students': 1}
            print("Average age per major:")
            for major, age_data in average_age_major.items():
                average = age_data['sum_ages'] / age_data['num_students']
                print(f"{major}: {average:.2f}")
            print()
        elif option == "6":
            average_age_major = {}
            for student in data:
                major = student['carrera']
                age = int(student['edad'])
                if major in average_age_major:
                    average_age_major[major]['sum_ages'] += age
                    average_age_major[major]['num_students'] += 1
                else:
                    average_age_major[major] = {'sum_ages': age, 'num_students': 1}
            print("Age indicator per major:")
            for student in data:
                major = student['carrera']
                age = int(student['edad'])
                average = average_age_major[major]['sum_ages'] / average_age_major[major]['num_students']
                if age > average:
                    status = "above"
                else:
                    status = "below"
                print(f"{student['nombre']} {student['apellido']} ({major}): {status} the average age")
            print()
        elif option == "7":
            age_ranges = {'18-25': 0, '26-35': 0, 'over 35': 0}
            for student in data:
                age = int(student['edad'])
                if 18 <= age <= 25:
                    age_ranges['18-25'] += 1
                elif 26 <= age <= 35:
                    age_ranges['26-35'] += 1
                else:
                    age_ranges['over 35'] += 1
            print("Age ranges:")
            for age_range, count in age_ranges.items():
                print(f"{age_range}: {count}")
            print()
        elif option == "8":
            city_majors = {}
            for student in data:
                city = student['ciudad']
                major = student['carrera']
                if city in city_majors:
                    city_majors[city].add(major)
                else:
                    city_majors[city] = {major}
            city_max_majors = max(city_majors, key=lambda x: len(city_majors[x]))
            print("City with the highest variety of majors:")
            print(f"{city_max_majors}: {', '.join(city_majors[city_max_majors])}")
            print()
        elif option == "9":
            print("Exiting the program...")
            break
        else:
            raise ValueError("Invalid option. Please enter a valid option.\n")

def generate_students_report(students, file_name):
    """
    Generate a CSV report containing student data.

    Args:
        students (list): A list of dictionaries containing student data.
        file_name (str): The name of the output file.

    Returns:
        None
    """
    with open(file_name, 'w', newline='') as csv_file:
        fieldnames = ['nombre', 'apellido', 'ciudad', 'pais', 'edad', 'carrera']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(students)

# Load the data from the CSV file
data = load_data()

# Generate the report
generate_report(data)
