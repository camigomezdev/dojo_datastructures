"""
A module for test submenu reports in the tests.test_reports package.
"""
import logging
from typing import Any, Callable
from unittest.mock import MagicMock, mock_open, patch

import pytest

from reports.submenu_reports import (
    generate_age_report,
    generate_city_report,
    generate_country_report,
)
from tests.test_processing.test_utils import students


@pytest.mark.parametrize(
    "func, key, report_file",
    [
        (generate_city_report, "ciudad", "data/processed/city_report.csv"),
        (generate_country_report, "pais", "data/processed/country_report.csv")
    ]
)
@patch('builtins.open', new_callable=mock_open)
@patch('reports.submenu_reports.get_user_choice_from_submenu', return_value="1")
@patch.object(logging.Logger, 'info')
def test_generate_submenu_report(
        mock_log_info: MagicMock,
        mock_file_open: MagicMock, func: Callable[..., Any], report_file: str
) -> None:
    """
    Test case for generate_submenu_report function.
    :param mock_log_info: Mocked logging info method from Logger class
    :type mock_log_info: MagicMock
    :param mock_file_open: Mocked open method from builtins
    :type mock_file_open: MagicMock
    :param func: generate_submenu_report method to be tested
    :type func: Callable
    :param report_file: The path to the report file
    :type report_file: str
    :return: None
    :rtype: NoneType
    """
    func(students)
    mock_file_open.assert_called_once_with(report_file, "w")
    mock_log_info.assert_called_once()


@patch('builtins.open', new_callable=mock_open)
@patch('builtins.input', side_effect=["30", "0"])
@patch.object(logging.Logger, 'info')
def test_generate_age_report(
        mock_log_info: MagicMock, mock_file_open: MagicMock
) -> None:
    """
    Test case for generate_age_report function.
    :param mock_log_info: Mocked logging info method from Logger class
    :type mock_log_info: MagicMock
    :param mock_file_open: Mocked open method from builtins
    :type mock_file_open: MagicMock
    :return: None
    :rtype: NoneType
    """
    generate_age_report(students)
    mock_file_open.assert_called_once_with(
        "data/processed/age_report.csv", "w")
    mock_log_info.assert_called_once_with("Generated %s report", 30)
