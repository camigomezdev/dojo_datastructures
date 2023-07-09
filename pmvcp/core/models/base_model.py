""" Base Model file for Py MVC Prompt Package """
# __doc__ (Base Model file for Py MVC Prompt Package)


class BaseModel():
    """ Class for PMVCP Base Model  """

    def __init__(self, **kwargs) -> None:
        """
        Init the PMVCP Base Model requirements
        """
        self.lang = kwargs['lang']
        self.cfg = kwargs['cfg']
        self.about = kwargs['about']

    @property
    def test(self) -> str:
        """
        Testing function
        """
        return 'Hello from PMVCP Base Model!'
