"""
A module for submenu reports in the reports package.
"""
import logging
from typing import Any

from core.decorators import with_logging
from processing.utils import filter_students, get_unique_values
from reports.reports import write_report
from reports.utils import get_user_choice_from_submenu

logger: logging.Logger = logging.getLogger(__name__)


def generate_submenu_report(
        students: list[dict[str, Any]], key: str, report_file: str
) -> None:
    """
    Generate a report using a submenu based on a specified key.
    :param students: The list of student data
    :type students: list[dict[str, Any]]
    :param key: The key to filter data by
    :type key: str
    :param report_file: The path to the report file
    :type report_file: str
    :return: None
    :rtype: NoneType
    """
    unique_values: list[str] = get_unique_values(students, key)
    choice: str = get_user_choice_from_submenu(
        f"Select a {key}:", unique_values)
    if choice != "0":
        selected_value: str = unique_values[int(choice) - 1]
        write_report(
            list(filter_students(students, key, selected_value)),
            report_file
        )
        logger.info("Generated %s report", selected_value)


@with_logging
def generate_city_report(students: list[dict[str, Any]]) -> None:
    """
    Generate the city report.
    :param students: The list of students
    :type students: list[dict[str, Any]]
    :return: None
    :rtype: NoneType
    """
    generate_submenu_report(
        students, "ciudad", "data/processed/city_report.csv")


@with_logging
def generate_country_report(students: list[dict[str, Any]]) -> None:
    """
    Generate the country report.
    :param students: The list of students
    :type students: list[dict[str, Any]]
    :return: None
    :rtype: NoneType
    """
    generate_submenu_report(
        students, "pais", "data/processed/country_report.csv")


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
