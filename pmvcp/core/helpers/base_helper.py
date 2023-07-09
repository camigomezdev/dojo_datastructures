""" Base Helper file for Py MVC Prompt Package """
# __doc__ (Base Helper file for Py MVC Prompt Package)


class BaseHelper():
    """ Class for Base Helper  """

    def __init__(self, **kwargs) -> None:
        """
        Init BaseHelper requirements
        """
        self.lang = kwargs['lang']
        self.cfg = kwargs['cfg']
        self.about = kwargs['about']

    @property
    def test(self) -> str:
        """
        Testing function
        """
        return 'Hello from PMVCP Base Helper!'
