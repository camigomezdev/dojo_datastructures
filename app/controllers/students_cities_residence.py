""" Students` Cities Residence Controller file for Dojo_Datastructures
Reto: Obtener todas las ciudades de residencia de los estudiantes."""
from app.controllers.base_controller import BaseController
from app.models.students_cities_residence import StudentsCitiesResidenceModel
from app.views.students_cities_residence import StudentsCitiesResidenceView


class StudentsCitiesResidenceController(BaseController):
    """ Class for Students` Cities Residence Controller  """

    def __init__(self, **kwargs) -> None:
        """
        Init Students` Cities Residence Controller requirements
        """
        super().__init__(**kwargs)

        self.model = StudentsCitiesResidenceModel(**kwargs)
        self.view = StudentsCitiesResidenceView(**kwargs)

        self.model.data = self.data_model
        self.data = self.data_model.get_data

    def _get_submenu_section_data(self) -> list:
        """
        Returns submenu section data
        """
        return [self.lang.get("LANG_SELECT_CITIES_RESIDENCE")]

    def _get_submenu_section_message(self) -> str:
        """
        Returns submenu option message
        """
        return self.lang.get("LANG_SELECT_OPTION")

    def _get_submenu_section_path(self, section: str) -> list:
        """
        Returns submenu city path
        """
        return [self.lang.sprintf("LANG_PATH_OPTION", section)]

    def _get_submenu_formats_path(self, section: str, formats: str) -> list:
        """
        Returns submenu formats path
        """
        return [self.lang.sprintf("LANG_PATH_OPTION", section),
                self.lang.sprintf("LANG_PATH_FORMAT", self.lang.translate(formats))]

    def _get_submenu_output_path(self, section: str, formats: str, output: str) -> list:
        """
        Returns submenu output path
        """
        return [self.lang.sprintf("LANG_PATH_OPTION", section),
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
