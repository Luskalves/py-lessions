from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    idade: int


class Luska(Pessoa):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()


luska = Luska('luska', 21)

print(luska.nome)
