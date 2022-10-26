class Televisao:
    def __init__(self, volume, tamanho, ligada=False, canal=1):
        self.volume = volume
        self.canal = canal
        self.tamanho = tamanho
        self.ligada = ligada

    def aumentar_volume(cls):
        if cls.volume < 99:
            cls.volume += 1

    def diminuir_volume(cls):
        if cls.volume > 0:
            cls.volume -= 1

    def modoficar_canal(cls, canal):
        if 99 <= canal >= 1:
            cls.canal = canal
        else:
            raise ValueError()

    def ligar_desligar(cls):
        if cls.ligada is False:
            cls.ligada = True
        else:
            cls.ligada = False
