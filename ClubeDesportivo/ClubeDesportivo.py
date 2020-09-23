from Atleta import Atleta       #from ficheiro.py import Class


class ClubeDesportivo:

    def __init__(self,nome):
        self.nome = nome


if __name__ == "__main__":
    clube = ClubeDesportivo("UDB")
    print(clube.nome)

    atletax = Atleta("Jonas","123456789","Masculino",25,"Corrida",56,1300)
 
    print(atletax.nome)

