""" Students` Cities Residence Model file for Dojo_Datastructures
Reto: Obtener todas las ciudades de residencia de los estudiantes."""
from app.models.base_model import BaseModel


class StudentsCitiesResidenceModel(BaseModel):
    """ Class for Students` Cities Residence Model  """

    def _formater_decode(self, section: str) -> list:
        """
        Cooking the data, returns a list
        """
        request_keys = {'ciudad'}
        data_items = self._data.get_data('dict_dict').items()

        temp_dict = {key1: {key2: value1[key2] for key2 in value1.keys(
        ) & request_keys} for key1, value1 in data_items}

        return list(temp_dict.values())

    def _formater_encode(self, datas: list) -> dict:
        """
        Formats the data to be compatible with exporters, returns a dict
        """
        temp_dict2 = {}
        cities_values = sorted(set({each['ciudad'] for each in datas}))
        range_values = range(0, len(datas))

        for key, data in zip(range_values, cities_values):
            temp_dict2[key] = {'ciudad': data}
        return temp_dict2
