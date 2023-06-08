import csv

# Función para leer el archivo CSV y cargar los datos en una estructura adecuada
def leer_datos_csv(data):
    with open(data, newline='') as archivo:
        lector = csv.DictReader(archivo)
        datos = list(lector)
    return datos

# Función para escribir el reporte en un archivo nuevo
def escribir_reporte(data, reporte):
    with open(data, 'w', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(reporte)

# Obtener todos los estudiantes que pertenezcan a una ciudad dada
def obtener_estudiantes_por_ciudad(estudiantes, ciudad):
    return [estudiante for estudiante in estudiantes if estudiante['ciudad'] == ciudad]

# Obtener todos los estudiantes que vivan en un país dado
def obtener_estudiantes_por_pais(estudiantes, pais):
    return [estudiante for estudiante in estudiantes if estudiante['pais'] == pais]

# Obtener todos los estudiantes que estén dentro del rango de edades dado
def obtener_estudiantes_por_rango_edad(estudiantes, rango_edad):
    edad_min, edad_max = rango_edad
    return [estudiante for estudiante in estudiantes if edad_min <= int(estudiante['edad']) <= edad_max]

# Obtener todas las ciudades de residencia de los estudiantes
def obtener_ciudades_residencia(estudiantes):
    return {estudiante['ciudad'] for estudiante in estudiantes}

# Identificar la edad promedio por carrera
def obtener_edad_promedio_por_carrera(estudiantes):
    edades_por_carrera = {}
    conteo_por_carrera = {}

    for estudiante in estudiantes:
        carrera = estudiante['carrera']
        edad = int(estudiante['edad'])

        if carrera in edades_por_carrera:
            edades_por_carrera[carrera] += edad
            conteo_por_carrera[carrera] += 1
        else:
            edades_por_carrera[carrera] = edad
            conteo_por_carrera[carrera] = 1

    edad_promedio_por_carrera = {carrera: edades_por_carrera[carrera] / conteo_por_carrera[carrera]
                                 for carrera in edades_por_carrera}
    return edad_promedio_por_carrera

# Indicar por carrera si el estudiante está por encima o por debajo del promedio de edad
def indicar_estudiantes_por_encima_por_debajo(estudiantes, edad_promedio_por_carrera):
    resultado = {}

    for estudiante in estudiantes:
        carrera = estudiante['carrera']
        edad = int(estudiante['edad'])
        promedio = edad_promedio_por_carrera[carrera]

        if edad > promedio:
            resultado.setdefault(carrera, {'encima': [], 'debajo': []})['encima'].append(estudiante)
        else:
            resultado.setdefault(carrera, {'encima': [], 'debajo': []})['debajo'].append(estudiante)

    return resultado

# Agrupar los estudiantes en diferentes rangos de edad (18-25, 26-35, mayores de 35)
def agrupar_estudiantes_por_rango_edad(estudiantes):
    rango_18_25 = []
    rango_26_35 = []
    mayores_35 = []

    for estudiante in estudiantes:
        edad = int(estudiante['edad'])

        if 18 <= edad <= 25:
            rango_18_25.append(estudiante)
        elif 26 <= edad <= 35:
            rango_26_35.append(estudiante)
        else:
            mayores_35.append(estudiante)

    return {'18-25': rango_18_25, '26-35': rango_26_35, 'mayores de 35': mayores_35}

# Identificar la ciudad que tiene la mayor variedad de carreras universitarias entre los estudiantes
def obtener_ciudad_mayor_variedad_carreras(estudiantes):
    ciudades = {}

    for estudiante in estudiantes:
        ciudad = estudiante['ciudad']
        carrera = estudiante['carrera']

        if ciudad in ciudades:
            ciudades[ciudad].add(carrera)
        else:
            ciudades[ciudad] = {carrera}

    ciudad_max_variedad_carreras = max(ciudades, key=lambda x: len(ciudades[x]))
    return ciudad_max_variedad_carreras

# Función para mostrar el menú y realizar las consultas
def mostrar_menu(estudiantes):
    while True:
        print("\n--- MENÚ ---")
        print("1. Obtener todos los estudiantes que pertenezcan a una ciudad dada")
        print("2. Obtener todos los estudiantes que vivan en un país dado")
        print("3. Obtener todos los estudiantes que estén dentro del rango de edades dado")
        print("4. Obtener todas las ciudades de residencia de los estudiantes")
        print("5. Identificar la edad promedio por carrera")
        print("6. Indicar por carrera si el estudiante está por encima o por debajo del promedio de edad")
        print("7. Agrupar los estudiantes en diferentes rangos de edad")
        print("8. Identificar la ciudad que tiene la mayor variedad de carreras universitarias")
        print("0. Salir")

        opcion = input("Ingrese el número de la opción que desea ejecutar: ")

        if opcion == '0':
            break
        elif opcion == '1':
            ciudad = input("Ingrese el nombre de la ciudad: ")
            estudiantes_ciudad = obtener_estudiantes_por_ciudad(estudiantes, ciudad)
            reporte = [(estudiante['nombre'], estudiante['apellido'], estudiante['ciudad'],
                        estudiante['pais'], estudiante['edad'], estudiante['carrera'])
                       for estudiante in estudiantes_ciudad]
            escribir_reporte("reporte_ciudad.csv", reporte)
            print("Reporte generado correctamente.")
        elif opcion == '2':
            pais = input("Ingrese el nombre del país: ")
            estudiantes_pais = obtener_estudiantes_por_pais(estudiantes, pais)
            reporte = [(estudiante['nombre'], estudiante['apellido'], estudiante['ciudad'],
                        estudiante['pais'], estudiante['edad'], estudiante['carrera'])
                       for estudiante in estudiantes_pais]
            escribir_reporte("reporte_pais.csv", reporte)
            print("Reporte generado correctamente.")
        elif opcion == '3':
            edad_min = int(input("Ingrese la edad mínima: "))
            edad_max = int(input("Ingrese la edad máxima: "))
            rango_edad = (edad_min, edad_max)
            estudiantes_rango_edad = obtener_estudiantes_por_rango_edad(estudiantes, rango_edad)
            reporte = [(estudiante['nombre'], estudiante['apellido'], estudiante['ciudad'],
                        estudiante['pais'], estudiante['edad'], estudiante['carrera'])
                       for estudiante in estudiantes_rango_edad]
            escribir_reporte("reporte_rango_edad.csv", reporte)
            print("Reporte generado correctamente.")
        elif opcion == '4':
            ciudades = obtener_ciudades_residencia(estudiantes)
            print("Ciudades de residencia de los estudiantes:")
            for ciudad in ciudades:
                print(ciudad)
        elif opcion == '5':
            edad_promedio_por_carrera = obtener_edad_promedio_por_carrera(estudiantes)
            for carrera, promedio in edad_promedio_por_carrera.items():
                print(f"Edad promedio para la carrera {carrera}: {promedio:.2f}")
        elif opcion == '6':
            edad_promedio_por_carrera = obtener_edad_promedio_por_carrera(estudiantes)
            estudiantes_por_encima_por_debajo = indicar_estudiantes_por_encima_por_debajo(estudiantes,
                                                                                         edad_promedio_por_carrera)
            for carrera, estudiantes in estudiantes_por_encima_por_debajo.items():
                print(f"Carrera: {carrera}")
                print("Estudiantes por encima del promedio:")
                for estudiante in estudiantes['encima']:
                    print(f"{estudiante['nombre']} {estudiante['apellido']}")
                print("Estudiantes por debajo del promedio:")
                for estudiante in estudiantes['debajo']:
                    print(f"{estudiante['nombre']} {estudiante['apellido']}")
        elif opcion == '7':
            estudiantes_por_rango_edad = agrupar_estudiantes_por_rango_edad(estudiantes)
            for rango, estudiantes in estudiantes_por_rango_edad.items():
                print(f"Rango de edad: {rango}")
                for estudiante in estudiantes:
                    print(f"{estudiante['nombre']} {estudiante['apellido']}")
        elif opcion == '8':
            ciudad_max_variedad_carreras = obtener_ciudad_mayor_variedad_carreras(estudiantes)
            print(f"La ciudad con la mayor variedad de carreras universitarias es: {ciudad_max_variedad_carreras}")
        else:
            print("Opción inválida. Intente nuevamente.")

# Código principal
data = 'data.csv'
estudiantes = leer_datos_csv(data)
mostrar_menu(estudiantes)
