import sqlite3

def creer_table():
    conn = sqlite3.connect('eleves.db')
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS Eleve")
    cur.execute("""CREATE TABLE Eleve (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT,
        prenom TEXT,
        age INTEGER,
        classe TEXT)
        """)
    conn.close()

creer_table()

conn = sqlite3.connect('eleves.db')
cur = conn.cursor()

cur.execute("""INSERT INTO Eleve (id, nom, prenom, age, classe) 
    VALUES (1, 'Dupont', 'Jean', 15, '2A')""")
conn.commit()

eleve_2 = ('Dupont', 'Jeanne', 17, 'TG2')
cur.execute("""INSERT INTO Eleve (nom, prenom, age, classe) 
    VALUES (?, ?, ?, ?)""", eleve_2)
conn.commit()

eleve_3 = {'nom': 'Marchand', 'prenom': 'Marie', 'age': 15, 'classe': '2A'}
cur.execute("""INSERT INTO Eleve (nom, prenom, age, classe) 
    VALUES (:nom, :prenom, :age, :classe)""", eleve_3)
conn.commit()

autres_eleves = [
    ('Martin', 'Adeline', 16, '1G1'),
    ('Dupont', 'Lucas', 15, '2A'),
    ('Richard', 'Louise', 15, '1G2'),
    ('Rouger', 'Marius', 16, '1G2'),
    ('Louapre', 'Lola', 18, 'TG2'),
    ('Boudou', 'Lise', 17, 'TG1'),
    ('Dupont', 'Aurélien', 16, '1G1'),
    ('Laurent', 'Diego', 17, '1G2'),
    ('Martin', 'Anaëlle', 16, 'TG1')
]

# for eleve in autres_eleves:
#     cur.execute("""INSERT INTO Eleve (nom, prenom, age, classe) 
#         VALUES (?, ?, ?, ?)""", eleve)
# conn.commit()

cur.executemany("""INSERT INTO Eleve (nom, prenom, age, classe) 
    VALUES (?, ?, ?, ?)""", autres_eleves)
conn.commit()


# res = cur.execute("SELECT * FROM Eleve")
# print(res.fetchall())
# print(list(res))
# print(res.fetchone())
# print(res.fetchone())
# print(res.fetchmany(3))
# print(res.fetchmany(3))

# res = cur.execute("SELECT id, nom, prenom FROM Eleve WHERE nom = ?", ('Dupont',))
# print(res.fetchall())

# res = cur.execute("SELECT id, nom, prenom FROM Eleve WHERE nom = :nom", {'nom': 'Dupont'})
# print(res.fetchall())

def recuperer_eleves_par_nom(nom):
    conn = sqlite3.connect('eleves.db')
    cur = conn.cursor()
    res = cur.execute("SELECT id, nom, prenom FROM Eleve WHERE nom = ?", (nom, ))
    eleves = res.fetchall()  # on stocke les résultats pour pouvoir les renvoyer
    conn.close()  
    return eleves  # après avoir fermé la connexion

print(recuperer_eleves_par_nom('Martin'))
print(recuperer_eleves_par_nom('Richard'))
print(recuperer_eleves_par_nom('Obama'))

conn.close()