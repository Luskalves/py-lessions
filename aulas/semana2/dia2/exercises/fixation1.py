
class Calculadora:
    def soma(self, x, y):
        return x + y


class CalculadoraDecorada:
    def __init__(self, calculadora):
        self.calculadora = calculadora

    def converterNumero(self, numero):
        if not isinstance(numero, str):
            return numero
        return {
            "um": 1, "dois": 2, "três": 3, "quatro": 4, "cinco": 5,
            "seis": 6, "sete": 7, "oito": 8, "nove": 9, "dez": 10,
        }.get(numero)

    def soma(self, x, y):
        return self.calculadora.soma(
            self.converterNumero(x), self.converterNumero(y)
        )


class CalculadoraDecoradaButENGLISH:
    def __init__(self, calculator):
        self.calculator = calculator

    def convertNumber(cls, number):
        if not isinstance(number, str):
            return number

        return {
            "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
            "sex": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10
        }.get(number)

    def sum(cls, x, y):
        return cls.calculator.soma(
            cls.convertNumber(x), cls.convertNumber(y)
        )


c1 = Calculadora()
c2 = CalculadoraDecorada(c1)
c3 = CalculadoraDecoradaButENGLISH(c1)


print("Primeira soma: ", c1.soma(1, 2))
print("Segunda soma: ", c2.soma("um", "dois"))
print("ENGLISH MOTHERT FUCKER", c3.sum("one", "two"))
