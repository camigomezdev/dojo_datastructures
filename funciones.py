import csv

# Función para leer el archivo CSV y cargar los datos en una lista de diccionarios
def read_data(data_file):
    with open(data_file, 'r') as file:
        reader = csv.DictReader(file)
        data = [dict(row) for row in reader]
    return data

# Función para obtener todos los estudiantes que pertenezcan a una ciudad dada
def get_students_from_city(data,city):
   estudiantes = [estudiante for estudiante in data if estudiante['ciudad']==city]
   print(estudiantes)
   return estudiantes

# Función para obtener todos los estudiantes que vivan en un país dado
def get_students_from_country(data,country):
   estudiantes = [estudiante for estudiante in data if estudiante['pais']==country]
   print(estudiantes)
   return estudiantes

# Función para obtener todos los estudiantes que estén dentro del rango de edades dado
def get_students_in_age_range(data,min_age, max_age):
    estudiantes = [estudiante for estudiante in data if min_age<= estudiante['edad'] <= max_age]
    print(estudiantes)
    return estudiantes

# Función para obtener todas las ciudades de residencia de los estudiantes
def get_cities(data):
    ciudades = {estudiante['ciudad'] for estudiante in data}
    print(ciudades)
    return ciudades

# Función para calcular la edad promedio por carrera
def age_average_by_career(data):
    edades_por_carrera = {}
    cantidad_por_carrera = {}
    for estudiante in data:
        carrera = estudiante['carrera']
        edad = int(estudiante['edad'])
        edades_por_carrera[carrera] = edades_por_carrera.get(carrera, 0) + edad
        cantidad_por_carrera[carrera] = cantidad_por_carrera.get(carrera, 0) + 1
    edad_promedio_por_carrera = {carrera: edades_por_carrera[carrera] / cantidad_por_carrera[carrera] for carrera in edades_por_carrera}
    print(edad_promedio_por_carrera)
    return edad_promedio_por_carrera

# Función para Indicar por carrera si el estudiante está por encima o por debajo del promedio de edad.
def above_or_below_average(data):
    estudiantes_por_carrera = {}
    for estudiante in data:
        carrera = estudiante['carrera']
        estudiantes_por_carrera.setdefault(carrera, []).append(estudiante)
    
    estudiantes_por_encima = {}
    estudiantes_por_debajo = {}
    for carrera, estudiantes in estudiantes_por_carrera.items():
        estudiantes_por_encima[carrera] = []
        estudiantes_por_debajo[carrera] = []
        edad_promedio = age_average_by_career(estudiantes)
        for estudiante in estudiantes:
            if int(estudiante['edad']) < edad_promedio[carrera]:
                estudiantes_por_debajo[carrera].append(estudiante)
            else:
                estudiantes_por_encima[carrera].append(estudiante)
    print("# \n# \n#\n")
    print('estudiantes por encima del promedio por carrera:\n')
    print(estudiantes_por_encima)
    print("# \n# \n#\n")
    print('estudiantes por debajo del promedio por carrera:\n')
    print(estudiantes_por_debajo)
    return estudiantes_por_encima, estudiantes_por_debajo

# Función para agrupar los estudiantes en diferentes rangos de edad
def group_students_by_age_range(data):
    estudiantes_por_rango = {
        '18-25': [],
        '26-35': [],
        'mayores de 35': []
    }
    
    for estudiante in data:
        edad = int(estudiante['edad'])
        if 18 <= edad <= 25:
            estudiantes_por_rango['18-25'].append(estudiante)
        elif 26 <= edad <= 35:
            estudiantes_por_rango['26-35'].append(estudiante)
        else:
            estudiantes_por_rango['mayores de 35'].append(estudiante)
    for range in estudiantes_por_rango:
        print(range)
        print(estudiantes_por_rango[range])
        print('####################################################\n')
    return estudiantes_por_rango

# Función para obtener la ciudad con la mayor variedad de carreras universitarias entre los estudiantes
def get_city_with_greatest_variety(data):
    ciudades_carreras = {}
    for estudiante in data:
        ciudad = estudiante['ciudad']
        carrera = estudiante['carrera']
        ciudades_carreras.setdefault(ciudad, set()).add(carrera)
    
    ciudad_con_mayor_variedad = max(ciudades_carreras, key=lambda ciudad: len(ciudades_carreras[ciudad]))
    print(ciudad_con_mayor_variedad)
    return ciudad_con_mayor_variedad