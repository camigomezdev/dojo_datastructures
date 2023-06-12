class Estudiantes:

    def __init__(self, datos: list):
        self.datos = datos
        self.ciudades = set()
        self.paises = set()
        self.carreras = set()
        self.__set_columnas()


    def __set_columnas(self) -> None:

        for row in self.datos:
            self.ciudades.add(row['ciudad'])
            self.paises.add(row['pais'])
            self.carreras.add(row['carrera'])

    def get_ciudades(self) -> set:
        return self.ciudades

    def get_paises(self) -> str:
        return self.paises

    def get_carreras(self) -> str:
        return self.carreras

    # Obtener todos los estudiantes que pertenezcan a una ciudad dada.
    def get_estudiantes_por_ciudad(self, ciudad: str) -> dict:

        estudiantes_por_ciudad = {f"{row['nombre']} {row['apellido']}": [row['ciudad']]
                                  for row in self.datos if row['ciudad'] == ciudad}

        return estudiantes_por_ciudad

    # Obtener todos los estudiantes que vivan en un país dado.
    def get_estudiantes_por_pais(self, pais: str) -> dict:

        estudiantes_por_pais = {f"{row['nombre']} {row['apellido']}": [row['pais']]
                                for row in self.datos if row['pais'] == pais}

        return estudiantes_por_pais

    # Obtener todos los estudiantes que estén dentro del rango de edades dado.
    def get_estudiantes_por_edad(self, edad_inicial: int, edad_final: int) -> dict:

        estudiantes_por_edad = {f"{row['nombre']} {row['apellido']}": [
            row['edad']] for row in self.datos if int(row['edad']) >= edad_inicial and int(row['edad']) <= edad_final}

        return estudiantes_por_edad if len(estudiantes_por_edad) > 0 else "No existen valores con ese rango"

    # Identificar la edad promedio por carrera.
    def get_edad_promedio_por_carrera(self, carrera: str) -> dict:

        estudiantes_por_carrera = {f"{row['nombre']} {row['apellido']}": [row['edad']]
                                   for row in self.datos if row['carrera'] == carrera}

        carrera_sum = 0

        for estudiantes in estudiantes_por_carrera.values():

            carrera_sum += float(str.join('', estudiantes))

        return (carrera_sum / len(estudiantes_por_carrera)) if carrera_sum > 0 else 0

    # Indicar por carrera si el estudiante está por encima o por debajo del promedio de edad.

    def get_estudiantes_nivel_academico(self, carrera: str) -> dict:
        estudiantes_por_carrera = {f"{row['nombre']} {row['apellido']}": [row['edad']]
                                   for row in self.datos if row['carrera'] == carrera}
        carrera_sum = 0

        for estudiantes in estudiantes_por_carrera.values():
            carrera_sum += float(str.join('', estudiantes))

        edad_promedio = (carrera_sum / len(estudiantes_por_carrera))

        print(f"Edad promedio de la carrera es: {edad_promedio}")
        estudiantes_nivel_academico = {}
        for key, value in estudiantes_por_carrera.items():

            estudiantes_nivel_academico[key] = f"edad: {str.join('', value)} por arriba"
            if edad_promedio > float(str.join('', value)):
                estudiantes_nivel_academico[key] = f"edad: {str.join('', value)} por debajo"

        return estudiantes_nivel_academico

    # Agrupa los estudiantes en diferentes rangos de edad (18-25, 26-35, mayores de 35).
    def get_estudiantes_por_rangos(self) -> list:

        estudiante_primer_rango = {row['nombre']: row['edad'] for row in self.datos if int(
            row['edad']) >= 18 and int(row['edad']) <= 25}
        estudiante_segundo_rango = {row['nombre']: row['edad'] for row in self.datos if int(
            row['edad']) >= 26 and int(row['edad']) <= 35}
        estudiante_tercer_rango = {row['nombre']: row['edad']
                                   for row in self.datos if int(row['edad']) > 35}

        estudiantes_por_rangos = [estudiante_primer_rango,
                                  estudiante_segundo_rango, estudiante_tercer_rango]

        return estudiantes_por_rangos

    # Identifica la ciudad que tienen la mayor variedad de carreras universitarias entre los estudiantes.
    def get_ciudad_mayor_carrera(self) -> dict:

        dict_carrera = {ciudad: list((set(alumno['carrera']
                                          for alumno in self.datos if alumno['ciudad'] in ciudad))) for ciudad in self.ciudades}

        mayor = 0
        for clave, valor in dict_carrera.items():

            print(f"{clave}, {valor}")

            if len(valor) > mayor:

                mayor = len(valor)
                ciudad = clave

        return f"{ciudad} tiene la mayor variedad de carreras {dict_carrera.get(ciudad)}"

    def guardar_datos(self, ruta: str, archivo: str, datos):
        with open(f"{ruta}{archivo}", 'w') as reporte:
            for k, v in datos.items():
                reporte.write(f"{k},{v}\n")

    def guardar_datos_lista(self, ruta: str, archivo: str, datos):
        with open(f"{ruta}{archivo}", 'w') as reporte:
            for _ in datos:
                reporte.write(f"{_}\n")
