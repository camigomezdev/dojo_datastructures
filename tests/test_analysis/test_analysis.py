"""
A module for test analysis in the tests.test_analysis package.
"""
from typing import Any

from analysis.analysis import (
    career_above_below_avg,
    city_with_most_careers,
    split_into_age_groups,
)

students: list[dict[str, Any]] = [
    {"nombre": "John", "edad": 22, "carrera": "Computer Engineering",
     "ciudad": "New York"},
    {"nombre": "Emily", "edad": 25, "carrera": "Psychology",
     "ciudad": "Los Angeles"},
    {"nombre": "David", "edad": 30, "carrera": "Medicine",
     "ciudad": "Chicago"},
    {"nombre": "Sophie", "edad": 28, "carrera": "Art History",
     "ciudad": "Chicago"},
]


def test_career_above_below_avg() -> None:
    """
    Test case for career_above_below_avg function.
    :return: None
    :rtype: NoneType
    """
    result: dict[str, str] = career_above_below_avg(students)

    assert len(result) == 4
    assert result["John"] == "below"
    assert result["Emily"] == "above"
    assert result["David"] == "above"
    assert result["Sophie"] == "below"


def test_split_into_age_groups() -> None:
    """
    Test case for split_into_age_groups function.
    :return: None
    :rtype: NoneType
    """
    result: dict[str, list[dict[str, Any]]] = split_into_age_groups(students)

    assert len(result) == 3
    assert len(result["18-25"]) == 1
    assert len(result["26-35"]) == 2
    assert len(result["36+"]) == 1


def test_city_with_most_careers() -> None:
    """
    Test case for city_with_most_careers function.
    :return: None
    :rtype: NoneType
    """
    result: str = city_with_most_careers(students)

    assert result == "Chicago"
