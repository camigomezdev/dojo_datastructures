# -*- coding: utf-8 -*-
import csv
import os
from typing import List
from ClassEstudiantes import Estudiantes

opciones = [1, 2, 3, 4, 5, 6, 7, 8, 9]
option = 1


with open('data.csv') as file:
    csv_reader = csv.DictReader(file, delimiter=',')
    datos = list(csv_reader)

    keys = csv_reader.fieldnames
    estudiantes = Estudiantes(datos=datos)

    while option in opciones:
        print("Menu de opciones:")
        print(f"1) Obtener todos los estudiantes que pertenezcan a una ciudad dada.")
        print(f"2) Obtener todos los estudiantes que vivan en un país dado.")
        print(
            f"3) Obtener todos los estudiantes que estén dentro del rango de edades dado.")
        print(f"4) Obtener todas las ciudades de residencia de los estudiantes.")
        print(f"5) Identificar la edad promedio por carrera.")
        print(f"6) Indicar por carrera si el estudiante está por encima o por debajo del promedio de edad.")
        print(f"7) Agrupa los estudiantes en diferentes rangos de edad (18-25, 26-35, mayores de 35).")
        print(f"8) Identifica la ciudad que tienen la mayor variedad de carreras universitarias entre los estudiantes.")
        print(f"0) Salir.\n")

        # Obtener todos los estudiantes que pertenezcan a una ciudad dada.
        option = int(input(f"Elija una opción: "))
        if option == 1:
            print(f"Las ciudades son: {estudiantes.get_ciudades()}")
            ciudad = input("Escriba una ciudad: ")
            print(estudiantes.get_estudiantes_por_ciudad(ciudad=ciudad))
        
        # Obtener todos los estudiantes que vivan en un país dado.
        elif option == 2:
            print(f"Los paises son: {estudiantes.get_paises()}")
            pais = input("Escriba un pais: ")
            print(estudiantes.get_estudiantes_por_pais(pais=pais))

        # Obtener todos los estudiantes que estén dentro del rango de edades dado.
        elif option == 3:
            edad_inicial = int(input("Escriba un rango de edad inicial: "))
            edad_final = int(input("Escriba un rango de edad final: "))
            print(
                f"Estudiantes por el rango seleccionado son: \n{estudiantes.get_estudiantes_por_edad(edad_inicial=edad_inicial,edad_final=edad_final)}")

        # Obtener todas las ciudades de residencia de los estudiantes.
        elif option == 4:
            print(
                f"Las ciudades de residencia son: {estudiantes.get_ciudades()}")

        # Identificar la edad promedio por carrera.
        elif option == 5:
            print(f"Las carreras son: {estudiantes.get_carreras()}")
            carrera = input("Selecciones una carrera: ")
            print(
                f" La edad promedio para la carrera {carrera} es: \n {estudiantes.get_edad_promedio_por_carrera(carrera=carrera)}")

        # Indicar por carrera si el estudiante está por encima o por debajo del promedio de edad.

        # Agrupa los estudiantes en diferentes rangos de edad (18-25, 26-35, mayores de 35).
        
        # Identifica la ciudad que tienen la mayor variedad de carreras universitarias entre los estudiantes.
        os.system('pause')
        os.system('cls')
