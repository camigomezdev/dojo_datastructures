""" Students By City Controller file for Dojo_Datastructures
Reto: Obtener todos los estudiantes que pertenezcan a una ciudad dada."""
from app.controllers.base_controller import BaseController
from app.models.students_by_city import StudentsByCityModel
from app.views.students_by_city import StudentsByCityView


class StudentsByCityController(BaseController):
    """ Class for Students By City Controller  """

    def __init__(self, **kwargs) -> None:
        """
        Init Students By City Controller requirements
        """
        super().__init__(**kwargs)

        self.model = StudentsByCityModel(**kwargs)
        self.view = StudentsByCityView(**kwargs)

        self.model.data = self.data_model
        self.data = self.data_model.get_data

    def _get_submenu_section_data(self) -> list:
        """
        Returns submenu section data
        """
        sections = []

        for row in self.data('list_dict'):
            if row["ciudad"] not in sections:  # Removes duplicates
                sections.append(row["ciudad"])

        return sorted(sections)

    def _get_submenu_section_message(self) -> str:
        """
        Returns submenu city message
        """
        return self.lang.get("LANG_SELECT_CITY")

    def _get_submenu_section_path(self, section: str) -> list:
        """
        Returns submenu city path
        """
        return [self.lang.sprintf("LANG_PATH_CITY", section)]

    def _get_submenu_formats_path(self, section: str, formats: str) -> list:
        """
        Returns submenu formats path
        """
        return [self.lang.sprintf("LANG_PATH_CITY", section),
                self.lang.sprintf("LANG_PATH_FORMAT", self.lang.translate(formats))]

    def _get_submenu_output_path(self, section: str, formats: str, output: str) -> list:
        """
        Returns submenu output path
        """
        return [self.lang.sprintf("LANG_PATH_CITY", section),
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
