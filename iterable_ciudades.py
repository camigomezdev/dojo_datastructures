""" Lista iterable para ciudades """


class IterableCiudades:
    def __init__(self, sequence=[]):
        self._item = sequence

    def __iter__(self):
        return iter(self._item)
