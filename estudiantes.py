""" Funciones para obtener datos de estudiantes """

import csv
import os
from iterador_promedio_edades import IteradorPromedioEdades
from iterable_ciudades import IterableCiudades
from async_iterador_estadisticas_edades import AsyncIteradorEstadisticasEdades


class Estudiantes:
    """ Definición de la clases Estudiantes."""

    def __init__(self, nombre_csv):
        """ Guarda los estudiantes en una lista "_lista" y crea el directorio
            'Reportes'"""

        self._lista = []
        with open(nombre_csv) as archivo_csv:
            lector_csv = csv.DictReader(archivo_csv, delimiter=',')
            for linea in lector_csv:
                self._lista.append(linea)
        if not os.path.exists("Reportes"):
            os.makedirs("Reportes")

    def generador_ciudades(self):
        """Generador que regresa las ciudades una a una con su índice"""

        indice_ciudad = 0
        for ciudad in list({ciudad['ciudad'] for ciudad in self._lista}):
            yield indice_ciudad, ciudad
            indice_ciudad += 1

    def por_ciudad(self):
        """ Obtiene estudiantes por ciudad dada."""

        ciudades = self.generador_ciudades()
        lista_ciudades = []

        while True:
            try:
                indice_ciudad, ciudad = next(ciudades)
                lista_ciudades.append(ciudad)
                print(f"{indice_ciudad+1}) {ciudad}")
            except StopIteration:
                break
        ciudad_index = ""
        # validar que ciudad elegida esté dentro del rango
        while not ciudad_index.isdecimal()\
                or int(ciudad_index) > len(lista_ciudades)\
                or int(ciudad_index) - 1 < 0:
            ciudad_index = input(f"Elige una ciudad \
del 1 al {len(lista_ciudades)}: ")
        estudiantes_por_ciudad = [estudiante for estudiante
                                  in self._lista
                                  if estudiante['ciudad']
                                  == lista_ciudades[int(ciudad_index) - 1]]
        print(f"\nEstudiantes en {lista_ciudades[int(ciudad_index) - 1]} \
guardados en rchivo: 'Estudiantes_por_ciudad_\
({lista_ciudades[int(ciudad_index) - 1]}).csv'.")
        columnas = ['nombre', 'apellido', 'ciudad', 'pais', 'edad', 'carrera']
        with open(f"Reportes/Estudiantes_por_ciudad_\
({lista_ciudades[int(ciudad_index) - 1]}).csv", mode='w') as archivo:
            escritor = csv.DictWriter(archivo, delimiter=',',
                                      fieldnames=columnas)
            escritor.writeheader()
            for estudiante in estudiantes_por_ciudad:
                escritor.writerow(estudiante)

    def por_pais(self):
        """ Obtiene estudiantes por país dado."""

        paises = list({pais['pais'] for pais in self._lista})
        for index, pais in enumerate(paises):
            print(f"{index+1}) {pais}")
        pais_index = ""
        # validar que país elegido esté dentro del rango
        while not pais_index.isdecimal()\
                or int(pais_index) > len(paises)\
                or int(pais_index) - 1 < 0:
            pais_index = input(f"Elige un país \
del 1 al {len(paises)}: ")
        estudiantes_por_pais = [estudiante for estudiante
                                in self._lista
                                if estudiante['pais']
                                == paises[int(pais_index) - 1]]
        print(f"\nEstudiantes en {paises[int(pais_index) - 1]} guardados en\
archivo: 'Estudiantes_por_país_({paises[int(pais_index) - 1]}).csv'.")
        columnas = ['nombre', 'apellido', 'ciudad', 'pais', 'edad', 'carrera']
        with open(f"Reportes/Estudiantes_por_país_\
({paises[int(pais_index) - 1]}).csv", mode='w') as archivo:
            escritor = csv.DictWriter(archivo, delimiter=',',
                                      fieldnames=columnas)
            escritor.writeheader()
            for estudiante in estudiantes_por_pais:
                escritor.writerow(estudiante)

    def por_rango_de_edad(self):
        """ Obtiene estudiantes por rango de edad dado."""

        edades = list({int(edad['edad']) for edad in self._lista})
        edad_min = ""
        # validar que edad mínima elegida esté dentro del rango
        while not edad_min.isnumeric()\
                or int(edad_min) < min(edades)\
                or int(edad_min) - 1 > max(edades):
            edad_min = input(f"Proporciona una edad MÍNIMA dentro del\
 rango {min(edades)}-{max(edades)}: ")
        edad_min = int(edad_min)
        edad_max = ""
        # validar que edad máxima elegida esté dentro del rango
        while not edad_max.isnumeric()\
                or int(edad_max) < edad_min\
                or int(edad_max) - 1 > max(edades):
            edad_max = input(f"Proporciona una edad MÁXIMA dentro del\
 rango {edad_min}-{max(edades)}: ")
        edad_max = int(edad_max)
        print(f"Edad min: {edad_min} Edad max: {edad_max}")
        estudiantes_por_rango_de_edad = [estudiante for estudiante
                                         in self._lista
                                         if int(estudiante['edad']) >= edad_min
                                         and int(estudiante['edad'])
                                         <= edad_max]
        print(f"\nEstudiantes en rango de edad {edad_min}-{edad_max} guardados\
 en archivo: 'Estudiantes_por_rango_de_edad({edad_min}-{edad_max})'.csv")
        columnas = ['nombre', 'apellido', 'ciudad', 'pais', 'edad', 'carrera']
        with open(f"Reportes/Estudiantes_por_rango_de_edad\
({edad_min}-{edad_max}).csv", mode='w') as archivo:
            escritor = csv.DictWriter(archivo, delimiter=',',
                                      fieldnames=columnas)
            escritor.writeheader()
            for estudiante in estudiantes_por_rango_de_edad:
                escritor.writerow(estudiante)

    def ciudades_de_residencia(self):
        """ Obtiene las ciudades de residencia de los estudiantes."""

        ciudades = IterableCiudades(list({ciudad['ciudad']
                                          for ciudad in self._lista}))
        print("\nCiudades de residencia guardados en archivo: \
'Ciudades_de_residencia.csv'.")
        columnas = ['ciudad']
        with open("Reportes/Ciudades_de_residencia.csv", mode='w') as archivo:
            escritor = csv.DictWriter(archivo, delimiter=',',
                                      fieldnames=columnas)
            escritor.writeheader()
            for ciudad in ciudades:
                escritor.writerow({"ciudad": ciudad})

    def edad_promedio_por_carrera(self, escribir_archivo=False):
        """ Obtiene la edad promedio por carrera. """

        carreras = {carrera['carrera']: [] for carrera in self._lista}
        for estudiante in self._lista:
            carreras[estudiante['carrera']].append(int(estudiante['edad']))
        promedio_edad_por_carrera = {carrera: promedio
                                     for carrera, promedio
                                     in IteradorPromedioEdades(carreras)}
        if escribir_archivo:
            print("\nEdad promedio por carrera guardado en archivo: \
'Edad_promedio_por_carrera.csv'.")
            columnas = ['carrera', 'edad_promedio']
            with open("Reportes/Edad_promedio_por_carrera.csv",
                      mode='w') as archivo:
                escritor = csv.DictWriter(archivo, delimiter=',',
                                          fieldnames=columnas)
                escritor.writeheader()
                for carrera in promedio_edad_por_carrera:
                    escritor.writerow({'carrera': carrera,
                                       'edad_promedio':
                                           promedio_edad_por_carrera[carrera]})
        return promedio_edad_por_carrera

    def arriba_debajo_promedio_de_edad(self):
        """ Estudiantes arriba o debajo del promedio de edad."""

        estudiantes = []
        promedio_edad_por_carrera = self.edad_promedio_por_carrera(False)
        for carrera, edad_promedio in promedio_edad_por_carrera.items():
            for estudiante in self._lista:
                if estudiante['carrera'] == carrera:
                    if int(estudiante['edad']) < edad_promedio:
                        estudiante['arriba_debajo_promedio'] = "Debajo"
                    elif int(estudiante['edad']) > edad_promedio:
                        estudiante['arriba_debajo_promedio'] = "Arriba"
                    else:
                        estudiante['arriba_debajo_promedio'] = "Promedio"
                    estudiantes.append(estudiante)
        print("\nEstudiantes arriba o debajo de edad promedio por carrera \
guardado en archivo: 'Estudiantes_arriba_debajo_edad_promedio.csv'.")
        columnas = ['carrera', 'nombre', 'apellido',
                    'arriba_debajo_promedio']
        with open("Reportes/Estudiantes_arriba_debajo\
_edad_promedio.csv", mode='w') as archivo:
            escritor = csv.DictWriter(archivo, delimiter=',',
                                      fieldnames=columnas)
            escritor.writeheader()
            for estudiante in estudiantes:
                escritor.writerow({'carrera': estudiante['carrera'],
                                   'nombre': estudiante['nombre'],
                                   'apellido': estudiante['apellido'],
                                   'arriba_debajo_promedio':
                                       estudiante['arriba_debajo_promedio']})

    def por_rangos_de_edad(self):
        """ Estudiantes por rangos de edad (18-25, 26-35, mayores de 35)."""

        rangos = [[18, 25], [26, 35], [35]]
        estudiantes = []
        for rango in rangos:
            for estudiante in self._lista:
                if len(rango) > 1:
                    if (int(estudiante['edad']) >= rango[0]
                            and int(estudiante['edad']) <= rango[1]):
                        estudiante['rango_edad'] = (str(rango[0])
                                                    + "-" + str(rango[1]))
                        estudiantes.append(estudiante)
                else:
                    if int(estudiante['edad']) > rango[0]:
                        estudiante['rango_edad'] = ">" + str(rango[0])
                        estudiantes.append(estudiante)
        print("\nEstudiantes por rango de edad guardado en archivo: \
'Estudiantes_por_rango_de_edad.csv'.")
        columnas = ['rango_edad', 'nombre', 'apellido',
                    'ciudad', 'pais', 'edad']
        with open("Reportes/Estudiantes_por_rango_de_edad.csv",
                  mode='w') as archivo:
            escritor = csv.DictWriter(archivo, delimiter=',',
                                      fieldnames=columnas)
            escritor.writeheader()
            for estudiante in estudiantes:
                escritor.writerow({'rango_edad': estudiante['rango_edad'],
                                   'nombre': estudiante['nombre'],
                                   'apellido': estudiante['apellido'],
                                   'ciudad': estudiante['ciudad'],
                                   'pais': estudiante['pais'],
                                   'edad': estudiante['edad']})

    def max_carreras_por_ciudad(self, num_carreras_por_ciudad={}):
        """ Regresa la(s) ciudad(es) con mayor numero de carreras """

        max_numero_carreras = max(num_carreras_por_ciudad.values())
        ciudades = {ciudad: carreras for ciudad, carreras
                    in num_carreras_por_ciudad.items()
                    if carreras == max_numero_carreras}
        return ciudades

    def ciudad_max_carreras(self):
        """ Obtener ciudad con la mayor variedad de carreras universitarias."""

        ciudades = IterableCiudades(list({ciudad['ciudad']
                                          for ciudad in self._lista}))
        num_carreras_por_ciudad = {ciudad: 0 for ciudad in ciudades}
        for ciudad in ciudades:
            carreras_por_ciudad = []
            for estudiante in self._lista:
                if (estudiante['ciudad'] == ciudad and estudiante['carrera']
                        not in carreras_por_ciudad):
                    carreras_por_ciudad.append(estudiante['carrera'])
            num_carreras_por_ciudad[ciudad] = len(carreras_por_ciudad)
        print("\nCiudad(es) con mayor varidad de carreras guardado en \
archivo: 'Ciudad(es)_con_mayor_variedad_de_carreras.csv'.")
        columnas = ['ciudad', 'num_carreras']
        with open("Reportes/Ciudad(es)_con_mayor_variedad\
_de_carreras.csv", mode='w') as archivo:
            escritor = csv.DictWriter(archivo, delimiter=',',
                                      fieldnames=columnas)
            escritor.writeheader()
            for ciudad, carreras in self.max_carreras_por_ciudad(
                    num_carreras_por_ciudad).items():
                escritor.writerow({'ciudad': ciudad,
                                   'num_carreras': carreras})

    async def async_estadisticas_edad_por_carrera(self):
        """ Obtiene estadisticas de edades por carrera de forma asíncrona. """

        carreras = {carrera['carrera']: [] for carrera in self._lista}
        for estudiante in self._lista:
            carreras[estudiante['carrera']].append(int(estudiante['edad']))
        estadisticas_edades_por_carrera = {carrera: {"media": media,
                                                     "mediana": mediana,
                                                     "moda": moda,
                                                     "min": min_edad,
                                                     "max": max_edad,
                                                     "desv_std_muestral":
                                                     desv_std_muestral,
                                                     "desv_std_poblacional":
                                                     desv_std_poblacional}
                                           async for carrera, media, mediana,
                                           moda, min_edad, max_edad,
                                           desv_std_muestral,
                                           desv_std_poblacional
                                           in AsyncIteradorEstadisticasEdades(
                                               carreras)}
        print("\nEstadisticas de edades por carrera guardado en archivo: \
'Estadisticas_de_edades_por_carrera.csv'.")
        columnas = ['carrera', 'media_edad', 'mediana_edad', 'moda_edad',
                    'min_edad', 'max_edad', 'desviacion_estandar_muestral',
                    'desviacion_estandar_poblacional']
        with open("Reportes/Estadisticas_de_edades\
_por_carrera.csv", mode='w') as archivo:
            escritor = csv.DictWriter(archivo, delimiter=',',
                                      fieldnames=columnas)
            escritor.writeheader()
            for carrera in estadisticas_edades_por_carrera:
                escritor.writerow({'carrera': carrera,
                                  'media_edad':
                                   estadisticas_edades_por_carrera
                                   [carrera]['media'],
                                   'mediana_edad':
                                   estadisticas_edades_por_carrera
                                   [carrera]['mediana'],
                                   'moda_edad':
                                   estadisticas_edades_por_carrera
                                   [carrera]['moda'],
                                   'min_edad':
                                   estadisticas_edades_por_carrera
                                   [carrera]['min'],
                                   'max_edad':
                                   estadisticas_edades_por_carrera
                                   [carrera]['max'],
                                   'desviacion_estandar_muestral':
                                   estadisticas_edades_por_carrera
                                   [carrera]['desv_std_muestral'],
                                   'desviacion_estandar_poblacional':
                                   estadisticas_edades_por_carrera
                                   [carrera]
                                   ['desv_std_poblacional']})
