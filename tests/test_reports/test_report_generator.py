"""
A module for test report generator in the tests.test_reports package.
"""
import os
from pathlib import Path
from typing import Any

import pytest
from pytest import MonkeyPatch

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

students: list[dict[str, Any]] = [
    {"nombre": "John", "apellido": "Doe", "ciudad": "New York",
     "pais": "USA", "edad": 25, "carrera": "Computer Science"},
    {"nombre": "Jane", "apellido": "Smith", "ciudad": "Los Angeles",
     "pais": "USA", "edad": 27, "carrera": "Business"},
]


def test_generate_city_report(tmpdir: Path) -> None:
    """
    Test case for generate_city_report function
    :param tmpdir: The temporary directory to generate the report
    :type tmpdir: Path
    :return: None
    :rtype: NoneType
    """
    report_file: str = os.path.join(tmpdir, "city_report.csv")
    print_submenu_input = "1\n0"

    with pytest.raises(SystemExit):
        with pytest.raises(FileNotFoundError):
            generate_city_report(students)

    monkeypatch: MonkeyPatch = MonkeyPatch()
    monkeypatch.setattr(
        "builtins.input", lambda _: print_submenu_input)  # type: ignore

    generate_city_report(students)

    assert os.path.exists(report_file)

    os.remove(report_file)


def test_generate_country_report(tmpdir: Path) -> None:
    """
    Test case for generate_country_report function
    :param tmpdir: The temporary directory to generate the report
    :type tmpdir: Path
    :return: None
    :rtype: NoneType
    """
    report_file: str = os.path.join(tmpdir, "country_report.csv")
    print_submenu_input = "1\n0"

    with pytest.raises(SystemExit):
        with pytest.raises(FileNotFoundError):
            generate_country_report(students)

    monkeypatch: MonkeyPatch = MonkeyPatch()
    monkeypatch.setattr(
        "builtins.input", lambda _: print_submenu_input)  # type: ignore

    generate_country_report(students)

    assert os.path.exists(report_file)

    os.remove(report_file)


def test_generate_age_report(tmpdir: Path) -> None:
    """
    Test case for generate_age_report function
    :param tmpdir: The temporary directory to generate the report
    :type tmpdir: Path
    :return: None
    :rtype: NoneType
    """
    report_file: str = os.path.join(tmpdir, "age_report.csv")
    age_input = "25\n0"  # Enter an age of 25, then exit

    with pytest.raises(SystemExit):
        with pytest.raises(FileNotFoundError):
            generate_age_report(students)

    monkeypatch: MonkeyPatch = MonkeyPatch()
    monkeypatch.setattr("builtins.input", lambda _: age_input)  # type: ignore

    generate_age_report(students)

    assert os.path.exists(report_file)

    os.remove(report_file)


def test_generate_cities_report(tmpdir: Path) -> None:
    """
    Test case for generate_cities_report function
    :param tmpdir: The temporary directory to generate the report
    :type tmpdir: Path
    :return: None
    :rtype: NoneType
    """
    report_file: str = os.path.join(tmpdir, "cities_report.csv")

    with pytest.raises(FileNotFoundError):
        generate_cities_report(students)

    generate_cities_report(students)

    assert os.path.exists(report_file)

    os.remove(report_file)


def test_generate_career_average_report(tmpdir: Path) -> None:
    """
    Test case for generate_career_average_report function
    :param tmpdir: The temporary directory to generate the report
    :type tmpdir: Path
    :return: None
    :rtype: NoneType
    """
    report_file: str = os.path.join(tmpdir, "career_average_report.csv")

    with pytest.raises(FileNotFoundError):
        generate_career_average_report(students)

    generate_career_average_report(students)

    assert os.path.exists(report_file)

    os.remove(report_file)


def test_generate_above_below_avg_report(tmpdir: Path) -> None:
    """
    Test case for generate_above_below_avg_report function
    :param tmpdir: The temporary directory to generate the report
    :type tmpdir: Path
    :return: None
    :rtype: NoneType
    """
    report_file: str = os.path.join(tmpdir, "above_below_avg_report.csv")

    with pytest.raises(FileNotFoundError):
        generate_above_below_avg_report(students)

    generate_above_below_avg_report(students)

    assert os.path.exists(report_file)

    os.remove(report_file)


def test_generate_age_group_report(tmpdir: Path) -> None:
    """
    Test case for generate_age_group_report function
    :param tmpdir: The temporary directory to generate the report
    :type tmpdir: Path
    :return: None
    :rtype: NoneType
    """
    report_file: str = os.path.join(tmpdir, "age_group_report.csv")

    with pytest.raises(FileNotFoundError):
        generate_age_group_report(students)

    generate_age_group_report(students)

    assert os.path.exists(report_file)

    os.remove(report_file)


def test_generate_most_career_city_report(tmpdir: Path) -> None:
    """
    Test case for generate_most_career_city_report function
    :param tmpdir: The temporary directory to generate the report
    :type tmpdir: Path
    :return: None
    :rtype: NoneType
    """
    report_file: str = os.path.join(tmpdir, "most_career_city_report.csv")

    with pytest.raises(FileNotFoundError):
        generate_most_career_city_report(students)

    generate_most_career_city_report(students)

    assert os.path.exists(report_file)

    os.remove(report_file)
