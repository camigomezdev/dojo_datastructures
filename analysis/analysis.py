"""
A module for analysis in the analysis package to explore data features.
"""
from typing import Any

from core.decorators import with_logging
from processing.utils import average_by_group


@with_logging
def career_above_below_avg(students: list[dict[str, Any]]) -> dict[str, str]:
    """
    Indicates by career whether the student is above or below the
     average age.
    :param students: The list of students
    :type students: list[dict[str, Any]]
    :return: A dictionary where keys are student's names and values
     indicate if the student's age is above or below the average
    :rtype: dict[str, str]
    """
    career_averages: dict[str, float] = average_by_group(
        students, "carrera", "edad"
    )
    return {student["nombre"]: "above" if student["edad"] > career_averages.get(
        student["carrera"], 0) else "below" for student in students
    }


@with_logging
def split_into_age_groups(
    students: list[dict[str, Any]]
) -> dict[str, list[dict[str, Any]]]:
    """
    Split students into age groups.
    :param students: The list of students
    :type students: list[dict[str, Any]]
    :return: A dictionary where keys are age group names and values are
     lists of students in that age group
    :rtype: dict[str, list[dict[str, Any]]]
    """
    return {
        "18-25": [student for student in students if
                  18 <= student["edad"] <= 25],
        "26-35": [student for student in students if
                  26 <= student["edad"] <= 35],
        "36+": [student for student in students if
                student["edad"] > 35]
    }


@with_logging
def city_with_most_careers(students: list[dict[str, Any]]) -> str:
    """
    Identifies the city with the greatest variety of university careers
     among the students.
    :param students: The list of students
    :type students: list[dict[str, Any]]
    :return: The name of the city with the unique careers
    :rtype: str
    """
    city_career_counts: dict[str, set[str]] = {
        city: {student["carrera"] for student in students if
               student["ciudad"] == city} for city in
        set(student["ciudad"] for student in students)
    }
    max_city: str = max(
        city_career_counts, key=lambda city: len(city_career_counts[city]))
    return max_city
