""" Parser Model file for Py MVC Prompt Package """
# __doc__ (Parser Model file for Py MVC Prompt Package)

import os
import configparser

from pmvcp.core.models.base_model import BaseModel


class Parser(BaseModel):
    """ Class for PMVCP Parser Model  """
    _file_path = ''
    _only_section = ''

    def __init__(self) -> None:
        """
        Init PMVCP Parser Model requirements
        """
        if self.section:
            self._only_section = self.section

    @property
    def section(self) -> str:
        """
        Returns only a section
        """
        return self._only_section

    @section.setter
    def section(self, section=None) -> None:
        """
        Sets a section
        """
        self._only_section = section
        
    @property
    def path_exists(self):
        """
        Returns True or False if file path exists
        """
        return os.path.exists(self.file_path)

    @property
    def file_path(self) -> str:
        """
        Returns file path
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path: str) -> None:
        """
        Sets the file path
        """
        if self._set_file_path:
            self._file_path = self._set_file_path
        else:
            self._file_path = file_path

    @property
    def _set_file_path(self) -> None:
        """
        Sets the file path, default None
        """
        return None
    
    @property
    def update(self) -> None:
        """
        Calls for update the file path
        """
        return None
        
    @property
    def data(self) -> configparser.ConfigParser:
        """
        Reads parser data, return configparser.ConfigParser()
        """
        parser = configparser.ConfigParser(allow_no_value=True)
        parser.sections()
        parser.read(self.file_path, 'UTF-8')

        return parser
    
    def get(self, key, section=None, type='str') -> str:
        """
        Gets a data value from a given key
        """
        if section is None and self._only_section:
            section = self._only_section

        if type == 'int':
            return self.data.getint(section, key)

        if type == 'float':
            return self.data.getfloat(section, key)

        if type == 'boolean':
            return self.data.getboolean(section, key)

        return self.data.get(section, key)

    def to_dict(self, read_dict=False) -> dict:
        """
        Returns data to dictionary
        """
        data_dict = {}

        if self._only_section:
            for key, value in self.data.items(self._only_section):
                if read_dict:
                    data_dict[key] = eval(value)
                else:
                    data_dict[key] = value
        else:
            for section in self.data.sections():
                data_dict[section] = {}
                for key, value in self.data.items(section):
                    if read_dict:
                        data_dict[section][key] = eval(value)
                    else:
                        data_dict[section][key] = value

        return data_dict
