""" Students By Country Model file for Dojo_Datastructures
Reto: Obtener todos los estudiantes que vivan en un país dado."""
from app.models.base_model import BaseModel


class StudentsByCountryModel(BaseModel):
    """ Class for Students By Country Model  """

    def _formater_decode(self, section: str) -> dict:
        """
        Cooking the data, returns a dict
        """
        data_items = self._data.get_data('dict_dict').items()
        return {key1: {key2: value1[key2] for key2 in value1.keys()} for key1, value1 in data_items if value1['pais'] == section}

    def _formater_encode(self, datas: dict) -> dict:
        """
        Formats the data to be compatible with exporters, returns a dict
        """
        return dict(enumerate(datas.values()))
