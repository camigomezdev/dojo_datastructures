import csv


def almacenar_datos(archivo_csv):
    datos = []

    with open(archivo_csv, 'r') as archivo:
        lector_csv = csv.reader(archivo)
        encabezados = next(lector_csv)

        for fila in lector_csv:
            diccionario = dict(zip(encabezados, fila))
            datos.append(diccionario)

    return datos


def filtro_por_ciudad(datos, ciudad):

    datos_filtrados = [dato['nombre'] for dato in datos if dato['ciudad'] == ciudad]

    if datos_filtrados:
        for nombre in datos_filtrados:
            print(f"El estudiante {nombre} vive en la ciudad de {ciudad}")
    else:
        print(f"No se encontro la ciudad: {ciudad}")


def filtro_por_pais(datos, pais):

    datos_filtrados = [dato['nombre'] for dato in datos if dato['pais'] == pais]

    if datos_filtrados:
        for nombre in datos_filtrados:
            print(f"El estudiante {nombre} vive en el pais {pais}")
    else:
        print(f"No se encontro el pais: {pais}")


def mostrar_datos_rango_edades(datos, edad_min, edad_max):

    datos_filtrados = [dato['nombre'] for dato in datos if edad_min <= int(dato['edad']) <= edad_max]

    if datos_filtrados:
        for nombre in datos_filtrados:
            print(f"El estudiante {nombre} esta dentro del rango")
    else:
        print(f"No hay alumnos dentro del rango {edad_min}-{edad_max}")


def mostrar_todas_ciudades(datos):

    datos_filtrados = {dato['ciudad'] for dato in datos}

    for ciudad in datos_filtrados:
        print(ciudad)


def promedio_de_edad_por_carrera(datos, carrera):

    datos_filtrados = [int(dato['edad']) for dato in datos if dato['carrera'] == carrera]

    suma = sum(datos_filtrados)
    promedio = suma / len(datos_filtrados)

    return promedio


def estado_estudiante_promedio_edad(datos, carrera):

    nombres = [dato['nombre'] for dato in datos if dato['carrera'] == carrera]
    edades = [int(dato['edad']) for dato in datos if dato['carrera'] == carrera]
    promedio = promedio_de_edad_por_carrera(datos, carrera)

    for nombre, edad in zip(nombres, edades):
        if edad > promedio:
            print(f"{nombre} ({edad}) esta por encima del promedio de edad ({promedio}) de la carrera.")
        elif edad < promedio:
            print(f"{nombre} ({edad}) esta por debajo del promedio de edad ({promedio}) de la carrera.")
        else:
            print(f"{nombre} tiene la misma ({edad}) que el promedio de edad ({promedio}) de la carrera.")


def agrupar_estudiantes_por_rangos_de_edad(datos):

    nombres = [dato['nombre'] for dato in datos]
    edades = [int(dato['edad']) for dato in datos]

    rangos_edad = {
        '18-25': [],
        '26-35': [],
        'mayores de 35': []
    }

    for nombre, edad in zip(nombres, edades):
        if 18 <= edad <= 25:
            rangos_edad['18-25'].append(nombre)
        elif 26 <= edad <= 35:
            rangos_edad['26-35'].append(nombre)
        else:
            rangos_edad['mayores de 35'].append(nombre)

    print(f"Estudiantes dentro del rango 18-25: {rangos_edad['18-25']}")
    print(f"Estudiantes dentro del rango 26-55: {rangos_edad['26-35']}")
    print(f"Estudiantes dentro del rango <35: {rangos_edad['mayores de 35']}")


def mayor_variedad_carreras_por_ciudad(datos):

    ciudades_carreras = {}

    ciudades = [dato['ciudad'] for dato in datos]
    carreras = [dato['carrera'] for dato in datos]

    for ciudad, carrera in zip(ciudades, carreras):
        if ciudad in ciudades_carreras:
            ciudades_carreras[ciudad].append(carrera)
        else:
            ciudades_carreras[ciudad] = [carrera]

    carreras_por_ciudad = {ciudad: len(set(carreras)) for ciudad, carreras in ciudades_carreras.items()}

    print(carreras_por_ciudad)
