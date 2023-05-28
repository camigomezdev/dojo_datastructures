"""
A module for utils in the tests.test_reports package.
"""
import builtins
from typing import Any

from _pytest.monkeypatch import MonkeyPatch

from reports.utils import get_user_choice_from_submenu, print_menu


def test_print_menu(captured_data: Any) -> None:
    """
    Test case for print menu function
    :param captured_data: The system captured data
    :type captured_data: Any
    :return: None
    :rtype: NoneType
    """
    expected_output = (
        "Select a report to generate:\n"
        "1. City Report\n"
        "2. Country Report\n"
        "3. Age Report\n"
        "4. Cities Report\n"
        "5. Career Average Report\n"
        "6. Above/Below Average Report\n"
        "7. Age Group Report\n"
        "8. Most Career City Report\n"
        "0. Exit\n"
    )

    print_menu()

    captured = captured_data.readouterr()
    assert captured.out == expected_output


def test_print_submenu(monkeypatch: MonkeyPatch) -> None:
    """
    Test case for print_submenu function.
    :param monkeypatch: The fixture to replace the input with mock
     implementation
    :type monkeypatch: MonkeyPatch
    :return: None
    :rtype: NoneType
    """
    monkeypatch.setattr(builtins, "input", lambda _: "2")  # type: ignore

    prompt: str = "Select a city:"
    values: list[str] = ["New York", "Los Angeles", "Chicago"]
    result: str = get_user_choice_from_submenu(prompt, values)

    assert result == "2"
