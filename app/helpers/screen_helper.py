""" Screen Helper file for Dojo_Datastructures """


class ScreenHelper():
    """ Class for Screen Helper """

    def __init__(self, **kwargs) -> None:
        """
        Init Screen Helper requirements
        """
        self.kwargs = kwargs

    def to_string_table(self, data: dict) -> str:
        """
        Show data at screen in table format
        """
        from app.helpers.table_helper import TableHelper

        table_helper = TableHelper(data, 'temp_file', **self.kwargs)
        table_helper.record_file()

        return table_helper.on_screen()

    def to_string_csv(self, data: dict) -> str:
        """
        Show data at screen in csv format
        """
        from app.helpers.csv_helper import CsvHelper

        csv_helper = CsvHelper(data, 'temp_file', **self.kwargs)
        csv_helper.record_file()

        return csv_helper.raw_read_file()

    def to_string_dict(self, data: dict) -> str:
        """
        Show data at screen in dict format
        """
        from app.helpers.dict_helper import DictHelper

        dict_helper = DictHelper(data, 'temp_file', **self.kwargs)

        return dict_helper.on_screen()

    def to_string_json(self, data: dict) -> str:
        """
        Show data at screen in json format
        """
        from app.helpers.json_helper import JsonHelper

        json_helper = JsonHelper(data, 'temp_file', **self.kwargs)
        json_helper.record_file()

        return json_helper.raw_read_file()
