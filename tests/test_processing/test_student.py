"""
A module for test student in the tests.test_processing package.
"""
from pathlib import Path
from typing import Any

import pytest

from core.exceptions import NOT_NUMBER, VALID_AGE, ValidationError
from processing.student import Student


def test_load_data_valid_csv(tmp_path: Path) -> None:
    """
    Test case for load_data method with a valid CSV file.
    :param tmp_path: The path to the file to load
    :type tmp_path: Path
    :return: None
    :rtype: NoneType
    """
    csv_file: Path = tmp_path / "test_data.csv"
    csv_file.write_text(
        "nombre,apellido,ciudad,pais,edad,carrera\n"
        "John,Doe,New York,USA,25,Computer Science\n"
        "Jane,Smith,Los Angeles,USA,22,Psychology\n"
        "David,Johnson,Chicago,USA,24,Engineering\n"
    )
    student: Student = Student(str(csv_file))
    loaded_data: list[dict[str, Any]] = student.load_data()

    assert len(loaded_data) == 3
    assert loaded_data[0]["nombre"] == "John"
    assert loaded_data[0]["apellido"] == "Doe"
    assert loaded_data[0]["ciudad"] == "New York"
    assert loaded_data[0]["pais"] == "USA"
    assert loaded_data[0]["edad"] == 25
    assert loaded_data[0]["carrera"] == "Computer Science"

    assert loaded_data[1]["nombre"] == "Jane"
    assert loaded_data[1]["apellido"] == "Smith"
    assert loaded_data[1]["ciudad"] == "Los Angeles"
    assert loaded_data[1]["pais"] == "USA"
    assert loaded_data[1]["edad"] == 22
    assert loaded_data[1]["carrera"] == "Psychology"

    assert loaded_data[2]["nombre"] == "David"
    assert loaded_data[2]["apellido"] == "Johnson"
    assert loaded_data[2]["ciudad"] == "Chicago"
    assert loaded_data[2]["pais"] == "USA"
    assert loaded_data[2]["edad"] == 24
    assert loaded_data[2]["carrera"] == "Engineering"


def test_load_data_invalid_csv(tmp_path: Path) -> None:
    """
    Test case for load_data method with an invalid CSV file.
    :param tmp_path: The path to the file to load
    :type tmp_path: Path
    :return: None
    :rtype: NoneType
    """
    csv_file: Path = tmp_path / "test_data.csv"
    csv_file.write_text(
        "nombre,apellido,ciudad,pais,edad,carrera\n"
        "John,Doe,New York,USA,25,Computer Science\n"
        "Jane,Smith,Los Angeles,USA,22,Psychology\n"
        "David,Johnson,Chicago,USA,24,Invalid\n"
    )
    student: Student = Student(str(csv_file))

    with pytest.raises(ValidationError) as exc_info:
        student.load_data()

    assert str(exc_info.value) == "Invalid career: 'Invalid'"


def test_load_data_invalid_age(tmp_path: Path) -> None:
    """
    Test case for load_data method with invalid age in the CSV file.
    :param tmp_path: The path to the file to load
    :type tmp_path: Path
    :return: None
    :rtype: NoneType
    """
    csv_file: Path = tmp_path / "test_data.csv"
    csv_file.write_text(
        "nombre,apellido,ciudad,pais,edad,carrera\n"
        "John,Doe,New York,USA,25,Computer Science\n"
        "Jane,Smith,Los Angeles,USA,22,Psychology\n"
        "David,Johnson,Chicago,USA,-5,Engineering\n"
    )
    student: Student = Student(str(csv_file))

    with pytest.raises(ValidationError) as exc_info:
        student.load_data()

    assert str(exc_info.value) == VALID_AGE


def test_load_data_non_numeric_age(tmp_path: Path) -> None:
    """
    Test case for load_data method with non-numeric age in the CSV file.
    :param tmp_path: The path to the file to load
    :type tmp_path: Path
    :return: None
    :rtype: NoneType
    """
    csv_file: Path = tmp_path / "test_data.csv"
    csv_file.write_text(
        "nombre,apellido,ciudad,pais,edad,carrera\n"
        "John,Doe,New York,USA,25,Computer Science\n"
        "Jane,Smith,Los Angeles,USA,22,Psychology\n"
        "David,Johnson,Chicago,USA,Invalid,Engineering\n"
    )
    student: Student = Student(str(csv_file))

    with pytest.raises(ValidationError) as exc_info:
        student.load_data()

    assert str(exc_info.value) == NOT_NUMBER


def test_load_data_file_not_found() -> None:
    """
    Test case for load_data method when the CSV file does not exist.
    :return: None
    :rtype: NoneType
    """
    student: Student = Student("non_existent_file.csv")

    with pytest.raises(FileNotFoundError):
        student.load_data()


def test_load_data_empty_csv(tmp_path: Path) -> None:
    """
    Test case for load_data method with an empty CSV file.
    :param tmp_path: The path to the file to load
    :type tmp_path: Path
    :return: None
    :rtype: NoneType
    """
    csv_file: Path = tmp_path / "test_data.csv"
    csv_file.write_text("nombre,apellido,ciudad,pais,edad,carrera\n")
    student: Student = Student(str(csv_file))
    loaded_data: list[dict[str, Any]] = student.load_data()

    assert len(loaded_data) == 0
