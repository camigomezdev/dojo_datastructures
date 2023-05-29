import csv


def read_csv(url_file='data.csv'):
    csv_data = {}
    with open(url_file) as file:
        csv_reader = csv.DictReader(file, delimiter=',')
        # skipping first row (headers row)
        next(csv_reader)
        for key, row in enumerate(csv_reader):
            csv_data[key] = row

        return csv_data


def get_users_between_age_range(min_age, max_age):
    if min_age > 0 and max_age > 0:
        csv_data = read_csv()
        return [
            row for row in csv_data.values()
            if min_age <= int(row['edad']) <= max_age
        ]
    else:
        print('Ingresa una edad valida')


def get_distinct_countries():
    csv_data = read_csv()
    return {row['pais'] for row in csv_data.values()}


def get_distinct_cities():
    csv_data = read_csv()
    return {row['ciudad'] for row in csv_data.values()}


def get_users_by_country(country):
    if does_this_country_exists(country):
        csv_data = read_csv()
        return [row for row in csv_data.values() if row['pais'] == country]
    else:
        print(f'No hay registros del pais: {country}')


def get_users_by_city(city):
    if does_this_city_exists(city):
        csv_data = read_csv()
        return [row for row in csv_data.values() if row['ciudad'] == city]
    else:
        print(f'No hay registros de la ciudad: {city}')


def does_this_country_exists(country):
    return country in get_distinct_countries()


def does_this_city_exists(city):
    return city in get_distinct_cities()


def group_users_by_career():
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
    csv_data = read_csv()
    for row in csv_data.values():
        print(
            f"Estudiante: {row['nombre']} {row['apellido']}, Edad: {row['edad']} {compare_age_by_career_average(row['edad'], row['carrera'])}")


def group_users_by_age_range():
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
    final_data = []

    grouped_careers_by_city = group_careers_by_city()
    max_careers_per_city = len(max(grouped_careers_by_city.values()))
    for city in grouped_careers_by_city.items():
        if len(city[1]) == max_careers_per_city:
            final_data.append(city[0])

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
