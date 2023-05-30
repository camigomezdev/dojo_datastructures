from csv_management import CsvManagement

csv_management = CsvManagement('data.csv')

options = """
    Opciones a consultar de la información del CSV de estudiantes!!!

    1) Obtener todos los estudiantes que pertenezcan a una ciudad dada.
    2) Obtener todos los estudiantes que vivan en un país dado.
    3) Obtener todos los estudiantes que estén dentro del rango de edades 
       dado.
    4) Obtener todas las ciudades de residencia de los estudiantes.
    5) Identificar la edad promedio por carrera.
    6) Indicar por carrera si el estudiante está por encima o por debajo del
       promedio de edad.
    7) Agrupa los estudiantes en diferentes rangos de edad (18-25, 26-35, 
       mayores de 35).
    8) Identifica la ciudad que tienen la mayor variedad de carreras 
       universitarias entre los estudiantes.
    9) Salir.
"""

value = None

while value is None or (1 <= value <= 9):
    print(options)
    option_entered = input("Ingresa una opción del 1 al 9: ")
    try:
        value = int(option_entered)

        if value == 1:
            city = input("Ingresa la ciudad: ")
            students = csv_management.get_students_by_city(city)

            if students:
                print(
                    f'Los estudiantes de la ciudad de {city} son: {students}'
                )
            else:
                print(f'No hay estudiantes asociados a {city}')

        if value == 2:
            country = input("Ingresa el pais: ")
            students = csv_management.get_students_by_country(country)

            if students:
                print(
                    f'Los estudiantes que viven en {country} son: {students}'
                )
            else:
                print(f'No hay estudiantes asociados a {country}')

        if value == 3:
            try:
                min_age = int(input("Ingresa la edad minima: "))
                max_age = int(input("Ingresa la edad maxima: "))

                students = csv_management.get_students_by_age_range(
                    min_age,
                    max_age
                )

                if students:
                    print(
                        f'Los estudiantes entre {min_age} y {max_age} son: {students}'
                    )
                else:
                    print('No hay estudiantes entre estas edades')

            except ValueError:
                print("Error: Debes ingresar un número válido.")

        if value == 4:
            cities = csv_management.get_cities()
            print(f'Estas son las ciudades dode residen los estudiantes: {cities}')

        if value == 5:
            carrera = input("Ingresa carrera para calcular promedio edad: ")
            average_age = csv_management.get_average_age_by_career(carrera)

            if average_age != 0:
                print(f'Para la carrera {carrera} el promedio es: {average_age}')

            print(f'No se puede calcular el proedio para la carrera: {carrera}')

        if value == 6:
            student_name = input("Ingresa el nombre del estudiante: ")
            student_is_above_or_below = csv_management.get_student_is_below_or_above_by_career_average_age(student_name)
            print(f'{student_is_above_or_below}')

        if value == 7:
            groups_by_age = csv_management.sort_students_by_age()

            for group, students in groups_by_age.items():
                print(f'{group}: {students}')

        if value == 8:
            cities_with_careers = csv_management.get_city_with_most_careers()

            print(f'La ciudad con mayor cantidad de carreras es: {cities_with_careers}')

        if value == 9:
            exit()

    except ValueError:
        print("Error: Debes ingresar un número válido.")
