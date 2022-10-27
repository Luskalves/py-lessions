from abc import ABC, abstractmethod


class Grafico(ABC):
    @abstractmethod
    def desenhar(self):
        raise NotImplementedError


class GraficoBarras(Grafico):
    def __init__(self, /, dados):
        self.dados = dados

    def desenhar(self):
        print("Lógica para desenhar o gráfico de barras")


class GraficoRadar(Grafico):
    def __init__(self, dados):
        self.dados = dados

    def desenhar(self):
        print("Lógica para desenhar o gráfico de Pizza")


