""" Menus Model file for Py MVC Prompt Package """
# __doc__ (Menus Model file for Py MVC Prompt Package)

from pmvcp.core.models.parser import Parser


class Menus(Parser):
    """ Class for PMVCP Menus Model  """

    _tag = 'en'
    
    def __init__(self, cfg: object) -> None:
        """
        Init PMVCP Menus Model requirements
        """
        self.cfg = cfg
        self._only_section = 'MENUS'
        self._file_path = self._set_file_path

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
        path = f'{self.cfg.get("APP_FOLDER", "DEFAULT")}/languages/{self.tag}.menus.ini'
        
        if self.path_exists is False:
            path = f'{self.cfg.get("APP_FOLDER", "DEFAULT")}/languages/{self.cfg.get("DEFAULT_LANGUAGE", "LANGUAGE")}.menus.ini'

        return path
    
    @property
    def update(self) -> str:
        """
        Calls for update the file path
        """
        self._file_path = self._set_file_path
