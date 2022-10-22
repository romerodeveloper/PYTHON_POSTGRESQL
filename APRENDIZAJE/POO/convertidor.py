from unicodedata import name


class convertidorTemperatura:

    MAX_CELSIUS = 100
    MAX_FARENHEIT = 213

    @classmethod
    def c_f(cls, celsius):
        if celsius > cls.MAX_CELSIUS:
            raise ValueError(f'Temperatura en celsius demasiado alta: {celsius}')

        return celsius * 9/5 + 32

    @classmethod
    def f_c(cls, faren):
        if faren > cls.MAX_FARENHEIT:
            raise ValueError(f'Temperatura en farenheit demasiado alta: {faren}')
        return (faren-32) * 5/9

if __name__ == '__main__':
    resultado = convertidorTemperatura.c_f(15)
    print(f'resultado: {resultado:.2f}')
    resultado2 = convertidorTemperatura.f_c(10)
    print(f'resultado: {resultado2:.2f}')