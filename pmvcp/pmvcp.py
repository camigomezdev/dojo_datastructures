""" Py_MVC_Prompt file for Py MVC Prompt Package """
# __doc__ (Py_MVC_Prompt file for Py MVC Prompt Package)
from pmvcp.core.router import Router


def main():
    """
       Main function, returns pmvcp example
    """
    app = Router()
    app.create_app()
