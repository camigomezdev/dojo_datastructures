""" Export Helper file for Dojo_Datastructures """


class ExportHelper():
    """ Class for Export Helper """

    def __init__(self, **kwargs) -> None:
        """
        Init Export Helper requirements
        """
        self.kwargs = kwargs

    def save_to_table(self, data: dict, file_name: str) -> str:
        """
        Save data to file in a txt file in table format
        """
        from app.helpers.table_helper import TableHelper

        table_helper = TableHelper(data, file_name, **self.kwargs)
        table_helper.record_file()

        return table_helper.record_file()

    def save_to_csv(self, data: dict, file_name: str) -> str:
        """
        Save data to file in a csv file format
        """
        from app.helpers.csv_helper import CsvHelper

        csv_helper = CsvHelper(data, file_name, **self.kwargs)

        return csv_helper.record_file()

    def save_to_dict(self, data: dict, file_name: str) -> str:
        """
        Save data to file in a txt file in dict format
        """
        from app.helpers.dict_helper import DictHelper

        dict_helper = DictHelper(data, file_name, **self.kwargs)

        return dict_helper.record_file()

    def save_to_json(self, data: dict, file_name: str) -> str:
        """
        Save data to file in a json file format
        """
        from app.helpers.json_helper import JsonHelper

        json_helper = JsonHelper(data, file_name, **self.kwargs)

        return json_helper.record_file()
