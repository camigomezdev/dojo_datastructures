""" Table Helper file for Dojo_Datastructures """
import os
from pathlib import Path
from tabulate import tabulate


class TableHelper():
    """ Class for Table Helper """
    _data = ''
    _file_name = ''
    _file_extension = 'html'

    def __init__(self, data: list, file_name: str, **kwargs) -> None:
        """
        Init Table Helper requirements
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
        return current_path / self.cfg.get("APP_FOLDER", "DEFAULT") / 'static' / 'html' / self._file_name

    @property
    def field_names(self) -> list:
        """
        Returns field names
        """
        return list(self._data[0].keys())

    def on_screen(self, headers='firstrow', tablefmt='fancy_grid') -> str:
        """
        Return screen format
        """
        table_list = []

        if isinstance(self._data, dict):
            table_list.append(self.field_names)
            for key1, value1 in self._data.items():
                table_list.append(list(value1.values()))
        else:
            table_list.append(list(self.field_names))
            for key1, value1 in enumerate(self._data, start=0):
                table_list.append(list(self._data[key1].values()))

        return tabulate(table_list, headers, tablefmt)

    def record_file(self) -> str:
        """
        Records a txt file
        """
        if os.name == 'nt':
            newline_value = ''
        else:
            newline_value = '\n'

        try:
            with open(self.file_path, 'w', newline=newline_value, encoding="utf-8") as file:
                file.write(str(self.on_screen('firstrow', 'html')))

            return self.lang.sprintf("LANG_FILE_SAVED_TO", self._file_extension, self.file_path)
        except Exception as error:
            return error
