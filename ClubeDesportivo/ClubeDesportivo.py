from Atleta import Atleta  # from ficheiro.py import Class
from AtletaProfissional import AtletaProfissional
from AtletaNaoProfissional import AtletaNaoProfissional
from Amador import Amador
from SemiProfissional import SemiProfissional


class ClubeDesportivo:

    list_atletas = []

    def __init__(self, nome):
        self.nome = nome

    def adicionaAtleta(self, atleta):
        self.list_atletas.append(atleta)


if __name__ == "__main__":
    clube = ClubeDesportivo("UDB")
    print(clube.nome)

    # alinea a criação do seguinte conjunto de instâncias
    # Atleta(String nome,int numidenticivil,String genero,int idade,String atividade ,double fcr, double premios)

    ##AtletaProfissional(String nome,int numidenticivil,String genero,int idade,String atividade ,double fcr, double premios,double salariofixo)
    atleta1 = AtletaProfissional("Jonas", "123456789", "Masculino", 25, "Corrida", 56, 1300, 600)
    atleta2 = AtletaProfissional("Paulo", "987654321", "Masculino", 20, "Natacao", 66, 1000, 200)

    ##SemiProfissional(String nome,int numidenticivil,String genero,int idade,String atividade ,double fcr, double premios, int antiguidade)
    atleta3 = SemiProfissional("Marta", "123213123", "Feminino", 30, "Natacao", 71, 500, 22)
    atleta4 = SemiProfissional("Sara", "344321456", "Feminino", 45, "Corrida", 63, 121, 4)
    atleta5 = SemiProfissional("Paulo", "555555555", "Masculino", 53, "Caminhada", 62, 90, 12)

    ##Amador(String nome,int numidenticivil,String genero,int idade,String atividade ,double fcr, double premios, int antiguidade)
    atleta6 = Amador("Joao", "333333333", "Masculino", 19, "Ciclismo", 60, 2000, 8)
    atleta7 = Amador("Rita", "444444444", "Feminino", 41, "Caminhada", 59, 400, 17)
    atleta8 = Amador("Luis", "225674444", "Masculino", 31, "Ciclismo", 67, 100, 1)

    # alinea b-criação de um contentor do tipo lista e armazenamento no mesmo das instâncias criadas
    clube.adicionaAtleta(atleta1)
    clube.adicionaAtleta(atleta2)
    clube.adicionaAtleta(atleta3)
    clube.adicionaAtleta(atleta4)
    clube.adicionaAtleta(atleta5)
    clube.adicionaAtleta(atleta6)
    clube.adicionaAtleta(atleta7)
    clube.adicionaAtleta(atleta8)

    # alinea c-criação de listagens separadas, sobre o contentor, para:
    ##alinea ci-obter o nome, a FCM e as FCT de cada atleta semiprofissional e amador

    for x in clube.list_atletas:
        if isinstance(x, SemiProfissional):
            print(
                "nome:{} FCM:{} gorduraFCT:{} cardioFCT:{}".format(
                    x.nome, x.FCM(), x.gorduraFCT(), x.cardioFCT()
                )
            )

    ##alinea cii-obter o nome e o valor a pagar de cada atleta
    for x in clube.list_atletas:
        print("nome:{} salarioMensal:{} ".format(x.nome, x.salarioMensal()))

    # alinea d-apresentação das quantidades de instâncias de atletas amadores e profissionais criadas, sem percorrer o contentor
    print("Instancias atletas Amadores:{}".format(Amador.NUMERO_AMADORES))
    print("Instancias atletas Profissionais:{}".format(AtletaProfissional.NUMERO_PROFISSIONAIS))

    # alinea e-cálculo e apresentação do valor total a pagar a cada tipo de atleta
    # (profissional, semiprofissional e amador), percorrendo apenas uma vez o contentor.
    # Deve ser também calculado e apresentado o valor total a pagar a todos os atletas.

    # for atleta in clube.list_atletas:
    # print(atleta)

    # print(*clube.dic_atletas, sep="\n")
