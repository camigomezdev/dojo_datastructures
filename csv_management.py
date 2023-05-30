"""_summary_

Returns:
    _type_: _description_
"""
import csv
import dataclasses
from pydantic import BaseModel, Field, constr
from typing import List, Optional


class Student(BaseModel):
    """ Estos son los atributos asociados a un estudiante
    """
    first_name: constr(to_lower=True) = Field(alias='nombre')
    last_name: constr(to_lower=True) = Field(alias='apellido')
    city: constr(to_lower=True) = Field(alias='ciudad')
    country: constr(to_lower=True) = Field(alias='pais')
    age: int = Field(alias='edad')
    career: constr(to_lower=True) = Field(alias='carrera')


@dataclasses.dataclass
class CsvManagement:
    """Clase para manejar todo lo relacionado a la informacion del CSV.
    """
    file_name: str

    def __post_init__(self) -> Optional[List[Student]]:
        with open(self.file_name, newline='', encoding='UTF-8') as f:
            csv_info = csv.DictReader(f)
            self.list_of_students = [Student(**row) for row in csv_info]

    def get_student_by_name(self, student_name: str) -> Optional[Student]:
        """ Metodo para buscar un estudiante por su nombre

        Args:
            student_name (str): Nombre del estudiante

        Returns:
            Optional[Student]: Toda la informacion relacionada al estudiante
        """
        for student in self.list_of_students:
            if student.first_name == student_name.lower():
                return student

        return None

    def get_students_by_city(self, city: str) -> Optional[List[Student]]:
        """Metodo para buscar los estudiantes de una ciudad

        Args:
            city (str): Nombre de la ciudad

        Returns:
            Optional[List[Student]]: Lista de estudiantes asociada a una ciudad
        """
        return [
            student.first_name.capitalize()
            for student in self.list_of_students
            if student.city == city.lower()
        ]

    def get_students_by_country(self, country: str) -> Optional[List[Student]]:
        """Metodo para buscar los estudiantes de un pais

        Args:
            country (str): Nombre del pais

        Returns:
            Optional[List[Student]]: Lista de estudiantes asociada a un pais
        """
        return [
            student.first_name.capitalize()
            for student in self.list_of_students
            if student.country == country.lower()
        ]

    def get_students_by_age_range(
            self,
            min_age: int,
            max_age: int
    ) -> Optional[List[Student]]:
        """Metodo para obtener la lista de estudiantes de un rango de edades

        Args:
            min_age (int): Edad minima
            max_age (int): Edad maxima

        Returns:
            Optional[List[Student]]: Lista de estudiantes de determinado rango 
            de edades
        """
        return [
            student.first_name.capitalize()
            for student in self.list_of_students
            if min_age >= student.age <= max_age
        ]

    def get_cities(self) -> Optional[List[str]]:
        """Metodo para obtener todas las ciudades

        Returns:
            Optional[set[str]]: Set con el nombre de las ciudades
        """
        return set(
            student.city.title() for student in self.list_of_students
        )

    def get_average_age_by_career(
            self,
            career: str
    ) -> int:
        """Metodo para obtener promedio de edad por carrera

        Args:
            career (str): Nombre de la carrera

        Returns:
            int: Promedio
        """
        list_students_by_career = [student.age
                                   for student in self.list_of_students
                                   if student.career == career.lower()]
        if list_students_by_career:
            return (sum(age for age in list_students_by_career) /
                    len(list_students_by_career))
        return 0

    def get_student_is_below_or_above_by_career_average_age(
            self,
            student_name: str
    ) -> str:
        """_summary_

        Args:
            student_name (str): _description_

        Returns:
            str: _description_
        """
        student = self.get_student_by_name(student_name)
        if student:
            career_average = self.get_average_age_by_career(student.career)

            if student.age > career_average:
                return f'El estudiante {student.first_name.title()} esta sobre el promedio'

            return f'El estudiante {student.first_name.title()} esta por debajo del promedio'

        return f'El estudiante {student_name} no existe!!!'

    def sort_students_by_age(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        age_groups = {
            '18-25': [],
            '26-35': [],
            '35+': []
        }

        for student in self.list_of_students:
            group = None

            if 18 <= student.age <= 25:
                group = '18-25'
            elif 26 <= student.age <= 35:
                group = '26-35'
            else:
                group = '35+'

            age_groups[group].append(student.first_name.capitalize())

        return age_groups

    def get_city_with_most_careers(self) -> str:
        """_summary_

        Returns:
            _type_: _description_
        """
        careers_by_city = {}

        for student in self.list_of_students:
            city = student.city.title()
            career = student.career.title()

            if city not in careers_by_city:
                careers_by_city[city] = set()

            careers_by_city[city].add(career)

        city_with_most_careers = None
        max_quantity = 0

        for city, careers in careers_by_city.items():
            quantity = len(careers)
            if quantity > max_quantity:
                max_quantity = quantity
                city_with_most_careers = city

        return city_with_most_careers
