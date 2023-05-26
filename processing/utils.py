"""
A module for utils in the processing package that provides utility
 functions to manipulate the student data.
"""
from typing import Any, Iterator

from core.decorators import with_logging

ENCODING: str = "UTF-8"
PROJECT_NAME: str = "dojo_datastructures"
HEADER: list[str] = ["nombre", "apellido", "ciudad", "pais", "edad", "carrera"]

@with_logging
def filter_students(
    students: list[dict[str, Any]], key: str, value: Any
) -> Iterator[dict[str, Any]]:
    """
    Filter students by given key-value pair.
    :param students: The list of students
    :type students: list[dict[str, Any]]
    :param key: The key to filter
    :type key: str
    :param value: The value to filter
    :type value: Any
    :return: An iterator over the filtered students
    :rtype: Iterator[dict[str, Any]]
    """
    return (student for student in students if student[key] == value)


@with_logging
def group_by(
    students: list[dict[str, Any]], key: str
) -> dict[Any, list[dict[str, Any]]]:
    """
    Group students by a given key.
    :param students: The list of students
    :type students: list[dict[str, Any]]
    :param key: The key to group by
    :type key: str
    :return: A dictionary where keys are the unique values of the
     specified key, and values are lists of students with that key
      value
    :rtype: dict[Any, list[dict[str, Any]]]
    """
    groups: dict[Any, list[dict[str, Any]]] = {}
    for student in students:
        groups.setdefault(student[key], []).append(student)
    return groups


@with_logging
def average_by_group(
    students: list[dict[str, Any]], group_key: str, average_key: str
) -> dict[Any, float]:
    """
    Calculate average of a certain field by group.
    :param students: The list of students
    :type students: list[dict[str, Any]]
    :param group_key: The key to group by
    :type group_key: str
    :param average_key: The key to calculate average of
    :type average_key: str
    :return: A dictionary where keys are the unique values of the group
     key, and values are the average of the average key for each group
    :rtype: dict[Any, float]
    """
    groups: dict[Any, list[dict[str, Any]]] = group_by(students, group_key)
    return {
        group: sum(student[average_key] for student in students) / len(students)
        for group, students in groups.items()
    }


def get_unique_values(data: list[dict[str, Any]], key: str) -> list[str]:
    """
    Retrieve unique values for a given key from a list of dictionaries.
    :param data: The list of dictionaries
    :type data: list[dict[str, Any]]
    :param key: The key to retrieve unique values from
    :type key: str
    :return: The list of unique values
    :rtype: list[str]
    """
    return list({item[key] for item in data if key in item})


def count_by_group(data: list[dict[str, Any]], key: str) -> dict[str, int]:
    """
    Count the number of occurrences of each unique value for a given
     key in a list of dictionaries.
    :param data: The list of dictionaries
    :type data: list[dict[str, Any]]
    :param key: The key to count occurrences for
    :type key: str
    :return: A dictionary mapping unique values to their counts
    :rtype: dict[str, int]
    """
    return {
        value: sum(1 for item in data if key in item and item[key] == value)
        for value in {item[key] for item in data if key in item}
    }
