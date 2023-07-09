""" Menus Controller file for Py MVC Prompt Package """
# __doc__ (Menus Controller file for Py MVC Prompt Package)

import importlib


class MenusController():
    """ Class for PMVCP Menus Controller  """

    _menus = {}
    
    def __init__(self, menus: dict, **kwargs: dict) -> None:
        """
        Init PMVCP Menus Controller requirements
        """
        self._menus = menus
        self.pmvcp_model = kwargs['pmvcp_model']
        self.pmvcp_view = kwargs['pmvcp_view']
        self.pmvcp_controller = kwargs['pmvcp_controller']
        self.lang = kwargs['lang']
        self.cfg = kwargs['cfg']
        self.about = kwargs['about']

    def _go_to_menu(self) -> object:
        """
        Function to build the first level menu options        
        """
        print(self.pmvcp_view.get_intro())

        for key, value in self._get_values().items():
            print(self.pmvcp_view.get_menu_options(key, value['text']))

        self.pmvcp_view.line_brake()
        option = self.pmvcp_view.input_options()

        if option.upper() in self._menus.keys() or option.lower() in self._menus.keys():
            
            if option.lower() == 'q':
                return self._go_to_exit()
            
            task = self._get_controller(option)
            
            while self._go_to_option(task):
                break
            self.pmvcp_view.clean_screen()
            return self._go_to_menu()
    
        else:
            self.pmvcp_view.clean_screen()
            return self._go_to_menu()

    def _go_to_exit(self) -> object:
        """
        Function to show exit
        """        
        output = self.pmvcp_view.get_exit()
        output += self.pmvcp_view.line_brake(False)
        if self.cfg.get('VIEW_ABOUT_ON_EXIT', 'DEFAULT', 'boolean'):
            for key, value in self.about.to_dict().items():
                output += f'{key}: {value}\n'
        return output
    
    def _go_to_option(self, task: str) -> object:
        """
        Function to build the first level menu options
        """        
        kwargs = {'pmvcp_model': self.pmvcp_model, 'pmvcp_view': self.pmvcp_view,
                  'pmvcp_controller': self.pmvcp_controller, 'lang': self.lang,
                  'cfg': self.cfg, 'about': self.about, 'menus': self._menus}
        controller = self._import_controller(task, **kwargs)
        
        print(controller.execute())
        
        """while controller.execute():
            pass
        self.pmvcp_view.clean_screen()"""
            
        return False

    def _get_controller(self, option: str) -> str:
        return str(self._menus[option]['call'])
    
    def _get_controller_camelcase(self, controller_name: str) -> str:
        splited = controller_name.replace("_", " ").split()
        if len(controller_name) == 0:
            return controller_name
        return ''.join(i.capitalize() for i in splited[0:])  #+'Controller'
    
    def _import_controller(self, controller_name, **kwargs):
        try:
            controller_class_name = self._get_controller_camelcase(controller_name)
            app_folder = self.cfg.get("APP_FOLDER", "DEFAULT")
            module = importlib.import_module(f"{app_folder}.controllers.{controller_name}")
            controller = getattr(module, f"{controller_class_name}Controller")
        except (ImportError, AttributeError):
            raise ValueError(f"Unknown format {format!r}") from None

        return controller(**kwargs)

    def _get_values(self) -> dict:
        values = self._menus
        values['Q'] = {'text': self.lang.get('LANG_QUIT_LEYEND'), 'call': 'quit'}

        return values
