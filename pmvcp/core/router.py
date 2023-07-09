""" Router file for Py MVC Prompt Package """
# __doc__ (Router file for Py MVC Prompt Package)
from pmvcp.core.controllers.base_controller import BaseController

class Router():
    """ Class for PMVCP Router  """

    def __init__(self) -> None:
        """
        Init PMVCP Router requirements
        """
        pass

    def create_app(cls) -> object:
        """
        Class-Method to route the app
        """
        controller = BaseController()
        
        print(controller.execute(task='default'))

    def dummy_func(self):
        """ Dummy DocString """
        return None
