import csv


def read_csv(url_file='data.csv'):
    """
    Read a CSV file and return its contents as a dictionary.

    Args:
        url_file (str): URL or path to the CSV file. Default is 'data.csv'.

    Returns:
        dict: A dictionary containing the CSV data, with row numbers as keys and row data as values.
    """
    csv_data = {}
    with open(url_file) as file:
        csv_reader = csv.DictReader(file, delimiter=',')
        # skipping first row (headers row)
        next(csv_reader)
        for key, row in enumerate(csv_reader):
            csv_data[key] = row

        return csv_data


def get_users_between_age_range(min_age, max_age):
    """
    Get a list of users within a specified age range.

    Args:
        min_age (int): Minimum age of users to include.
        max_age (int): Maximum age of users to include.

    Returns:
        list: A list of user records that fall within the specified age range.
    """
    if min_age > 0 and max_age > 0:
        csv_data = read_csv()
        return [
            row for row in csv_data.values()
            if min_age <= int(row['edad']) <= max_age
        ]
    else:
        print('Ingresa una edad valida')


def get_distinct_countries():
    """
    Get a set of distinct countries from the CSV data.

    Returns:
        set: A set of distinct country names.
    """
    csv_data = read_csv()
    return {row['pais'] for row in csv_data.values()}


def get_distinct_cities():
    """
    Get a set of distinct cities from the CSV data.

    Returns:
        set: A set of distinct city names.
    """
    csv_data = read_csv()
    return {row['ciudad'] for row in csv_data.values()}


def get_users_by_country(country):
    """
    Get a list of users from a specific country.

    Args:
        country (str): Name of the country.

    Returns:
        list: A list of user records from the specified country.
    """
    if does_this_country_exists(country):
        csv_data = read_csv()
        return [row for row in csv_data.values() if row['pais'] == country]
    else:
        print(f'No hay registros del pais: {country}')


def get_users_by_city(city):
    """
    Get a list of users from certain city

    Args:
        city (str): Name of the city.

    Returns:
        list: A list of user records from the specific city
    """
    if does_this_city_exists(city):
        csv_data = read_csv()
        return [row for row in csv_data.values() if row['ciudad'] == city]
    else:
        print(f'No hay registros de la ciudad: {city}')


def does_this_country_exists(country):
    """
    Check if a country exists in the CSV data.

    Args:
        country (str): Name of the country.

    Returns:
        bool: True if the country exists, False otherwise.
    """
    return country in get_distinct_countries()


def does_this_city_exists(city):
    """
    Check if a city exists in the CSV data.

    Args:
        city (str): Name of the city.

    Returns:
        bool: True if the city exists, False otherwise.
    """
    return city in get_distinct_cities()


def group_users_by_career():
    """
    Group users by their career.

    Returns:
        dict: A dictionary where the keys are career names and the values are lists of user records.
    """
    csv_data = read_csv()
    final_data = {}
    for row in csv_data.values():
        career = row['carrera']
        if career not in final_data:
            final_data[career] = []

        final_data[career].append(row)

    return final_data


def print_r(iterable):
    for row in iterable:
        print(row)


def get_average_age_grouped_by_career():
    """
    Calculate the average age for each career.

    Returns:
        dict: A dictionary where the keys are career names and the values are the average ages as integers.
    """
    grouped_users_by_career = group_users_by_career()
    average_age_by_career = {}

    for career, users in grouped_users_by_career.items():
        total_age, average_age = 0, 0
        total_users = len(users)
        for user in users:
            total_age += int(user['edad'])
        average_age = total_age / total_users
        average_age_by_career[career] = int(average_age)

    return average_age_by_career


def compare_age_by_career_average(age, career):
    """
    Compare the given age with the average age for a specific career.

    Args:
        age (str): Age to compare.
        career (str): Name of the career.

    Returns:
        str: A string indicating the comparison result.
    """
    average_age_grouped_by_career = int(
        get_average_age_grouped_by_career()[career]
    )

    if int(age) > average_age_grouped_by_career:
        return f" - EDAD MAYOR AL PROMEDIO ({average_age_grouped_by_career})"
    elif int(age) < average_age_grouped_by_career:
        return f" - EDAD MENOR AL PROMEDIO ({average_age_grouped_by_career})"
    else:
        return f" - EDAD IGUAL AL PROMEDIO ({average_age_grouped_by_career})"


def list_users_with_age_comparison():
    """
    Print the list of users with their ages and a comparison to the average age of their respective career.
    """
    csv_data = read_csv()
    for row in csv_data.values():
        print(
            f"Estudiante: {row['nombre']} {row['apellido']}, Edad: {row['edad']} {compare_age_by_career_average(row['edad'], row['carrera'])}")


