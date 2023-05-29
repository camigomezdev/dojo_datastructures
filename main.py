"""
Dojo Estructuras de datos avanzados
"""

import sys
import asyncio
from estudiantes import Estudiantes

if len(sys.argv) < 2:
    print("\n¡Error! Parámetro faltante.")
    print("\nUso: python3 main.py <nombre de archivo>.csv\n")
else:
    es = Estudiantes(sys.argv[1])
    opcion = ""
    while opcion != 'q':
        print("1) Estudiantes que pertenezcan a una ciudad X.")
        print("2) Estudiantes que vivan en un país X.")
        print("3) Estudiantes que estén dentro de un rango de edad X-Y.")
        print("4) Obtener todas las ciudades de residencia de los estudian\
tes.")
        print("5) Edad promedio por carrera.")
        print("6) Estudiantes arriba o debajo del promedio de edad.")
        print("7) Estudiantes por rangos de edad (18-25, 26-35, mayores de \
35).")
        print("8) Ciudad(es) con la mayor variedad de carreras universitarias \
entre los estudiantes.")
        print("9) Estadísticas de edades por carrera.")
        print("10) Estadísticas de dedades globales.")
        print("q) Salir")
        opcion = ""
        while opcion != "q" and (not opcion.isdecimal()
                                 or int(opcion) > 10 or int(opcion) < 1):
            opcion = input("\nElige una opción del 1 al 10: ")
        match opcion:
            case "1": es.por_ciudad()
            case "2": es.por_pais()
            case "3": es.por_rango_de_edad()
            case "4": es.ciudades_de_residencia()
            case "5": es.edad_promedio_por_carrera(escribir_archivo=True)
            case "6": es.arriba_debajo_promedio_de_edad()
            case "7": es.por_rangos_de_edad()
            case "8": es.ciudad_max_carreras()
            case "9": asyncio.run(es.async_estadisticas_edad_por_carrera())
            case "10": asyncio.run(es.async_estadisticas_edad_global())
        if opcion != "q":
            input("\nPresiona Enter para regresar al menú...\n")
