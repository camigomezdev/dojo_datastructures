"""
A module for test average reports in the tests.test_reports package.
"""
import logging
from unittest.mock import MagicMock, mock_open, patch

from reports.average_reports import (
    generate_above_below_avg_report,
    generate_career_average_report,
)
from tests.test_processing.test_utils import students


@patch('builtins.open', new_callable=mock_open)
@patch.object(logging.Logger, 'info')
def test_generate_career_average_report(
        mock_log_info: MagicMock, mock_file_open: MagicMock
) -> None:
    """
    Test case for generate_career_average_report function.
    :param mock_log_info: Mocked logging info method from Logger class
    :type mock_log_info: MagicMock
    :param mock_file_open: Mocked open method from builtins
    :type mock_file_open: MagicMock
    :return: None
    :rtype: NoneType
    """
    generate_career_average_report(students)

    # Assert the write calls
    mock_file_open.assert_called_once_with(
        "data/processed/career_average_report.csv", "w")
    mock_log_info.assert_called_once_with("Generated career average report")


@patch('builtins.open', new_callable=mock_open)
@patch.object(logging.Logger, 'info')
def test_generate_above_below_avg_report(
        mock_log_info: MagicMock, mock_file_open: MagicMock
) -> None:
    """
    Test case for generate_above_below_avg_report function.
    :param mock_log_info: Mocked logging info method from Logger class
    :type mock_log_info: MagicMock
    :param mock_file_open: Mocked open method from builtins
    :type mock_file_open: MagicMock
    :return: None
    :rtype: NoneType
    """
    generate_above_below_avg_report(students)

    # Assert the write calls
    mock_file_open.assert_called_once_with(
        "data/processed/above_below_avg_report.csv", "w")
    mock_log_info.assert_called_once_with(
        "Generated age above-below average report")
