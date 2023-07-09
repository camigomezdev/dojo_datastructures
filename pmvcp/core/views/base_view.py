""" Base View file for Py MVC Prompt Package """
# __doc__ (Base View file for Py MVC Prompt Package)

import os

from pmvcp.core.decorators.decorators_views import decorate_intro


class BaseView:
    """ Class for PMVCP Base View  """

    def __init__(self, **kwargs) -> None:
        """
        Init the PMVCP Base View requirements
        """
        self.lang = kwargs['lang']
        self.cfg = kwargs['cfg']
        self.about = kwargs['about']

    @decorate_intro(num_lines=3)
    def get_intro(self, dummy='') -> str:
        """
        Function to get intro view message (str)
        """
        title = self.cfg.get("DEFAULT_TITLE", "DEFAULT")
        padding_left = self.cfg.get("PADDING_LEFT", "DEFAULT", "int")

        return title.center(padding_left)+'\n'

    @decorate_intro(num_lines=1)
    def get_exit(self, dummy='') -> str:
        """
        Function to get exit view message (str) -> LANG_EXIT_PROGRAM
        """
        self.clean_screen()
        return f' >>> {self.lang.get("LANG_EXIT_PROGRAM")} \n'

    def get_menu_options(self, key: str, value: str) -> str:
        """
        Function to get menu options view formated (str)
        """
        return f'[{key}] {value} '
    
    def get_path(self, sections: list) -> str:
        """
        Function to get path (str)
        """
        path = ''
        i = 0

        for section in sections:
            if i == 0:
                path += f'>>> {str(section)}'

            if i >= 1:                
                path += f' -> {str(section)}'
                
            i +=1

        return path

    def line_brake(self, prints=True) -> str:
        """
        Function to get a linebrake in view (str)
        """
        if prints:
            print('\n', end='')
            return ''
        else:
            return '\n'
    
    def input_start(self) -> str:
        """
        Returns the select option input (str)
        """
        return input(f'{self.lang.get("LANG_INPUT_PRESS_A_KEY_START")} ')

    def input_language(self) -> str:
        """
        Returns the select option input (str)
        """
        return input(f'{self.lang.get("LANG_SELECT_LANGUAGE")} ')

    def input_options(self) -> str:
        """
        Returns the select option input (str)
        """
        return input(f'{self.lang.get("LANG_INPUT_SELECT_OPTION")} ')

    def input_pause(self) -> str:
        """
        Returns the intro press a key pause (str)
        """
        return input(f'{self.lang.get("LANG_INPUT_PRESS_A_KEY_CONTINUE")} ')

    def input_generic(self, text: str) -> str:
        """
        Returns the pause option to repeat binary search (str)
        """
        return input(text)

    def clean_screen(self) -> object:
        """
        Makes a screen clear in view. Calls cls for Windows
        and clear for Unix/Linux (object)
        """
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    @property
    def test(self) -> str:
        """
        Testing function
        """
        return 'Hello from PMVCP Base View!'
