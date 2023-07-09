""" Dict Helper file for Dojo_Datastructures """
import os
from pathlib import Path


class DictHelper():
    """ Class for Dict Helper """
    _data = ''
    _file_name = ''
    _file_extension = 'txt'

    def __init__(self, data: list, file_name: str, **kwargs) -> None:
        """
        Init Dict Helper requirements
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
        return current_path / self.cfg.get("APP_FOLDER", "DEFAULT") / 'static' / 'txt' / self._file_name

    @property
    def field_names(self) -> list:
        """
        Returns field names
        """
        return None

    def on_screen(self) -> str:
        """
        Return screen format
        """
        return self._pretty_write_dict(self._data)

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
                file.writelines(self.on_screen())
            return self.lang.sprintf("LANG_FILE_SAVED_TO", self._file_extension, self.file_path)
        except Exception as error:
            return error

    @staticmethod
    def _pretty_write_dict(dictionary):

        def _nested(obj, level=1):
            indentation_values = "\t" * level
            indentation_braces = "\t" * (level - 1)
            if isinstance(obj, dict):
                return "{\n%(body)s%(indent_braces)s}" % {
                    "body": "".join("%(indent_values)s\'%(key)s\': %(value)s,\n" % {
                        "key": str(key),
                        "value": _nested(value, level + 1),
                        "indent_values": indentation_values
                    } for key, value in obj.items()),
                    "indent_braces": indentation_braces
                }
            if isinstance(obj, list):
                return "[\n%(body)s\n%(indent_braces)s]" % {
                    "body": "".join("%(indent_values)s%(value)s,\n" % {
                        "value": _nested(value, level + 1),
                        "indent_values": indentation_values
                    } for value in obj),
                    "indent_braces": indentation_braces
                }
            return f"'{str(obj)}'"

        dict_text = _nested(dictionary)
        return dict_text
