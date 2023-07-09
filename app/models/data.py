""" Data Model file for Dojo_Datastructures """
import csv
from pathlib import Path


class DataModel:
    """ Class for Data Model """

    def __init__(self, **kwargs) -> None:
        """
        Init Data Model requirements
        """
        self.pmvcp_model = kwargs['pmvcp_model']
        self.pmvcp_view = kwargs['pmvcp_view']
        self.pmvcp_controller = kwargs['pmvcp_controller']
        self.lang = kwargs['lang']
        self.cfg = kwargs['cfg']
        self.about = kwargs['about']
        self.menus = kwargs['menus']

    def get_data(self, mode='list_dict') -> dict:
        """
        Reads csv file and return data by list_dict (list{dict{}}) or dict_dict (dict1{dict2{}})
        """
        file_path = self._get_file_path

        try:
            if mode == 'list_dict':
                with open(file_path, 'r', encoding='utf-8') as file:
                    return list(csv.DictReader(file, delimiter=','))

            if mode == 'dict_dict':
                with open(file_path, 'r', encoding='utf-8') as file:
                    temp_dict = {}
                    i = 0
                    lines = csv.DictReader(file, delimiter=',')
                    for line in lines:
                        temp_dict[i] = line
                        i += 1
                    return temp_dict

            return []
        except Exception as error:
            print(self.lang.sprintf("LANG_ERROR_READING_FILE", self.cfg.get("DATA_FILE", "OPTIONS"), error))

    @property
    def _get_file_name(self) -> str:
        """
        Returns data file name
        """
        return self.cfg.get("DATA_FILE", "OPTIONS")

    @property
    def _get_file_path(self) -> str:
        """
        Returns file path
        """
        try:
            current_path = Path.cwd()
            file_path = current_path / \
                self.cfg.get("APP_FOLDER", "DEFAULT") / \
                'static' / 'data' / self._get_file_name

            if (file_path.exists() and file_path.is_file()):
                return file_path

            return None
        except Exception as error:
            print((self.lang.sprintf(
                    "LANG_ERROR_FILE_NO_EXISTS", self.cfg.get("DATA_FILE", "OPTIONS"), file_path)), error)
