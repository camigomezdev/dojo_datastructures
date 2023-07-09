""" Json Helper file for Dojo_Datastructures """
import json
import os
from pathlib import Path


class JsonHelper():
    """ Class for Json Helper """
    _data = ''
    _file_name = ''
    _file_extension = 'json'

    def __init__(self, data: list, file_name: str, **kwargs) -> None:
        """
        Init Json Helper requirements
        """
        self._data = data
        self._file_name = f'{file_name}.{self._file_extension}'

        self.lang = kwargs['lang']
        self.cfg = kwargs['cfg']
        self.about = kwargs['about']

    @property
    def file_path(self) -> Path:
        """
        Returns file path
        """
        current_path = Path.cwd()
        return current_path / self.cfg.get("APP_FOLDER", "DEFAULT") / 'static' / 'json' / self._file_name

    @property
    def field_names(self) -> list:
        """
        Returns field names
        """
        return list(self._data[0].keys())

    def raw_read_file(self) -> str:
        """
        Reads a csv file
        """
        output = []

        try:
            with open(self.file_path, 'r', encoding="utf-8") as file:
                for row in file.readlines():
                    output.append(row)

            return ''.join(output)
        except Exception as error:
            return error

    def record_file(self) -> str:
        """
        Records a csv file
        """
        if os.name == 'nt':
            newline_value = ''
        else:
            newline_value = '\n'

        try:
            with open(self.file_path, 'w', newline=newline_value, encoding="utf-8") as file:
                json.dump(self._data, file, indent=4,
                          sort_keys=True, ensure_ascii=False)

            return self.lang.sprintf("LANG_FILE_SAVED_TO", self._file_extension, self.file_path)
        except Exception as error:
            return error
