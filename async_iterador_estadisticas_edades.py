""" Iterador asíncrono que regresa la media, mediana, moda, max, min,
    desviación estándar muestral y poblacional de las edades por carrera
    leyendo un diccionario con el nombre de cada carrera como llave
    y una lista con las edades por carrera como valor """

import asyncio


class AsyncIteradorEstadisticasEdades:
    """Definición de la clase Async Iterador Estadisticas Edades"""

    def __init__(self, diccionario):
        self._dic = diccionario
        self._indice = 0

    def __aiter__(self):
        return self

    def media(self, iterable):
        acumulador = 0
        for lista in iterable:
            for edad in lista:
                acumulador += int(edad)
        return round(acumulador/len(lista))

    def mediana(self, iterable):
        for lista in iterable:
            lista.sort()
            mitad = len(lista) // 2
            mediana = (lista[mitad] + lista[~mitad]) / 2
        return mediana

    def moda(self, iterable):
        for lista in iterable:
            return max(set(lista), key=lista.count)

    def min(self, iterable):
        for lista in iterable:
            return min(lista)

    def max(self, iterable):
        for lista in iterable:
            return max(lista)

    def desviacion_estandar_muestral(self, iterable):
        for lista in iterable:
            return (sum((x-(sum(lista) / len(lista)))**2 for x in lista) /
                    (len(lista)-1))**0.5

    def desviacion_estandar_poblacional(self, iterable):
        for lista in iterable:
            return (sum((x-(sum(lista) / len(lista)))**2 for x in lista) /
                    (len(lista)))**0.5

    async def __anext__(self):
        if self._indice < len(self._dic):
            await asyncio.sleep(0, media := self.media(self._dic[valor]
                                for indice, valor
                                in enumerate(self._dic)
                                if indice == self._indice))
            await asyncio.sleep(0, mediana := self.mediana(self._dic[valor]
                                for indice, valor
                                in enumerate(self._dic)
                                if indice == self._indice))
            await asyncio.sleep(0, moda := self.moda(self._dic[valor]
                                for indice, valor
                                in enumerate(self._dic)
                                if indice == self._indice))
            await asyncio.sleep(0, min_edad := self.min(self._dic[valor]
                                for indice, valor
                                in enumerate(self._dic)
                                if indice == self._indice))
            await asyncio.sleep(0, max_edad := self.max(self._dic[valor]
                                for indice, valor
                                in enumerate(self._dic)
                                if indice == self._indice))
            await asyncio.sleep(0, desviacion_estandar_muestral :=
                                self.desviacion_estandar_muestral(
                                    self._dic[valor]
                                    for indice, valor
                                    in enumerate(self._dic)
                                    if indice == self._indice))
            await asyncio.sleep(0, desviacion_estandar_poblacional :=
                                self.desviacion_estandar_poblacional(
                                    self._dic[valor]
                                    for indice, valor
                                    in enumerate(self._dic)
                                    if indice == self._indice))
            for indice, valor in enumerate(self._dic.keys()):
                if indice == self._indice:
                    carrera = valor
            self._indice += 1
            return (carrera, media, mediana, moda, min_edad, max_edad,
                    desviacion_estandar_muestral,
                    desviacion_estandar_poblacional)
        else:
            raise StopAsyncIteration
