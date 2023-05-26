"""
A module for test main in the tests package.
"""
from typing import Any

import pytest
from pytest import MonkeyPatch

from main import main


@pytest.mark.parametrize(
    "user_input",
    ["1\n0\n", "2\n0\n", "3\n0\n", "4\n0\n", "5\n0\n", "6\n0\n", "7\n0\n",
     "8\n0\n", "0\n"]
)
def test_main_user_input(
        monkeypatch: MonkeyPatch, capsys: Any, user_input: str
) -> None:
    """
    Test case for main user input
    :param monkeypatch: The fixture to replace the input with mock
     implementation
    :type monkeypatch: MonkeyPatch
    :param capsys: The system captured data
    :type capsys: Any
    :param user_input: The user input
    :type user_input: str
    :return: None
    :rtype: NoneType
    """
    monkeypatch.setattr("builtins.input", lambda _: user_input)  # type: ignore
    main()

    captured = capsys.readouterr()
    assert "Program exited." in captured.out


def test_main_invalid_choice(capsys: Any) -> None:
    """
    Test case for main invalid choice
    :param capsys: The system captured data
    :type capsys: Any
    :return: None
    :rtype: NoneType
    """
    user_input: str = "9\n0\n"
    monkeypatch: MonkeyPatch = MonkeyPatch()
    monkeypatch.setattr("builtins.input", lambda _: user_input)  # type: ignore
    main()

    captured = capsys.readouterr()
    assert "Invalid choice. Please try again." in captured.out
