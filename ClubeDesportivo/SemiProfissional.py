from AtletaNaoProfissional import AtletaNaoProfissional     #from ficheiro.py import Class

class SemiProfissional(AtletaNaoProfissional):

    #salario fixo de um Atleta semiprofissional
    salarioFixo = 1000

    n_semiprofissionais = 0

    def __init__(self,nome,numidenticivil,genero,idade,atividade,fcr,premios,antiguidade):
        super().__init__(nome,numidenticivil,genero,idade,atividade,fcr,premios,antiguidade)
        self.n_semiprofissionais = self.n_semiprofissionais + 1

    
    def salarioMensal(self):
        return self.salarioFixo + self.salarioAntiguidade(self.salarioFixo)


if __name__ == "__main__":
    #atletax = Atleta("Jonas","123456789","Masculino",25,"Corrida",56,1300)

    atletax = SemiProfissional("Jonas","123456789","Masculino",25,"Corrida",56,1300,12)
    atletay = SemiProfissional("Jon","1236789","Masculino",22,"Corrida",57,20,22)

    print("atletax")
    print(atletax.salarioFixo)
    print(atletax.salarioMensal())
    
    
    print("atletay")
    print(atletay.salarioFixo)
    print(atletay.salarioMensal())
    
    
    
