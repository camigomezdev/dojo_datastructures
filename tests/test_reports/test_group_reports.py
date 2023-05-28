"""
A module for test group reports in the tests.test_reports package.
"""
import logging
from typing import Any
from unittest.mock import MagicMock, mock_open, patch

from reports.group_reports import (
    generate_age_group_report,
    generate_cities_report,
    generate_group_report,
)

students: list[dict[str, Any]] = [
    {"nombre": "John", "apellido": "Wick", "ciudad": "New York", "edad": 20,
     "carrera": "Telematics", "grupo_edad": "18-25"},
    {"nombre": "Emily", "apellido": "Blunt", "ciudad": "London", "edad": 22,
     "carrera": "Psychology", "grupo_edad": "18-25"},
    {"nombre": "David", "apellido": "Beckham", "ciudad": "London", "edad": 25,
     "carrera": "Medicine", "grupo_edad": "18-25"},
    {"nombre": "Sophie", "apellido": "Turner", "ciudad": "Los Angeles",
     "edad": 23, "carrera": "Art History", "grupo_edad": "18-25"}
]


@patch('builtins.open', new_callable=mock_open)
@patch.object(logging.Logger, 'info')
def test_generate_group_report(
        mock_log_info: MagicMock, mock_file_open: MagicMock
) -> None:
    """
    Test case for generate_group_report function.
    :param mock_log_info: Mocked logging info method from Logger class
    :type mock_log_info: MagicMock
    :param mock_file_open: Mocked open method from builtins
    :type mock_file_open: MagicMock
    :return: None
    :rtype: NoneType
    """
    generate_group_report(
        students, "carrera", "numero_estudiantes",
        "data/processed/test_report.csv", ["carrera", "numero_estudiantes"]
    )

    mock_file_open.assert_called_once_with(
        "data/processed/test_report.csv", "w")
    mock_log_info.assert_called_once_with("Generated carrera report")


@patch('builtins.open', new_callable=mock_open)
@patch.object(logging.Logger, 'info')
def test_generate_cities_report(
        mock_log_info: MagicMock, mock_file_open: MagicMock
) -> None:
    """
    Test case for generate_cities_report function.
    :param mock_log_info: Mocked logging info method from Logger class
    :type mock_log_info: MagicMock
    :param mock_file_open: Mocked open method from builtins
    :type mock_file_open: MagicMock
    :return: None
    :rtype: NoneType
    """
    generate_cities_report(students)

    mock_file_open.assert_called_once_with(
        "data/processed/cities_report.csv", "w")
    mock_log_info.assert_called_once_with("Generated ciudad report")


@patch('builtins.open', new_callable=mock_open)
@patch.object(logging.Logger, 'info')
def test_generate_age_group_report(
        mock_log_info: MagicMock, mock_file_open: MagicMock
) -> None:
    """
    Test case for generate_age_group_report function.
    :param mock_log_info: Mocked logging info method from Logger class
    :type mock_log_info: MagicMock
    :param mock_file_open: Mocked open method from builtins
    :type mock_file_open: MagicMock
    :return: None
    :rtype: NoneType
    """
    generate_age_group_report(students)

    mock_file_open.assert_called_once_with(
        "data/processed/age_group_report.csv", "w")
    mock_log_info.assert_called_once_with("Generated grupo_edad report")
