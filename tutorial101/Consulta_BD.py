import sqlite3

conn = sqlite3.connect("mydatabase.db")
#conn.row_factory = sqlite3.Row
cursor = conn.cursor()

sql = "SELECT * FROM albums WHERE artist=?" #Consulta
cursor.execute(sql, [("Trip Lee")]) #Nome para busca
print(cursor.fetchall()) 

print("\nHere's a listing of all the records in the table:\n") #Listagem
for row in cursor.execute("SELECT rowid, * FROM albums ORDER BY artist"): 
    print(row)

print("\nResults from a LIKE query:\n") 
sql = """
SELECT * FROM albums
WHERE title LIKE 'The%'""" #Faz a consulta para um caractere específico usando caractere% no qual todos elementos que tiverem este começo serão listados
#Para o final, basta usar %caractere
#Para ambos os lados, basta usar %caractere%
cursor.execute(sql)
print(cursor.fetchall())