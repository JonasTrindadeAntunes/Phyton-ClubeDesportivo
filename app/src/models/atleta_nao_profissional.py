from typing import Union

from src.models.atleta import Atleta


class AtletaNaoProfissional:
    pct_minima: float = 0.02
    pct_media: float = 0.08
    pct_maxima: float = 0.2

    def __init__(self, atleta: Atleta, antiguidade: int):
        self.atleta = Atleta
        self.antiguidade = antiguidade

    @property
    def salario_antiguidade(self, valor: int) -> Union[int, float]:
        if self.antiguidade >= 5 and self.antiguidade <= 10:
            return valor * self.pct_minima
        elif self.antiguidade > 10 and self.antiguidade <= 20:
            return valor * self.pct_media
        elif self.antiguidade > 20:
            return valor * self.pct_maxima

        return 0


if __name__ == "__main__":
    x = Atleta(
        nome="Paulo",
        numidenticivil=1234567,
        genero="Masculino",
        idade=25,
        atividade="Corrida",
        fcr=56,
        premios=1300,
    )
    y = AtletaNaoProfissional(atlteta=x, antiguidade=10)
    # print(x.__dict__)
    # print(y.__dict__)
