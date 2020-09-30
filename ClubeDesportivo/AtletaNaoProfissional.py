from Atleta import Atleta       #from ficheiro.py import Class

class AtletaNaoProfissional(Atleta):

    percentagem_minima = 0.02
    percentagem_media = 0.08
    percentagem_maxima = 0.2

    # param nome o nome do atleta
    # param numidenticivil o numero de identificação civil do atleta
    # param genero o genero do atleta
    # param idade a idade do atleta
    # param atividade a atividade do atleta
    # param fcr a frequencia cardiaca de repouso do atleta
    # param premios o valor mensal arrecadado em prémios no mes pelo atleta
    #param antiguidade a antiguidade de um atleta nao profissional
    def __init__(self,nome,numidenticivil,genero,idade,atividade,fcr,premios,antiguidade):
        self.antiguidade = antiguidade
        super().__init__(nome,numidenticivil,genero,idade,atividade,fcr,premios)


    # A property is just like a getter.
    # It turns the method age() into an read-only attribute of the same name.
    # There's no need to write trivial getters and setters in Python, though.

    def getAntiguidade(self):
        return self.antiguidade
    
    # This allows the property to be set
    def setAntiguidade(self,antiguidade):
        self.antiguidade = antiguidade

    # retorna parte do salario ganho pelo atleta de acordo com a antiguidade
    def salarioAntiguidade(self,valor):
        if   (self.antiguidade >= 5 and self.antiguidade <= 10):
            return valor * self.percentagem_minima
        elif (self.antiguidade > 10 and self.antiguidade <= 20):
            return valor * self.percentagem_media
        elif (self.antiguidade > 20):
            return valor * self.percentagem_maxima
        else:
            return 0
            
        
    def __repr__(self):
        return (super().__repr__() + f'antiguidade: {self.antiguidade!r}')


if __name__ == "__main__":
    atletax = AtletaNaoProfissional("Jonas","123456789","Masculino",25,"Corrida",56,1300,12)

    print(atletax.getPremios())
    print(atletax.getAntiguidade())
    print(atletax.salarioAntiguidade(1000))
    