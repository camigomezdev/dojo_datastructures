"""
A module for average reports in the reports package.
"""
import logging
from typing import Any

from analysis.analysis import career_above_below_avg
from core.decorators import with_logging
from processing.utils import average_by_group
from reports.reports import write_report

logger: logging.Logger = logging.getLogger(__name__)


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
