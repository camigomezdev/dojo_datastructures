"""
A module for test utils in the tests.test_processing package.
"""
from typing import Any

import pytest

from processing.utils import (
    average_by_group,
    count_by_group,
    filter_students,
    get_unique_values,
    group_by,
)

students: list[dict[str, Any]] = [
    {"nombre": "John", "apellido": "Wick", "edad": 20,
     "carrera": "Telematics"},
    {"nombre": "Emily", "apellido": "Blunt", "edad": 22,
     "carrera": "Psychology"},
    {"nombre": "David", "apellido": "Beckham", "edad": 25,
     "carrera": "Medicine"},
    {"nombre": "Sophie", "apellido": "Turner", "edad": 23,
     "carrera": "Art History"}
]


def test_filter_students() -> None:
    """
    Test case for filter_students function.
    :return: None
    :rtype: NoneType
    """
    filtered_students: list[dict[str, Any]] = list(
        filter_students(students, "carrera", "Psychology"))
    assert len(filtered_students) == 1
    assert filtered_students[0]["nombre"] == "Emily"
    assert filtered_students[0]["apellido"] == "Blunt"


def test_group_by() -> None:
    """
    Test case for group_by function.
    :return: None
    :rtype: NoneType
    """
    groups: dict[Any, list[dict[str, Any]]] = group_by(students, "carrera")
    assert len(groups) == 3
    assert groups["Telematics"][0]["nombre"] == "John"
    assert groups["Telematics"][0]["apellido"] == "Wick"
    assert groups["Psychology"][0]["nombre"] == "Emily"
    assert groups["Psychology"][0]["apellido"] == "Blunt"
    assert groups["Medicine"][0]["nombre"] == "David"
    assert groups["Medicine"][0]["apellido"] == "Beckham"


def test_average_by_group() -> None:
    """
    Test case for average_by_group function.
    :return: None
    :rtype: NoneType
    """
    age_average: dict[Any, float] = average_by_group(
        students, "carrera", "edad")
    assert len(age_average) == 3
    assert age_average["Telematics"] == pytest.approx(20.0)  # type: ignore
    assert age_average["Psychology"] == pytest.approx(22.0)  # type: ignore
    assert age_average["Medicine"] == pytest.approx(25.0)  # type: ignore


def test_get_unique_values() -> None:
    """
    Test case for get_unique_values function.
    :return: None
    :rtype: NoneType
    """
    unique_careers: list[str] = get_unique_values(students, "carrera")
    assert len(unique_careers) == 3
    assert "Telematics" in unique_careers
    assert "Psychology" in unique_careers
    assert "Medicine" in unique_careers


def test_count_by_group() -> None:
    """
    Test case for count_by_group function.
    :return: None
    :rtype: NoneType
    """
    result: dict[str, int] = count_by_group(students, "carrera")
    assert result == {"Telematics": 1, "Psychology": 1, "Medicine": 1,
                      "Art History": 1}

    result = count_by_group(students, "edad")
    assert result == {20: 1, 22: 1, 25: 1, 23: 1}  # type: ignore

    result = count_by_group(students, "nombre")
    assert result == {"John": 1, "Emily": 1, "David": 1, "Sophie": 1}

    result = count_by_group(students, "city")
    assert result == {}
