""" Base Controller file for Py MVC Prompt Package """
# __doc__ (Base Controller file for Py MVC Prompt Package)

from pmvcp.core.controllers.menus import MenusController
from pmvcp.core.models.base_model import BaseModel
from pmvcp.core.models.about import About
from pmvcp.core.models.menus import Menus
from pmvcp.core.models.configuration import Configuration
from pmvcp.core.models.language import Language
from pmvcp.core.views.base_view import BaseView


class BaseController():
    """ Class for PMVCP Base Controller  """
    _name = ''
    _task = ''

    def __init__(self) -> None:
        """
        Init the PMVCP Base Controller requirements
        """
        self.cfg = Configuration()
        self.lang = Language(self.cfg)
        self.lang.tag = 'en'
        self.about = About(self.cfg)
        self.menus_model = Menus(self.cfg)
        
        self.kwargs = {'lang': self.lang, 'cfg': self.cfg, 'about': self.about}

        self.model = self._get_model(**self.kwargs)
        self.view = self._get_view(**self.kwargs)

    def execute(self, task: str) -> object:
        """
        Executes the PMVCP Base Controller
        """
        self.view.clean_screen()
        print(self.view.get_intro())

        curr_lang = self.view.input_language()        
        curr_lang = self.current_language(curr_lang)

        self.lang.tag = curr_lang
        self.lang.update

        self.about.tag = curr_lang
        self.about.update

        if task == 'default':    
            self.menus_model.tag = curr_lang
            self.menus_model.update
            
            kwargs_menus = {'pmvcp_model': self.model,
                            'pmvcp_view': self.view,
                            'pmvcp_controller': self}
            kwargs_menus.update(self.kwargs)
            self.kwargs.clear()
            menus = self._get_menu(self.menus_model.to_dict(True), **kwargs_menus)

            self.view.input_start()
            self.view.clean_screen()

            return menus._go_to_menu()

        return menus._go_to_option(task)

    def _get_model(self, **kwargs) -> object:
        """
        Returns the PMVCP Base Model
        """
        return BaseModel(**kwargs)

    def _get_view(self, **kwargs) -> object:
        """
        Returns the PMVCP Base View
        """
        return BaseView(**kwargs)

    def _get_menu(self, menus: dict, **kwargs: dict) -> object:
        """
        Executes the PMVCP Menus Controller
        """
        return MenusController(menus, **kwargs)
    
    def current_language(self, key: str) -> str:
        """
        Function to return current short language tag from input
        * -> Refactor!!!
        """
        if key == '1':
            return 'en'
        elif key == '2':
            return 'es'
        else:
            return self.cfg.get('DEFAULT_LANGUAGE', 'LANGUAGE')

    @property
    def test(self) -> str:
        """
        Testing function
        """
        return 'Hello from PMVCP Base Controller!'
