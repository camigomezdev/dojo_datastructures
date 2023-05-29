import csv
from pathlib import Path
import random


class CSVParser:
    MENU_OPTIONS = [
        {
            "option": 1,
            "description": "Obtener todos los estudiantes que pertenezcan a una ciudad.",
        },
        {
            "option": 2,
            "description": "Obtener todos los estudiantes que vivan en un país.",
        },
        {
            "option": 3,
            "description": "Obtener todos los estudiantes que estén dentro del rango de edades dado.",
        },
        {
            "option": 4,
            "description": "Obtener todas las ciudades de residencia de los estudiantes.",
        },
        {"option": 5, "description": "Identificar la edad promedio por carrera."},
        {
            "option": 6,
            "description": "Indicar por carrera si el estudiante está por encima o por debajo del promedio de edad.",
        },
        {
            "option": 7,
            "description": "Agrupa los estudiantes en diferentes rangos de edad (18-25, 26-35, mayores de 35).",
        },
        {
            "option": 8,
            "description": "Identifica la ciudad que tienen la mayor variedad de carreras universitarias entre los estudiantes.",
        },
    ]

    def __init__(self):
        self.data = []
        self.user_selection = None
        self.career_average = []

    def read_csv(self):
        file = Path(__file__).with_name("data.csv")
        with file.open("r") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                self.data.append(row)

    def user_menu(self):
        print("Bienvenido, para detener la ejecucion solo precio CTRL + C 🚀\n ")
        print("👾 Selecciona una opcion para continuar 👉")
        print("-----------------------------------")
        for index, method in enumerate(self.MENU_OPTIONS):
            print(f'{method["option"]}. {method["description"]}')

    def extra_menu_options(self):
        """
        match function is only available on python 3.10.
        Before run this code, make sure you are running an enviroment with python 3.10
        """
        self.user_selection = int(input("Tu opcion: "))
        match self.user_selection:
            case 1:
                cities = [obj["ciudad"] for obj in self.data]
                duplicates = set([city for city in cities if cities.count(city) > 1])
                print(duplicates)
                city = input("Escribe el nombre de la ciudad para continuar: 👉 ")
                city_selected = [obj for obj in self.data if obj["ciudad"] == city]

                self.write_to_csv(f"Estudiantes_{city}", city_selected)

            case 2:
                countries = [obj["pais"] for obj in self.data]
                duplicates = set(
                    [country for country in countries if countries.count(country) > 1]
                )
                print(duplicates)
                country = input("Escribe el nombre del pais para continuar: 👉 ")
                country_selected = [obj for obj in self.data if obj["pais"] == country]

                self.write_to_csv(f"Estudiantes_de_{country}", country_selected)

            case 3:
                age = input("Escribe el rango de edad para continuar: 👉 ")
                age_selected = [obj for obj in self.data if obj["edad"] == age]

                self.write_to_csv(f"Estudiantes_{age}", age_selected)

            case 4:
                cities = [obj["ciudad"] for obj in self.data]
                duplicates = set([city for city in cities if cities.count(city) > 1])
                data = []
                [data.append({"ciudad": i}) for i in duplicates]

                self.write_to_csv("Ciudades", data)

            case 5:
                careers = {}
                data = []
                [
                    careers.__setitem__(obj["carrera"], [int(obj["edad"])])
                    if obj["carrera"] not in careers
                    else careers[obj["carrera"]].append(int(obj["edad"]))
                    for obj in self.data
                ]

                [
                    data.append(
                        {"carrera": career, "edad_promedio": sum(ages) / len(ages)}
                    )
                    for career, ages in careers.items()
                ]

                self.career_average.append(data)
                self.write_to_csv("Edad_promedio", data)

            case 6:
                data = []
                students = [
                    {
                        "nombre": obj["nombre"],
                        "apellido": obj["apellido"],
                        "edad": obj["edad"],
                        "carrera": obj["carrera"],
                    }
                    for obj in self.data
                ]

                if len(self.career_average) == 0:
                    return print(
                        "\n\n Primero necesitas correr la opcion 5 para obtener el promedio de edad por carrera \n\n"
                    )

                [
                    data.append(
                        {
                            "nombre": student["nombre"],
                            "apellido": student["apellido"],
                            "edad": student["edad"],
                            "carrera": student["carrera"],
                            "edad_promedio": list(
                                filter(
                                    lambda x: x["carrera"] == student["carrera"],
                                    self.career_average[0],
                                )
                            )[0]["edad_promedio"],
                            "status": "mayor"
                            if int(student["edad"])
                            > list(
                                filter(
                                    lambda x: x["carrera"] == student["carrera"],
                                    self.career_average[0],
                                )
                            )[0]["edad_promedio"]
                            else "menor",
                        }
                    )
                    for student in students
                ]

                self.write_to_csv("Edad_promedio_total", data)

            case 7:
                results = []
                group_selected = int(
                    input(
                        "Selecciona el rango de edad: \n 1. 18-25 \n 2. 26-35 \n 3. mayores de 35 \n "
                    )
                )

                if group_selected == 1:
                    results = [obj for obj in self.data if 18 <= int(obj["edad"]) <= 25]
                elif group_selected == 2:
                    results = [obj for obj in self.data if 26 <= int(obj["edad"]) <= 35]
                elif group_selected == 3:
                    results = [obj for obj in self.data if int(obj["edad"]) > 35]

                self.write_to_csv("Rango_edad", results)

            case 8:
                cities_with_most_careers = {}
                data = []
                cities = [obj["ciudad"] for obj in self.data]
                duplicates = set([city for city in cities if cities.count(city) > 1])
                careers = [obj["carrera"] for obj in self.data]

                # for obj in self.data:
                #     if obj["ciudad"] not in cities_with_most_careers:
                #         cities_with_most_careers[obj["ciudad"]] = [obj["carrera"]]
                #     else:
                #         cities_with_most_careers[obj["ciudad"]].append(obj["carrera"])

                [
                    cities_with_most_careers.__setitem__(
                        obj["ciudad"], [obj["carrera"]]
                    )
                    if obj["ciudad"] not in cities_with_most_careers
                    else cities_with_most_careers[obj["ciudad"]].append(obj["carrera"])
                    for obj in self.data
                ]

                [
                    data.append({"ciudad": city, "carreras": len(set(careers))})
                    for city, careers in cities_with_most_careers.items()
                    if city in duplicates
                ]

                self.write_to_csv("Carreras_ciudad", data)

            case _:
                print("Opcion no valida")

    def write_to_csv(self, title, data):
        with open(f"media/{title}_{random.random()}.csv", "w", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        print("Archivo creado con exito! 🎉 Busca en el folder de media")
