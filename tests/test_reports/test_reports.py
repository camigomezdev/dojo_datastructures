"""
A module for test reports in the tests.test_reports package.
"""
import csv
import os
from pathlib import Path
from typing import Any

from reports.reports import write_report


def test_write_report(tmpdir: Path) -> None:
    """
    Test case for write_report function
    :param tmpdir: The temporary directory to write report
    :type tmpdir: Path
    :return: None
    :rtype: NoneType
    """
    students:  list[dict[str, Any]] = [
        {
            "nombre": "John",
            "apellido": "Doe",
            "ciudad": "New York",
            "pais": "USA",
            "edad": 25,
            "carrera": "Computer Science",
        },
        {
            "nombre": "Jane",
            "apellido": "Smith",
            "ciudad": "Los Angeles",
            "pais": "USA",
            "edad": 27,
            "carrera": "Business",
        },
    ]
    report_file: str = os.path.join(tmpdir, "report.csv")

    write_report(students, report_file)

    assert os.path.exists(report_file)

    with open(report_file, "r", encoding="UTF-8") as file:
        reader = csv.reader(file)
        rows: list[list[str]] = list(reader)

        assert rows[0] == [
            "nombre", "apellido", "ciudad", "pais", "edad", "carrera"]
        assert rows[1:] == [
            ["John", "Doe", "New York", "USA", "25", "Computer Science"],
            ["Jane", "Smith", "Los Angeles", "USA", "27", "Business"],
        ]

    os.remove(report_file)
