"""
A module for exceptions in the core package.
"""
VALID_AGE: str = "'edad' field must be a positive integer."
NOT_NUMBER: str = "'edad' field must be a number."


class ValidationError(Exception):
    """Exception raised for errors in the student data."""

    def __init__(self, message: str):
        self.message: str = message
        super().__init__(self.message)
