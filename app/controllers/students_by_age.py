""" Students By Age Controller file for Dojo_Datastructures
Reto: Obtener todos los estudiantes que estén dentro del rango de edades dado."""
from app.controllers.base_controller import BaseController
from app.models.students_by_age import StudentsByAgeModel
from app.views.students_by_age import StudentsByAgeView


class StudentsByAgeController(BaseController):
    """ Class for Students By Age Controller  """

    def __init__(self, **kwargs) -> None:
        """
        Init Students By Age Controller requirements
        """
        super().__init__(**kwargs)

        self.model = StudentsByAgeModel(**kwargs)
        self.view = StudentsByAgeView(**kwargs)

        self.model.data = self.data_model
        self.data = self.data_model.get_data

    def _get_submenu_section_data(self) -> list:
        """
        Returns submenu section data
        """
        sections = []

        for row in self.data('list_dict'):
            if row["edad"] not in sections:  # Removes duplicates
                sections.append(row["edad"])

        return sorted(sections)

    def _get_submenu_section_message(self) -> str:
        """
        Returns submenu age message
        """
        return self.lang.get("LANG_SELECT_AGE")

    def _get_submenu_section_path(self, section: str) -> list:
        """
        Returns submenu age path
        """
        return [self.lang.sprintf("LANG_PATH_AGE", section)]

    def _get_submenu_formats_path(self, section: str, formats: str) -> list:
        """
        Returns submenu formats path
        """
        return [self.lang.sprintf("LANG_PATH_AGE", section),
                self.lang.sprintf("LANG_PATH_FORMAT", self.lang.translate(formats))]

    def _get_submenu_output_path(self, section: str, formats: str, output: str) -> list:
        """
        Returns submenu output path
        """
        return [self.lang.sprintf("LANG_PATH_AGE", section),
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