def group_users_by_age_range():
    """
    Group users into age ranges.

    Returns:
        dict: A dictionary where the keys are age ranges and the values are lists of user records.
    """
    age_ranges = [(18, 25), (26, 35)]
    age_ranges_list = ["18-25", "26-35", "36+"]
    final_data = {}
    csv_data = read_csv()

    for user in csv_data.values():
        for index, (min_age, max_age) in enumerate(age_ranges):
            if int(user['edad']) >= 36:
                age_range = age_ranges_list[2]
            elif min_age <= int(user['edad']) <= max_age:
                age_range = age_ranges_list[index]

            if age_range not in final_data:
                final_data[age_range] = []

            final_data[age_range].append(user)

    return final_data


def group_careers_by_city():
    """
    Group careers by city.

    Returns:
        dict: A dictionary where the keys are city names and the values are lists of career names.
    """
    csv_data = read_csv()
    cities = get_distinct_cities()
    final_data = {}

    for city in cities:
        final_data[city] = []

    for row in csv_data.values():
        if row["carrera"] not in final_data[row["ciudad"]]:
            final_data[row["ciudad"]].append(row["carrera"])

    return final_data


def city_with_most_careers():
    """
    Find the city(s) with the most number of careers.

    Returns:
        list: A list of city names with the most number of careers.
    """
    final_data = []

    grouped_careers_by_city = group_careers_by_city()
    max_careers_per_city = len(max(grouped_careers_by_city.values()))
    KEYS_INDEX = 1
    VALUES_INDEX = 0
    for city in grouped_careers_by_city.items():
        if len(city[KEYS_INDEX]) == max_careers_per_city:
            final_data.append(city[VALUES_INDEX])

    return final_data


if __name__ == '__main__':
    program_running = True

    while program_running:
        print('=== M E N U ===\n' +
              '1.- Obtener todos los estudiantes que pertenezcan a una ciudad dada.\n' +
              '2.- Obtener todos los estudiantes que vivan en un país dado.\n' +
              '3.- Obtener todos los estudiantes que estén dentro del rango de edades dado.\n' +
              '4.- Obtener todas las ciudades de residencia de los estudiantes.\n' +
              '5.- Identificar la edad promedio por carrera.\n' +
              '6.- Indicar por carrera si el estudiante está por encima o por debajo del promedio de edad.\n' +
              '7.- Agrupa los estudiantes en diferentes rangos de edad (18-25, 26-35, mayores de 35).\n' +
              '8.- Identifica la ciudad que tienen la mayor variedad de carreras'
              ' universitarias entre los estudiantes.\n' +
              '9.- Salir.')
        option_user = input('Ingrese el numero de la opcion que desee realizar: ')

        match option_user:
            case "1":
                cities = get_distinct_cities()
                print("Ciudades disponibles: ")
                print_r(cities)
                city_selected = input("Ingrese la ciudad:").lower().capitalize()
                users_by_city = get_users_by_city(city_selected)
                if users_by_city:
                    print("Resultado: ")
                    print_r(users_by_city)
            case "2":
                countries = get_distinct_countries()
                print("Paises disponibles:")
                print_r(countries)
                country_selected = input("Ingrese el país: ").lower().capitalize()
                users_by_country = get_users_by_country(country_selected)
                if users_by_country:
                    print("Resultado: ")
                    print_r(users_by_country)
            case "3":
                age_min = int(input("Ingrese la edad mínima: "))
                age_max = int(input("Ingrese la edad máxima: "))
                users_between_age_range = get_users_between_age_range(age_min, age_max)
                print("Resultado: ")
                print_r(users_between_age_range)
            case "4":
                cities = get_distinct_cities()
                print("Ciudades de residencia de los estudiantes:")
                print_r(cities)
            case "5":
                average_age_grouped_by_career = get_average_age_grouped_by_career()
                print("Edad promedio por carrera:")
                print(average_age_grouped_by_career)
            case "6":
                list_users_with_age_comparison()
            case "7":
                grouped_users_by_age_range = group_users_by_age_range()
                print("Estudiantes agrupados por rangos de edad:")
                for age_range, users in grouped_users_by_age_range.items():
                    print(f"Rango: ({age_range}) - Estudiantes ({len(users)})")
                    print("Estudiantes:")
                    for user in users:
                        print(user)
            case "8":
                city_with_most_careers = city_with_most_careers()
                print("Ciudad con mayor variedad de carreras universitarias:")
                print(city_with_most_careers)
            case "9":
                program_running = False
                print("BYE!")
            case _:
                print("Ingrese una opcion valida. \n")
