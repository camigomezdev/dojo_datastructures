"""
A module for test misc reports in the tests.test_reports package.
"""
import logging
from unittest.mock import MagicMock, mock_open, patch

from reports.misc_reports import generate_most_career_city_report
from tests.test_processing.test_utils import students


@patch('builtins.open', new_callable=mock_open)
@patch.object(logging.Logger, 'info')
def test_generate_most_career_city_report(
        mock_log_info: MagicMock, mock_file_open: MagicMock
) -> None:
    """
    Test case for generate_most_career_city_report function.
    :param mock_log_info: Mocked logging info method from Logger class
    :type mock_log_info: MagicMock
    :param mock_file_open: Mocked open method from builtins
    :type mock_file_open: MagicMock
    :return: None
    :rtype: NoneType
    """
    generate_most_career_city_report(students)

    mock_file_open.assert_called_once_with(
        "data/processed/most_career_city_report.csv", "w")
    mock_log_info.assert_called_once_with(
        "Generated the city with most career variety career report")
