""" Iterador que regresa el valor promedio de edades por carrera
    leyendo un diccionario con el nombre de cada carrera como llave
    y una lista con las edades como valor """


class IteradorPromedioEdades:
    """Definición de la clase Iterador Promedio"""

    def __init__(self, diccionario):
        self._dic = diccionario
        self._indice = 0

    def __iter__(self):
        return self

    def promedio(self, iterable):
        acumulador = 0
        for lista in iterable:
            for edad in lista:
                acumulador += int(edad)
        return round(acumulador/len(lista))

    def __next__(self):
        if self._indice < len(self._dic):
            valor_promedio = self.promedio(self._dic[valor]
                                           for indice, valor
                                           in enumerate(self._dic)
                                           if indice == self._indice)
            for indice, valor in enumerate(self._dic.keys()):
                if indice == self._indice:
                    carrera = valor
            self._indice += 1
            return carrera, valor_promedio
        else:
            raise StopIteration
