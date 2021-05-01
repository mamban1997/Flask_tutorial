import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO iris_db (sepal_length, sepal_width,petal_length,petal_width,type_iris) VALUES (?, ?, ?, ?, ?)",
            ('7.8', '4.1', '0.3', '1.7', 'Setosa')
            )

cur.execute("INSERT INTO iris_db (sepal_length, sepal_width,petal_length,petal_width,type_iris) VALUES (?, ?, ?, ?, ?)",
            ('7.3', '3.1', '2.5', '2.3', 'Versicolor'))

connection.commit()
connection.close()