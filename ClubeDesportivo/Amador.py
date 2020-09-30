from AtletaNaoProfissional import AtletaNaoProfissional     #from ficheiro.py import Class


class Amador(AtletaNaoProfissional):

    salariominimo = 5
   
    # O valor desta percentagem pode ser atualizado, e é igual para todos os atletas
    # percentagem aplicada aos premios do atleta no mes
    percentagem_variavel = 0.07             
    
    NUMERO_AMADORES = 0
    

    def __init__(self,nome,numidenticivil,genero,idade,atividade,fcr,premios,antiguidade):
        super().__init__(nome,numidenticivil,genero,idade,atividade,fcr,premios,antiguidade)
        self.NUMERO_AMADORES += 1

    # retorna a parcela ganha dos premios pelo atleta de acordo com a com uma percentagem
    def salarioPremios(self):
        return self.getPremios() * self.percentagem_variavel 

    def salarioMensal(self):
        if(self.salarioAntiguidade(self.premios) + self.salarioPremios() < 5):
            return 5
        else:
            return self.salarioAntiguidade(self.premios) + self.salarioPremios()



if __name__ == "__main__":
    #atletax = Atleta("Jonas","123456789","Masculino",25,"Corrida",56,1300)

    atletax = Amador("Jonas","123456789","Masculino",25,"Corrida",56,1500,12)
    atletay = Amador("Jonas","123456789","Masculino",25,"Corrida",56,100,20)

    print(atletax.getPremios())
    print(atletax.salarioPremios())
    print(atletax.salarioMensal())
    print(atletay.salarioMensal())
    

    