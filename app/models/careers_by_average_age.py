""" Careers By Average Age Model file for Dojo_Datastructures
Reto: Indicar por carrera si el estudiante está por encima o por debajo del promedio de edad."""
from app.models.base_model import BaseModel


class CareersByAverageAgeModel(BaseModel):
    """ Class for Careers By Average Age Model  """

    def _formater_decode(self, section: str) -> list:
        """
        Cooking the data, returns a list
        """
        request_keys = {'nombre', 'apellido', 'carrera', 'edad'}
        data_items = self._data.get_data('dict_dict').items()

        temp_dict = {key1: {key2: value1[key2] for key2 in value1.keys(
        ) & request_keys} for key1, value1 in data_items if value1['carrera'] == section}

        return [value for key, value in temp_dict.items()]

    def _formater_encode(self, datas: list) -> dict:
        """
        Formats the data to be compatible with exporters, returns a dict
        """
        temp_dict2 = {}
        ages_values = [int(each['edad']) for each in datas]
        range_values = range(0, len(datas))

        for key, data in zip(range_values, datas):
            temp_dict2[key] = {'nombre': data.get('nombre'),
                               'apellido': data.get('apellido'),
                               'carrera': data.get('carrera'),
                               'edad': data.get('edad'),
                               'edad promedio': self._get_collate_average_age(ages_values, data.get('edad'))}

        return temp_dict2

    def _get_collate_average_age(self, ages: list, current_age: int) -> str:
        """
        Joins average ages list and compare current age, then return a string legend
        """
        average_age = round(sum(ages)/int(len(ages)))

        if int(current_age) > average_age:
            return self.lang.sprintf('LANG_AVERAGE_AGE_HIGHER', str(average_age))

        if int(current_age) == average_age:
            return self.lang.sprintf('LANG_AVERAGE_AGE_EQUAL', str(average_age))

        if int(current_age) < average_age:
            return self.lang.sprintf('LANG_AVERAGE_AGE_LOWER', str(average_age))

        return None
