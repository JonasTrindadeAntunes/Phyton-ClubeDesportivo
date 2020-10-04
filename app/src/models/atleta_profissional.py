from typing import Union

from src.models.atleta import Atleta


class AtletaProfissional:
    pct_premios: float = 0.2

    def __init__(self, atleta: Atleta, salario_fixo: int):
        self.atleta = atleta
        self.salario_fixo = salario_fixo

    @property
    def salario_premios(self) -> Union[int, float]:
        return self.atleta.premios * self.pct_premios

    @property
    def salario_mensal(self) -> Union[int, float]:
        return self.salario_fixo * self.salario_premios


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
    y = AtletaProfissional(atleta=x, salario_fixo=1000)
    # print(x.__dict__)
    # print(y.__dict__)
