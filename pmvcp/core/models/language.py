""" Language Model file for Py MVC Prompt Package """
# __doc__ (Language Model file for Py MVC Prompt Package)

import os

from pmvcp.core.models.parser import Parser


class Language(Parser):
    """ Class for PMVCP Language Model  """

    _tag = 'en'

    def __init__(self, cfg: object) -> None:
        """
        Init PMVCP Language Model requirements
        """
        self.cfg = cfg
        self._only_section = 'LANG'
        self._file_path = self._set_file_path

    @property
    def lang(self) -> object:
        """
        Returns the language configparser.ConfigParser
        """
        return self.data

    @property
    def tag(self) -> str:
        """
        Returns default language name tag
        """
        return self._tag

    @tag.setter
    def tag(self, tag='en') -> str:
        """
        Set default language name tag, (en) for default
        """
        self._tag = tag.lower()
    
    @property
    def _set_file_path(self) -> str:
        """
        Sets the file path
        """
        path = f'{self.cfg.get("APP_FOLDER", "DEFAULT")}/languages/{self.tag}.ini'
        
        if self.path_exists is False:
            path = f'{self.cfg.get("APP_FOLDER", "DEFAULT")}/languages/{self.cfg.get("DEFAULT_LANGUAGE", "LANGUAGE")}.ini'

        return path
    
    @property
    def update(self) -> str:
        """
        Calls for update the file path
        """
        self._file_path = self._set_file_path
        
    def sprintf(self, text, *args, **kwargs) -> str:
        """
        Return a formatted string
        """
        return self.get(text).format(*args, **kwargs)

    def translate(self, text) -> str:
        """
        Return a translated string
        """
        import configparser
        default = {text: text}

        try:
            return self.data.get(self._only_section, text)
        except configparser.NoOptionError as error:
            return self.data.get(self._only_section, text, vars=default)
