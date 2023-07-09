""" Base Model file for Dojo_Datastructures """
from app.helpers.screen_helper import ScreenHelper
from app.helpers.export_helper import ExportHelper


class BaseModel():
    """ Class for Base Model  """
    _data = ''

    def __init__(self, **kwargs) -> None:
        """
        Init Base Model requirements
        """
        self.pmvcp_model = kwargs['pmvcp_model']
        self.pmvcp_view = kwargs['pmvcp_view']
        self.pmvcp_controller = kwargs['pmvcp_controller']
        self.lang = kwargs['lang']
        self.cfg = kwargs['cfg']
        self.about = kwargs['about']
        self.menus = kwargs['menus']

        self._data = self.data

    @property
    def data(self) -> dict:
        """
        Returns getter for data (dict)
        """
        return self._data

    @data.setter
    def data(self, data: dict) -> list:
        """
        Returns setter for data (dict)
        """
        self._data = data

    def make_export(self, section: str, formats: str, output: str) -> dict:
        """
        Splits export between screen or file (dict)
        """
        if output == 'screen':
            return self.make_export_to_screen(section, formats)

        if output == 'file':
            return self.make_export_to_file(section, formats)

        raise Exception(self.lang.get("LANG_ERROR_NO_OUTPUT"))

    def make_export_to_screen(self, section: str, formats: str) -> dict:
        """
        Return screen export (dict)
        """
        kwargs = {'lang': self.lang, 'cfg': self.cfg, 'about': self.about}
        screen = ScreenHelper(**kwargs)

        if formats == 'table':
            return screen.to_string_table(self._prepare_export(section))

        if formats == 'dictionary':
            return screen.to_string_dict(self._prepare_export(section))

        if formats == 'csv':
            return screen.to_string_csv(self._prepare_export(section))

        if formats == 'json':
            return screen.to_string_json(self._prepare_export(section))

        raise Exception(self.lang.get("LANG_ERROR_NO_FORMAT"))

    def make_export_to_file(self, section: str, formats: str, output: str) -> dict:
        """
        Return file export (dict)
        """
        kwargs = {'lang': self.lang, 'cfg': self.cfg, 'about': self.about}
        export = ExportHelper(**kwargs)
        file_name = input(self.lang.get("LANG_INSERT_FILE_NAME"))

        if formats == 'table':
            return export.save_to_table(self._prepare_export(section), file_name)

        if formats == 'dictionary':
            return export.save_to_dict(self._prepare_export(section), file_name)

        if formats == 'csv':
            return export.save_to_csv(self._prepare_export(section), file_name)

        if formats == 'json':
            return export.save_to_json(self._prepare_export(section), file_name)

        raise Exception(self.lang.get("LANG_ERROR_NO_FORMAT"))

    def _prepare_export(self, section: str) -> list | dict:
        """
        Prepare data for export (dict)
        """
        keys = self._formater_decode(section)

        return self._formater_encode(keys)

    def _formater_decode(self, section: str) -> list:
        """
        Cooking the data, returns a list
        """
        return []

    def _formater_encode(self, datas: list) -> list | dict:
        """
        Formats the data to be compatible with exporters, returns a dict
        """
        return datas
