""" Students By City Controller file for Dojo_Datastructures """
from app.models.data import DataModel


class BaseController():
    """ Class for Base Controller  """

    def __init__(self, **kwargs) -> None:
        """
        Init Base Controller requirements
        """
        self.pmvcp_model = kwargs['pmvcp_model']
        self.pmvcp_view = kwargs['pmvcp_view']
        self.pmvcp_controller = kwargs['pmvcp_controller']
        self.lang = kwargs['lang']
        self.cfg = kwargs['cfg']
        self.about = kwargs['about']
        self.menus = kwargs['menus']

        self.data_model = DataModel(**kwargs)

    def execute(self) -> str:
        """
        Excecute Base Controller
        """
        self.pmvcp_view.clean_screen()
        print(self.pmvcp_view.get_intro())

        self._get_submenu()

        return False

    def _get_submenu(self) -> None:
        """
        Returns submenu
        """
        section_data = self._get_submenu_section_data()
        section = self._get_submenu_section(
            section_data, self._get_submenu_section_message())

        formats_data = self._get_submenu_formats_data()
        formats = self._get_submenu_section(
            formats_data, self.lang.get("LANG_SELECT_FORMAT"), True, section)

        output_data = self._get_submenu_output_data()
        output = self._get_submenu_section(output_data, self.lang.get(
            "LANG_SELECT_OUTPUT"), True, section, formats)

        print(self.model.make_export(section, formats, output))
        print(self.pmvcp_view.input_pause())

    def _get_submenu_section(self, section_data: list, message: str, translate=False, *args) -> str:
        """
        Returns submenu section
        """
        section = self._get_submenu_section_value(
            section_data, message, translate)
        while section is None:
            self.pmvcp_view.clean_screen()
            print(self.pmvcp_view.get_intro())
            section = self._get_submenu_section_value(
                section_data, message, translate)

            if section is not None:
                break

        self.pmvcp_view.clean_screen()
        print(self.pmvcp_view.get_intro())

        new_args = list(args)
        new_args.append(section)
        print(self.pmvcp_view.get_path(self._get_submenu_path(*new_args)))

        return section

    def _get_submenu_section_value(self, section_data: list, message: str, translate=False) -> str:
        """
        Returns submenu section value
        """
        print(self.view.get_select_section(message))
        for index, value in enumerate(section_data, start=0):
            if translate:
                print(self.view.get_submenu_options(
                    index, self.lang.translate(value)))
            else:
                print(self.view.get_submenu_options(index, value))
        section_input = self.view.input_option()

        check = self._get_submenu_section_check(section_input, section_data)
        while check:
            if check is True:
                return section_data[int(section_input)]
        return None

    def _get_submenu_section_check(self, section_input, temp_dict) -> bool:
        """
        Returns submenu section loop check
        """
        return section_input.isnumeric() and int(section_input) >= 0 and int(section_input) < len(temp_dict)

    def _get_submenu_section_data(self) -> None:
        """
        Returns submenu section data
        """
        return None

    def _get_submenu_formats_data(self) -> list:
        """
        Returns submenu formats data
        """
        return ['table', 'dictionary', 'csv', 'json']

    def _get_submenu_output_data(self) -> list:
        """
        Returns submenu output data
        """
        return ['screen', 'file']

    def _get_submenu_section_message(self) -> None:
        """
        Returns submenu option message
        """
        return None

    def _get_submenu_section_path(self, section: str) -> None:
        """
        Returns submenu section path
        """
        return None

    def _get_submenu_formats_path(self, section: str, formats: str) -> None:
        """
        Returns submenu formats path
        """
        return None

    def _get_submenu_output_path(self, section: str, formats: str, output: str) -> None:
        """
        Returns submenu output path
        """
        return None

    def _get_submenu_path(self, *args) -> None:
        """
        Returns submenu path
        """
        return None
