""" Students By Average Age Model file for Dojo_Datastructures
Reto: Agrupa los estudiantes en diferentes rangos de edad (18-25, 26-35, mayores de 35)."""
from app.models.base_model import BaseModel


class StudentsByAverageAgeModel(BaseModel):
    """ Class for Students By Average Age Model  """

    def _formater_decode(self, section: str) -> list:
        """
        Cooking the data, returns a list
        """
        data_items = self._data.get_data('dict_dict').items()
        return {key1: {key2: value2 for key2, value2 in value1.items()} for key1, value1 in data_items if int(value1["edad"]) in self._get_range(section)}

    def _formater_encode(self, datas: list) -> dict:
        """
        Formats the data to be compatible with exporters, returns a dict
        """
        return dict(enumerate(datas.values()))

    def _get_range(self, age_range: str) -> list:
        """
        Make range() for '18-25', '26-35', '> 35'
        """
        if age_range == '18-25':
            return list(range(18, 25, 1))

        if age_range == '26-35':
            return list(range(26, 35, 1))

        if age_range == '> 35':
            return list(range(36, 80, 1))

        return []
