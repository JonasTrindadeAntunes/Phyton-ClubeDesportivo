from Atleta import Atleta  # from ficheiro.py import Class


class AtletaProfissional(Atleta):

    percentagem_Premios = 0.20

    NUMERO_PROFISSIONAIS = 0

    def __init__(self, nome, numidenticivil, genero, idade, atividade, fcr, premios, salariofixo):
        self.salariofixo = salariofixo
        super().__init__(nome, numidenticivil, genero, idade, atividade, fcr, premios)
        self.NUMERO_PROFISSIONAIS += 1

    def salarioPremios(self):
        return self.premios * self.percentagem_Premios

    def salarioMensal(self):
        return self.salariofixo + self.salarioPremios()

    def __repr__(self):
        return super().__repr__() + f"salariofixo: {self.salariofixo!r}"


if __name__ == "__main__":
    atletax = AtletaProfissional("Jonas", "123456789", "Masculino", 25, "Corrida", 56, 1000, 500)

    print(atletax.salarioPremios())
    print(atletax.salarioMensal())
