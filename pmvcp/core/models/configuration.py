""" Configuration Model file for Py MVC Prompt Package """
# __doc__ (Configuration Model file for Py MVC Prompt Package)

import os

from pmvcp.core.models.parser import Parser


class Configuration(Parser):
    """ Class for PMVCP Configuration Model  """

    def __init__(self) -> None:
        """
        Init PMVCP Configuration Model requirements
        """
        self._only_section = 'LANG'
        self._file_path = self._set_file_path

    @property
    def cfg(self) -> object:
        """
        Returns the language configparser.ConfigParser
        """
        return self.data

    @property
    def _set_file_path(self) -> str:
        """
        Sets the file path
        """
        return 'config.ini'
