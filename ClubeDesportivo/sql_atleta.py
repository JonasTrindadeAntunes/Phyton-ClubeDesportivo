import sqlite3
from Atleta import Atleta

conn = sqlite3.connect(":memory:")
cursor_atleta = conn.cursor()

cursor_atleta.execute(
    """CREATE TABLE Atleta (
    nome text,
    numidenticivil integer,
    genero text,
    idade integer,
    atividade text,
    fcr integer,
    premios integer
    )"""
)

atletax = Atleta("Jonas", 123456789, "Masculino", 25, "Corrida", 56, 1300)
atletay = Atleta("paulo", 987654321, "Masculino", 26, "Natacao", 66, 1000)

cursor_atleta.execute(
    "INSERT INTO Atleta VALUES ('{}',{},'{}',{},'{}',{},{})".format(
        atletax.nome,
        atletax.numidenticivil,
        atletax.genero,
        atletax.idade,
        atletax.atividade,
        atletax.fcr,
        atletax.premios,
    )
)
conn.commit()
cursor_atleta.execute(
    "INSERT INTO Atleta VALUES (:nome, :numidenticivil, :genero, :idade, :atividade, :fcr, :premios)",
    {
        "nome": atletay.nome,
        "numidenticivil": atletay.numidenticivil,
        "genero": atletay.genero,
        "idade": atletay.idade,
        "atividade": atletay.atividade,
        "fcr": atletay.fcr,
        "premios": atletay.premios,
    },
)
conn.commit()


def getNome(self):
    cursor_atleta.execute("SELECT * FROM Atleta Where nome:= nome", {"nome": self.nome})
    return cursor_atleta.fetchall()


conn.close()
