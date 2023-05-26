"""
This module provides the main command-line interface for the student
 processing program.
"""
import logging
from typing import Any

from core import logging_config
from core.decorators import with_logging
from processing.student import Student
from reports.report_generator import (
    generate_above_below_avg_report,
    generate_age_group_report,
    generate_age_report,
    generate_career_average_report,
    generate_cities_report,
    generate_city_report,
    generate_country_report,
    generate_most_career_city_report,
)
from reports.utils import print_menu

logging_config.setup_logging()
logger: logging.Logger = logging.getLogger(__name__)


@with_logging
def main() -> None:
    """
    The main function that runs the student data program.
    :return: None
    :rtype: NoneType
    """
    student: Student = Student("data/raw/data.csv")
    students: list[dict[str, Any]] = student.load_data()
    while True:
        print_menu()
        choice: str = input("Enter your choice: ")
        match choice:
            case "1":
                generate_city_report(students)
            case "2":
                generate_country_report(students)
            case "3":
                generate_age_report(students)
            case "4":
                generate_cities_report(students)
            case "5":
                generate_career_average_report(students)
            case "6":
                generate_above_below_avg_report(students)
            case "7":
                generate_age_group_report(students)
            case "8":
                generate_most_career_city_report(students)
            case "0":
                break
            case _:
                logger.error("Invalid choice %s. Please try again.\n", choice)
    logger.info("Program exited.")


if __name__ == "__main__":
    main()
