"""
A module for group reports in the reports package.
"""
import logging
from typing import Any

from core.decorators import with_logging
from processing.utils import count_by_group
from reports.reports import write_report

logger: logging.Logger = logging.getLogger(__name__)


@with_logging
def generate_group_report(
        students: list[dict[str, Any]], group_key: str, count_key: str,
        report_file: str, header: list[str]
) -> None:
    """
    Generate a report based on the grouping and count of specific keys.
    :param students: The list of student data
    :type students: list[dict[str, Any]]
    :param group_key: The key to group data by
    :type group_key: str
    :param count_key: The key to count occurrences of
    :type count_key: str
    :param report_file: The path to the report file
    :type report_file: str
    :param header: The header for the report
    :type header: list[str]
    :return: None
    :rtype: NoneType
    """
    group_counts: dict[str, int] = count_by_group(students, group_key)
    report_data: list[dict[str, Any]] = [
        {group_key: group, count_key: count} for group, count in
        group_counts.items()]
    write_report(report_data, report_file, header)
    logger.info("Generated %s report", group_key)


@with_logging
def generate_cities_report(students: list[dict[str, Any]]) -> None:
    """
    Generate the cities report.
    :param students: The list of students
    :type students: list[dict[str, Any]]
    :return: None
    :rtype: NoneType
    """
    generate_group_report(
        students, "ciudad", "numero_estudiantes",
        "data/processed/cities_report.csv", ["ciudad", "numero_estudiantes"])


@with_logging
def generate_age_group_report(students: list[dict[str, Any]]) -> None:
    """
    Generate the age group report.
    :param students: The list of students
    :type students: list[dict[str, Any]]
    :return: None
    :rtype: NoneType
    """
    generate_group_report(
        students, "grupo_edad", "numero_estudiantes",
        "data/processed/age_group_report.csv",
        ["grupo_edad", "numero_estudiantes"])
