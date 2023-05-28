"""
A module for menu reports in the reports package.
"""
import logging
from typing import Any

from analysis.analysis import city_with_most_careers
from core.decorators import with_logging
from reports.reports import write_report

logger: logging.Logger = logging.getLogger(__name__)


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
