""" Filters Helper file for Py MVC Prompt Package """
# __doc__ (Filters Helper file for Py MVC Prompt Package)

from helpers.base_helper import BaseHelper


class Filters(BaseHelper):
    """ Class for Filters Helper  """

    def float_int(self, value: float | int):
        """
        Returns a float or int value
        """
        try:
            value_str = str(value)

            if value_str.replace('.', '', 1).isdigit():
                return float(value)

            if value_str.isnumeric():
                return int(value)

            raise Exception(f'Error: {value}')
        except Exception as error:
            raise error

    def dummy_func(self):
        """ Dummy DocString"""
        return None
