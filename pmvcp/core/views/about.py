""" About View file for Py MVC Prompt Package """
# __doc__ (About View file for Py MVC Prompt Package)
from about import About


class AboutView():
    """ AboutView class """

    @classmethod
    def formated(cls) -> str:
        """
            Returns formated about data (str)
        """
        about = About()
        test = about.to_dict()

        for keys, values in about.items():
            return f'{keys}: {values}'

    def dummy_func(self):
        """ Dummy DocString"""
        return None


ab = AboutView()
print(ab.formated())