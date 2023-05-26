"""
A module for menu reports in the reports package.
"""
import logging
from typing import Any

from analysis.analysis import (
    career_above_below_avg,
    city_with_most_careers,
    split_into_age_groups,
)
from core.decorators import with_logging
from processing.utils import (
    average_by_group,
    count_by_group,
    filter_students,
    get_unique_values,
)
from reports.reports import write_report
from reports.utils import print_submenu

logger: logging.Logger = logging.getLogger(__name__)


@with_logging
def generate_city_report(students: list[dict[str, Any]]) -> None:
    """
    Generate the city report.
    :param students: The list of students
    :type students: list[dict[str, Any]]
    :return: None
    :rtype: NoneType
    """
    unique_cities: list[str] = get_unique_values(students, "ciudad")
    city_submenu: str = print_submenu("Select a city:", unique_cities)
    if city_submenu != "0":
        selected_city: str = unique_cities[int(city_submenu) - 1]
        write_report(
            list(filter_students(students, "ciudad", selected_city)),
            "data/processed/city_report.csv"
        )
        logger.info("Generated %s report", selected_city)


@with_logging
def generate_country_report(students: list[dict[str, Any]]) -> None:
    """
    Generate the country report.
    :param students: The list of students
    :type students: list[dict[str, Any]]
    :return: None
    :rtype: NoneType
    """
    unique_countries: list[str] = get_unique_values(students, "pais")
    country_submenu: str = print_submenu("Select a country:", unique_countries)
    if country_submenu != "0":
        selected_country: str = unique_countries[int(country_submenu) - 1]
        write_report(
            list(filter_students(
                students, "pais", unique_countries[int(country_submenu) - 1])),
            "data/processed/country_report.csv"
        )
        logger.info("Generated %s report", selected_country)


@with_logging
def generate_age_report(students: list[dict[str, Any]]) -> None:
    """
    Generate the age report.
    :param students: The list of students
    :type students: list[dict[str, Any]]
    :return: None
    :rtype: NoneType
    """
    while True:
        age_submenu: str = input("Enter an age (0 to exit): ")
        if age_submenu == "0":
            break
        try:
            age: int = int(age_submenu)
            if 0 < age <= 120:
                write_report(
                    list(filter_students(students, "edad", age)),
                    "data/processed/age_report.csv"
                )
                logger.info("Generated %s report", age)
                break
            logger.error("Invalid age. Please enter a valid age.\n")
        except ValueError:
            logger.error("Invalid age. Please enter a valid age.\n")


@with_logging
def generate_cities_report(students: list[dict[str, Any]]) -> None:
    """
    Generate the cities report.
    :param students: The list of students
    :type students: list[dict[str, Any]]
    :return: None
    :rtype: NoneType
    """
    city_counts: dict[str, int] = count_by_group(students, "ciudad")
    print(city_counts)
    report_data: list[dict[str, Any]] = [
        {"ciudad": city, "numero_estudiantes": count} for city, count in
        city_counts.items()]
    print(report_data)
    header: list[str] = ["ciudad", "numero_estudiantes"]
    write_report(report_data, "data/processed/cities_report.csv", header)
    logger.info("Generated cities report")


@with_logging
def generate_career_average_report(students: list[dict[str, Any]]) -> None:
    """
    Generate the career average report.
    :param students: The list of students
    :type students: list[dict[str, Any]]
    :return: None
    :rtype: NoneType
    """
    header: list[str] = ["carrera", "edad_promedio"]
    write_report(
        [{"carrera": k, "edad_promedio": v} for k, v in
         average_by_group(students, "carrera", "edad").items()],
        "data/processed/career_average_report.csv", header
    )
    logger.info("Generated career average report")


@with_logging
def generate_above_below_avg_report(students: list[dict[str, Any]]) -> None:
    """
    Generate the above/below average report.
    :param students: The list of students
    :type students: list[dict[str, Any]]
    :return: None
    :rtype: NoneType
    """
    header: list[str] = ["nombre", "status"]
    above_below_avg: dict[str, str] = career_above_below_avg(students)
    write_report(
        [{"nombre": k, "status": v} for k, v in above_below_avg.items()],
        "data/processed/above_below_avg_report.csv", header
    )
    logger.info("Generated age above-below average report")


@with_logging
def generate_age_group_report(students: list[dict[str, Any]]) -> None:
    """
    Generate the age group report.
    :param students: The list of students
    :type students: list[dict[str, Any]]
    :return: None
    :rtype: NoneType
    """
    header: list[str] = ["grupo_edad", "numero_estudiantes"]
    write_report(
        [{"grupo_edad": k, "numero_estudiantes": len(v)} for k, v in
         split_into_age_groups(students).items()],
        "data/processed/age_group_report.csv", header
    )
    logger.info("Generated age groups report")


@with_logging
def generate_most_career_city_report(students: list[dict[str, Any]]) -> None:
    """
    Generate the most career city report.
    :param students:  The list of students
    :type students: list[dict[str, Any]]
    :return: None
    :rtype: NoneType
    """
    most_career_city: str = city_with_most_careers(students)
    header: list[str] = ["ciudad"]
    write_report(
        [{"ciudad": most_career_city}],
        "data/processed/most_career_city_report.csv", header
    )
    logger.info("Generated the city with most career variety career report")
