from dataclasses import dataclass
from typing import Union


@dataclass
class Atleta:
    nome: str
    numidenticivil: int
    genero: str
    idade: int
    atividade: str
    fcr: int
    premios: int

    cardio_it: float = 0.75
    gordura_it: float = 0.6

    def get_fcm(self):
        if self.atividade == "Caminhada" or self.atividade == "Corrida":
            return 208.75 - (0.73 * self.idade)
        elif self.atividade == "Ciclismo":
            if self.genero == "Feminino":
                return 189 - (0.56 * self.idade)
            else:
                return 202 - (0.72 * self.idade)
        elif self.atividade == "Natacao":
            return 204 - (1.7 * self.idade)
        else:
            raise ValueError("Sem atividade associada")

    def get_gordura_fct(self) -> Union[int, float]:
        return self.fcr + (self.gordura_it * (self.get_fcm() - self.fcr))

    def get_cardio_fct(self) -> Union[int, float]:
        return self.fcr + (self.cardio_it * (self.get_fcm() - self.fcr))


if __name__ == "__main__":
    x = Atleta("Paulo", 1234567, "Masculino", 25, "Corrida", 26, 1300)
    # print(x.__dict__)
