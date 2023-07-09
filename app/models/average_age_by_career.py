""" Average Age By Career Model file for Dojo_Datastructures
Reto: Identificar la edad promedio por carrera."""
from app.models.base_model import BaseModel


class AverageAgeByCareerModel(BaseModel):
    """ Class for Average Age By Career Model  """

    def _formater_decode(self, section: str) -> list:
        """
        Cooking the data, returns a list
        """
        request_keys = {'carrera', 'edad'}
        data_items = self._data.get_data('dict_dict').items()

        temp_dict = {key1: {key2: value1[key2] for key2 in value1.keys(
        ) & request_keys} for key1, value1 in data_items}

        return [value for key, value in temp_dict.items()]

    def _formater_encode(self, datas: list) -> dict:
        """
        Formats the data to be compatible with exporters, returns a dict
        """
        temp_dict2 = {}
        career_values = sorted(set({each['carrera'] for each in datas}))
        ages_values = {int(each['edad']) for each in datas}
        range_values = range(0, len(datas))

        for key, data in zip(range_values, career_values):
            ages_values = {int(each['edad'])
                           for each in datas if each['carrera'] == data}
            temp_dict2[key] = {'carrera': data,
                               'edad promedio': self._get_average_age(ages_values)}

        return temp_dict2

    def _get_average_age(self, ages: list) -> int:
        """
        Joins average ages list and compare current age, then return a string legend
        """
        return round(sum(ages)/int(len(ages)))
