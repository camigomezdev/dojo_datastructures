""" Careers By Average Age Controller file for Dojo_Datastructures
Reto: Indicar por carrera si el estudiante está por encima o por debajo del promedio de edad."""
from app.controllers.base_controller import BaseController
from app.models.careers_by_average_age import CareersByAverageAgeModel
from app.views.careers_by_average_age import CareersByAverageAgeView


class CareersByAverageAgeController(BaseController):
    """ Class for Careers By Average Age Controller  """

    def __init__(self, **kwargs) -> None:
        """
        Init Careers By Average Age Controller requirements
        """
        super().__init__(**kwargs)

        self.model = CareersByAverageAgeModel(**kwargs)
        self.view = CareersByAverageAgeView(**kwargs)

        self.model.data = self.data_model
        self.data = self.data_model.get_data

    def _get_submenu_section_data(self) -> list:
        """
        Returns submenu section data
        """
        sections = []

        for row in self.data('list_dict'):
            if row["carrera"] not in sections:  # Removes duplicates
                sections.append(row["carrera"])

        return sorted(sections)

    def _get_submenu_section_message(self) -> str:
        """
        Returns submenu option message
        """
        return self.lang.get("LANG_SELECT_CAREERS")

    def _get_submenu_section_path(self, section: str) -> list:
        """
        Returns submenu carrer path
        """
        return [self.lang.sprintf("LANG_PATH_CAREER", section)]

    def _get_submenu_formats_path(self, section: str, formats: str) -> list:
        """
        Returns submenu formats path
        """
        return [self.lang.sprintf("LANG_PATH_CAREER", section),
                self.lang.sprintf("LANG_PATH_FORMAT", self.lang.translate(formats))]

    def _get_submenu_output_path(self, section: str, formats: str, output: str) -> list:
        """
        Returns submenu output path
        """
        return [self.lang.sprintf("LANG_PATH_CAREER", section),
                self.lang.sprintf("LANG_PATH_FORMAT",
                                  self.lang.translate(formats)),
                self.lang.sprintf("LANG_PATH_OUTPUT", self.lang.translate(output))]

    def _get_submenu_path(self, *args) -> list:
        """
        Returns submenu path
        """
        if len(args) == 1:
            return self._get_submenu_section_path(args[0])

        if len(args) == 2:
            return self._get_submenu_formats_path(args[0], args[1])

        if len(args) == 3:
            return self._get_submenu_output_path(args[0], args[1], args[2])

        return args
