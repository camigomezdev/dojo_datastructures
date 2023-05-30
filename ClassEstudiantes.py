# -*- coding: utf-8 -*-
import csv


class Estudiantes:

    def __init__(self, datos: list):
        self.datos = datos
        self.ciudades = set()
        self.paises = set()
        self.carreras = set()
        self.__set_columnas()

    # Obtener todas las ciudades

    def __set_columnas(self) -> None:

        for row in self.datos:
            self.ciudades.add(row['ciudad'])
            self.paises.add(row['pais'])
            self.carreras.add(row['carrera'])

    def get_ciudades(self) -> str:

        ciudades = [ciudad for ciudad in self.ciudades]

        return str.join(', ', ciudades)

    def get_paises(self) -> str:

        paises = [pais for pais in self.paises]

        return str.join(', ', paises)

    def get_carreras(self) -> str:

        carreras = [carrera for carrera in self.carreras]

        return str.join(', ', carreras)

    # Obtener todos los estudiantes que pertenezcan a una ciudad dada.
    def get_estudiantes_por_ciudad(self, ciudad: str) -> dict:

        estudiantes_por_ciudad = {row['nombre']: [row['ciudad']]
                                  for row in self.datos if row['ciudad'] == ciudad}

        return estudiantes_por_ciudad

    # Obtener todos los estudiantes que vivan en un país dado.
    def get_estudiantes_por_pais(self, pais: str) -> dict:

        estudiantes_por_pais = {row['nombre']: [row['pais']]
                                for row in self.datos if row['pais'] == pais}

        return estudiantes_por_pais

    # Obtener todos los estudiantes que estén dentro del rango de edades dado.
    def get_estudiantes_por_edad(self, edad_inicial: int, edad_final: int) -> dict:

        estudiantes_por_edad = {row['nombre']: [
            row['edad']] for row in self.datos if int(row['edad']) >= edad_inicial and int(row['edad']) <= edad_final}

        return estudiantes_por_edad if len(estudiantes_por_edad) > 0 else "No existen valores con ese rango"

    # Identificar la edad promedio por carrera.
    def get_edad_promedio_por_carrera(self, carrera: str) -> dict:

        estudiantes_por_carrera = {row['nombre']: [row['edad']]
                                   for row in self.datos if row['carrera'] == carrera}

        carrera_sum = 0

        for estudiantes in estudiantes_por_carrera.values():

            carrera_sum += float(str.join('', estudiantes))

        return (carrera_sum / len(estudiantes_por_carrera)) if carrera_sum > 0 else 0

    # Indicar por carrera si el estudiante está por encima o por debajo del promedio de edad.

    def get_nivel_estudiante(Self, carrera: str, estudiante: str) -> list:
        pass

    # Agrupa los estudiantes en diferentes rangos de edad (18-25, 26-35, mayores de 35).
    def get_agrupar_estudiantes_por_edad(self, estudiantes: list) -> list:
        pass

    # Identifica la ciudad que tienen la mayor variedad de carreras universitarias entre los estudiantes.
    def get_ciudad_variedad_carreraras(self) -> str:
        pass
