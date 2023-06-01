from funciones import *

def menu():
    data = read_data('data.csv')
    option = "no option selected"
    while option != 9:
        print('MENU DE OPCIONES')
        print('1) Obtener todos los estudiantes que pertenezcan a una ciudad dada.')
        print('2) Obtener todos los estudiantes que vivan en un país dado.')
        print('3) Obtener todos los estudiantes que estén dentro del rango de edades dado.')
        print('4) Obtener todas las ciudades de residencia de los estudiantes.')
        print('5) Identificar la edad promedio por carrera.')
        print('6) Indicar por carrera si el estudiante está por encima o por debajo del promedio de edad.')
        print('7) Agrupa los estudiantes en diferentes rangos de edad (18-25, 26-35, mayores de 35).')
        print('9) SALIR')
        option = int(input("Ingrese el número de la opción que desea ejecutar: "))
        if option == 1:
            city = input('Ingrese la ciudad que quiere buscar: ')
            get_students_from_city(data, city)
        elif option == 2:
            country = input('Ingrese el pais que quiere buscar: ')
            get_students_from_country(data, country)
        elif option == 3:
            min_age = input('Ingrese la edad minima: ')
            max_age = input('Ingrese la edad maxima: ')
            get_students_in_age_range(data, min_age,max_age)
        elif option == 4:
            get_cities(data)
        elif option == 5:
            age_average_by_career(data)
        elif option == 6:
            above_or_below_average(data)
        elif option == 7:
            group_students_by_age_range(data)
        elif option == 8:
            get_city_with_greatest_variety(data)


if __name__ == "__main__":
        menu()
