class Atleta:

    # param nome o nome do atleta
    # param numidenticivil o numero de identificação civil do atleta
    # param genero o genero do atleta
    # param idade a idade do atleta
    # param atividade a atividade do atleta
    # param fcr a frequencia cardiaca de repouso do atleta
    # param premios o valor mensal arrecadado em prémios no mes pelo atleta
    def __init__(self,nome,numidenticivil,genero,idade,atividade,fcr,premios):
        self.nome = nome
        self.numidenticivil = numidenticivil
        self.genero = genero
        self.idade = idade
        self.atividade =atividade
        self.fcr = fcr
        self.premios = premios


    # A property is just like a getter.
    # It turns the method age() into an read-only attribute of the same name.
    # There's no need to write trivial getters and setters in Python, though.
    def getNome(self):
        return self.nome
    
    def getNumidenticivil(self):
        return self.numidenticivil
   
    def getGenero(self):
        return self.genero
       
    def getIdade(self):
        return self.idade

    def getAtividade(self):
        return self.atividade
    
    def getFCR(self):
        return self.fcr
    
    def getPremios(self):
        return self.premios


    # This allows the property to be set
    def setNome(self,nome):
        self.nome = nome

    def setNumidenticivil(self,numidenticivil):
        self.numidenticivil = numidenticivil
    
    def setGenero(self,genero):
        self.genero = genero

    def setIdade(self,idade):
        self.idade = idade

    def setAtividade(self,atividade):
        self.atividade = atividade
    
    def setFCR(self,fcr):
        self.fcr = fcr

    def setPremios(self,premios):
        self.premios = premios




if __name__ == "__main__":
    atletax = Atleta("Jonas","123456789","Masculino",25,"Corrida",56,1300)
   
    print(atletax.getNome())
    print(atletax.getIdade())
    print(atletax.nome)
