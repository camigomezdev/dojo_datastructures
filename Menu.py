from utils import get_csv_data


class Menu:
    """
    Define un objeto menú que se despliega al usuario para obtener distintos
    datos a partir del csv asignado
    """
    def __init__(self, data_path) -> None:
        print("Bienvenido al menú!")
        self.user_data_list = get_csv_data(data_path)
        self.ciudades = set([linea["ciudad"] for linea in self.user_data_list])
        self.paises = set([linea["pais"] for linea in self.user_data_list])
        self.edades = set([linea["edad"] for linea in self.user_data_list])
        self.carreras = set(
            [linea["carrera"] for linea in self.user_data_list])
        self.reports_path = "./reports"

    def obt_dict_alum(self, cat: int) -> dict:
        """
        Función que retorna un diccionario con información de los alumnos
        ordenados por cada categoría. Ejemplo: si recibe el argumento cat con
        valor de 4, retornaría un diccionario con los alumnos ordenados por
        cada ciudad en una lista:
        {
            Art History: [{"nombre": ...}]
        }
        [cat: int]: un número del 1 al 4 que determina la llave y la
        información con la que se va a iterar.
        """

        informacion: set
        llave: str

        if cat == 1:
            informacion = self.ciudades
            llave = "ciudad"
        elif cat == 2:
            informacion = self.paises
            llave = "pais"
        elif cat == 3:
            informacion = self.edades
            llave = "edad"
        else:
            informacion = self.carreras
            llave = "carrera"

        cant_alumnos = {
            categoria: [alumno for alumno in self.user_data_list
                        if alumno[llave] == categoria]
            for categoria in sorted(informacion)
        }

        return cant_alumnos

    def cant_alum_por(self, llave: str, categoria: int):
        titulo = f"La cantidad de alumnos por {llave} es:"
        alumnos = self.obt_dict_alum(categoria)
        print(titulo)

        with open(f"{self.reports_path}/alumnos por {llave}.txt", "w") \
                as report:
            report.write(titulo + "\n")
            for key, value in alumnos.items():
                cantidad = len(value)
                print("{}: {}".format(key, cantidad))
                report.write("{}: {}\n".format(key, cantidad))

    def alum_por_edad(self, inicio: int, final: int, categoria: int) -> None:
        titulo = "Los alumnos dentro el rango de edad de " + \
                f"{inicio} a {final} años son:"
        alumnos = self.obt_dict_alum(categoria)

        print(titulo)

        with open(f"{self.reports_path}/alumnos por rango de edad de {inicio}"
                  + "a {final}.txt", "w") as report:
            report.write(titulo + "\n")
            for key, value in alumnos.items():
                if int(key) >= inicio and int(key) <= final:
                    print("{}: {}".format(key, value))
                    report.write("{}: {}\n".format(key, value))

    def ciudades_alum(self, categoria: int):
        titulo = "Las ciudades de residencia de los estudiantes son:"
        alumnos = self.obt_dict_alum(categoria)
        print(titulo)

        with open(f"{self.reports_path}/ciudades de residencia.txt", "w") \
                as report:
            report.write(titulo + "\n")
            for key, value in alumnos.items():
                print("-{}".format(key))
                report.write("-{}\n".format(key))

    def get_prom_x_carrera(self) -> dict:
        alumnos = self.obt_dict_alum(4)
        promedios = {}

        for key, value in alumnos.items():
            sum = 0
            for alumno in value:
                sum += int(alumno["edad"])
            promedios[key] = sum // len(value)

        return promedios

    def guardar_promedio_carrera(self):
        titulo = "El promedio de edad por carrera es:"
        print(titulo)
        promedios = self.get_prom_x_carrera()

        with open(f"{self.reports_path}/Edad promedio por carrera.txt",
                  "w") as report:
            report.write(titulo + "\n")
            for key, value in promedios.items():
                print(f"{key}: {value}")
                report.write(f"{key}: {value}\n")

    def alumno_vs_promedio(self):
        titulo = "Alumnos encima o debajo del promedio de edad de la carrera:"
        promedios = self.get_prom_x_carrera()

        with open(f"{self.reports_path}/alumnos vs promedio.txt",
                  "w") as report:
            print(titulo)
            report.write(f"{titulo}\n")

            for carrera in self.carreras:
                report.write(f"{carrera}:\n")
                for alumno in self.user_data_list:
                    if carrera == alumno["carrera"]:
                        string = "{}, {}: ".format(
                                alumno['apellido'], alumno['nombre'])
                        if int(promedios[carrera]) > int(alumno["edad"]):
                            print(string + "Mayor")
                            report.write(string + "Mayor\n")
                        elif int(promedios[carrera]) < int(alumno["edad"]):
                            print(string + "Menor")
                            report.write(string + "Menor\n")
                    else:
                        continue

    def alum_rango_edad(self):
        titulo = "Alumnos por rango de edad:"
        grupo_18_25 = []
        grupo_26_35 = []
        grupo_35_plus = []

        print(titulo)
        for alumno in self.user_data_list:
            edad = int(alumno["edad"])
            if edad >= 18 and edad <= 25:
                grupo_18_25.append("{}, {}".format(
                    alumno["apellido"], alumno["nombre"]))
            elif edad >= 26 and edad <= 35:
                grupo_26_35.append("{}, {}".format(
                    alumno["apellido"], alumno["nombre"]))
            elif edad >= 35:
                grupo_35_plus.append("{}, {}".format(
                    alumno["apellido"], alumno["nombre"]))

        with open(f"{self.reports_path}/alumnos por rango de edad.txt",
                  "w") as report:
            report.write(f"{titulo}\n")
            print("Alumnos de 18 a 25 años:")

            report.write("Alumnos de 18 a 25 años:\n")
            for alumno in grupo_18_25:
                print(alumno)
                report.write(f"{alumno}\n")

            print("Alumnos de 26 a 35 años:")
            report.write("Alumnos de 26 a 35 años:\n")
            for alumno in grupo_26_35:
                print(alumno)
                report.write(f"{alumno}\n")

            print("Alumnos mayores a 35 años:")
            report.write("Alumnos mayores a 35 años:\n")
            for alumno in grupo_35_plus:
                print(alumno)
                report.write(f"{alumno}\n")

    def cd_mas_carreras(self):
        titulo = "Ciudades con más carreras:"
        cant_carr_cd = {ciudad: len(set(
            alumno["carrera"]
            for alumno in self.user_data_list
            if ciudad == alumno["ciudad"]))
            for ciudad in self.ciudades
        }

        with open(f"{self.reports_path}/ciudades con mas carreras.txt",
                  "w") as report:
            print(titulo)
            report.write(f"{titulo}\n")
            for key, value in cant_carr_cd.items():
                print(f"{key}: {value}")
                report.write(f"{key}: {value}\n")

    def run_menu(self):
        usr_input = ""
        while usr_input != "q":
            usr_input = input("""
            Escoge una opción:
            1. Obtener todos los estudiantes que pertenezcan a una ciudad dada.
            2. Obtener todos los estudiantes que vivan en un país dado.
            3. Obtener todos los estudiantes que estén dentro del rango de edades dado.
            4. Obtener todas las ciudades de residencia de los estudiantes.
            5. Identificar la edad promedio por carrera.
            6. Indicar por carrera si el estudiante está por encima o por debajo del promedio de edad.
            7. Agrupa los estudiantes en diferentes rangos de edad (18-25, 26-35, mayores de 35).
            8. Identifica la ciudad que tienen la mayor variedad de carreras universitarias entre los estudiantes.
            q. Salir
            Selección: """)
            try:
                if int(usr_input) == 1:
                    self.cant_alum_por("ciudad", 1)
                elif int(usr_input) == 2:
                    self.cant_alum_por("pais", 2)
                elif int(usr_input) == 3:
                    inicio = int(input("Introduzca el inicio del rango: "))
                    final = int(input("Introduzca el final del rango: "))
                    self.alum_por_edad(inicio, final, 3)
                elif int(usr_input) == 4:
                    self.ciudades_alum(1)
                elif int(usr_input) == 5:
                    self.guardar_promedio_carrera()
                elif int(usr_input) == 6:
                    self.alumno_vs_promedio()
                elif int(usr_input) == 7:
                    self.alum_rango_edad()
                elif int(usr_input) == 8:
                    self.cd_mas_carreras()
                else:
                    print("Introduzca un número del 1 al 8, o q para salir.")
            except:
                print("Introduzca un número del 1 al 8, o q para salir.")
