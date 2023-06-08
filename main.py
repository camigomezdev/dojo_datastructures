from functions import almacenar_datos, filtro_por_ciudad, filtro_por_pais, mostrar_datos_rango_edades, mostrar_todas_ciudades, promedio_de_edad_por_carrera, estado_estudiante_promedio_edad


def mostrar_menu():
    print("----- MENU -----")
    print("1. Mostrar estudiantes que pertenezcan a una ciudad dada")
    print("2. Mostrar estudiantes que viven en un pais dado")
    print("3. Mostrar datos por rango de edad dado")
    print("4. Mostrar todas las ciudades")
    print("5. Mostrar la edad promedio por carrera")
    print("6. Mostrar si el estudiante es < o > de la edad promedio por carrera")
    print("9. Salir")


datos = almacenar_datos('data.csv')

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        ciudad = (input("Ingrese la ciudad deseada: "))
        filtro_por_ciudad(datos, ciudad)
    if opcion == "2":
        pais = (input("Ingrese el pais deseado: "))
        filtro_por_pais(datos, pais)
    elif opcion == "3":
        edad_min = int(input("Ingrese la edad mínima del rango: "))
        edad_max = int(input("Ingrese la edad máxima del rango: "))
        mostrar_datos_rango_edades(datos, edad_min, edad_max)
    elif opcion == "4":
        mostrar_todas_ciudades(datos)
    elif opcion == "5":
        carrera = (input("Ingrese la carrera deseada: "))
        promedio = promedio_de_edad_por_carrera(datos, carrera)
        print(promedio)
    elif opcion == "6":
        carrera = (input("Ingrese la carrera deseada: "))
        estado_estudiante_promedio_edad(datos, carrera)
    elif opcion == "9":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
