import sqlite3
from Atleta import Atleta

conn = sqlite3.connect(':memory:')
cursor_atleta = conn.cursor()

cursor_atleta.execute("""CREATE TABLE Atletas (
    nome text,
    numidenticivil integer,
    genero text,
    idade integer,
    atividade text,
    fcr integer,
    premios integer
    )""")


def insert_atleta(atleta):
    with conn:
        cursor_atleta.execute("INSERT INTO Atletas VALUES (:nome, :numidenticivil, :genero, :idade, :atividade, :fcr, :premios)",
                                                                                                                        {'nome': atleta.nome,
                                                                                                                        'numidenticivil': atleta.numidenticivil,
                                                                                                                        'genero': atleta.genero,
                                                                                                                        'idade': atleta.idade,
                                                                                                                        'atividade': atleta.atividade,
                                                                                                                        'fcr': atleta.fcr,
                                                                                                                        'premios': atleta.premios})

def get_atletas_pelo_nome(nome):
    cursor_atleta.execute("SELECT * FROM Atletas WHERE nome= :nome",{'nome': nome})
    return cursor_atleta.fetchall()

def update_premios(atleta,premios):
    with conn:
        cursor_atleta.execute("""UPDATE Atletas SET premios= :premios
                                WHERE nome= :nome AND numidenticivil= :numidenticivil""",
                                    {'nome': atleta.nome, 'numidenticivil': atleta.numidenticivil, 'premios': premios})

def remove_atleta(atleta):
    with conn:
        cursor_atleta.execute("DELETE FROM Atletas WHERE nome= :nome AND numidenticivil= :numidenticivil",
                                {'nome': atleta.nome, 'numidenticivil': atleta.numidenticivil})

atletax = Atleta('Jonas',123456789,'Masculino',25,'Corrida',56,1300)
atletay = Atleta('Paulo',987654321,'Masculino',26,'Natacao',66,1000)
insert_atleta(atletax)
insert_atleta(atletay)

cursor_atleta.execute("SELECT * FROM Atletas")
print(cursor_atleta.fetchall())

atleta= get_atletas_pelo_nome('Jonas')
print(atleta)

update_premios(atletax,3200)


atleta= get_atletas_pelo_nome('Jonas')
print(atleta)

print(atleta[0])
print(atleta[0])
print(atleta[0])

remove_atleta(atletax)
atleta= get_atletas_pelo_nome('Jonas')
print(atleta)

##################################[('Paulo', 987654321, 'Masculino', 26, 'Natacao', 66, 1000)]
cursor_atleta.execute("SELECT * FROM Atletas")
print(cursor_atleta.fetchall())


conn.close()