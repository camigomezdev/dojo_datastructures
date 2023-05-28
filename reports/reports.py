"""
A module for reports in the reports package for file input/output
 functions.
"""
import csv
from typing import Any, Optional

from core.decorators import benchmark
from processing.utils import ENCODING, HEADER


@benchmark
def write_report(
        report_data: list[dict[str, Any]], report_file: str,
        header: Optional[list[str]] = None
) -> None:
    """
    Write a report on student data to a CSV file.
    :param report_data: The data to write report
    :type report_data: list[dict[str, Any]]
    :param report_file: path to the report file
    :type report_file: str
    :param header: The header for the report
    :type header: Optional[list[str]]
    :return: None
    :rtype: NoneType
    """
    if not header:
        header = HEADER
    with open(report_file, "w", encoding=ENCODING, newline="") as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(report_data)
