""" City With More Careers Model file for Dojo_Datastructures
Reto: Identifica la ciudad que tienen la mayor variedad de carreras universitarias entre los estudiantes."""
from app.models.base_model import BaseModel


class CityWithMoreCareersModel(BaseModel):
    """ Class for City With More Careers Model  """

    def _formater_decode(self, section: str) -> list:
        """
        Cooking the data, returns a list
        """
        request_keys = {"ciudad", "carrera"}
        data_items = self._data.get_data('dict_dict').items()

        return {key1: {key2: value1[key2] for key2 in value1.keys() & request_keys} for key1, value1 in data_items}

    def _formater_encode(self, datas: list) -> dict:
        """
        Formats the data to be compatible with exporters, returns a dict
        """
        temp_dict = {}
        temp_dict2 = {}
        temp_dict3 = {}
        temp_list = []
        range_values = range(0, len(datas))

        for value1 in datas.values():
            temp_list.append(value1["ciudad"] + ' - ' + value1["carrera"])
            temp_dict[value1["ciudad"]] = str(
                temp_list).count(value1["ciudad"])

        highest = max(temp_dict.values())
        temp_dict2 = {k for k, v in temp_dict.items() if v == highest}

        for key, data in zip(range_values, temp_dict2):
            temp_dict3[key] = {"ciudad": data, "carreras": highest}

        return temp_dict3
