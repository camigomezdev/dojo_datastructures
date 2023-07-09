""" Base View file for Dojo_Datastructures """


class BaseView():
    """ Class for Base View  """

    def __init__(self, **kwargs) -> None:
        """
        Init Base View requirements
        """
        self.pmvcp_model = kwargs['pmvcp_model']
        self.pmvcp_view = kwargs['pmvcp_view']
        self.pmvcp_controller = kwargs['pmvcp_controller']
        self.lang = kwargs['lang']
        self.cfg = kwargs['cfg']
        self.about = kwargs['about']
        self.menus = kwargs['menus']

    def input_option(self) -> str:
        """
        Function to get only city path formated (str)
        """
        return input(f'{self.lang.get("LANG_OPTION")} ')

    def get_select_section(self, message: str) -> str:
        """
        Function to get only city path formated (str)
        """
        return f'[>] {message} '

    def get_submenu_options(self, index: int, value: str) -> str:
        """
        Function to get only city path formated (str)
        """
        return f'[{index}] {value} '
