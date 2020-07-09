import sqlite3

class Person:
 
    def __init__(self, name, surname, position=1):
        self.name = name
        self.surname = surname
        self.position = position
 
    def display(self):
        return self.name, self.surname, self.position
 
    def __del__(self):
       return self.name, self.surname, self.position

p1 = Person(name = 'Dmytro', surname = 'Dmytrenko', position = 'main engineer')
conn = sqlite3.connect('lab10_db.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE lab10_11                  (name text, surname text, position text)                """)
# Створення першого запису в таблиці "вручну"
cursor.execute("""INSERT INTO lab10_11
VALUES ('Ivanov Ivan', 'director', 'smm')"""                )
# Створення першого запису в таблиці із екземпляра класу Worker
cursor.execute("""INSERT INTO lab10_11                    VALUES (?,?,?)""", p1.__del__()                ) # Зберігаємо зміни
conn.commit() 
 
# Вставляємо список з трьох працівників
all_workers = [(' Mykola', 'Mykolenko', 'smm'),
(' Inna','Savchuk', 'secretary', ),
            ('Khrystyna', 'Shved', 'smm')] 
 
cursor.executemany("INSERT INTO lab10_11 VALUES (?,?,?)", all_workers)
conn.commit() 
 
#  Виведення на екран всіх записів 
 
print("Записи в таблиці бази даних у вигляі списка:")
sql = "SELECT * FROM lab10_11"
cursor.execute(sql)
print(cursor.fetchall())
print('____________________________________________________________________________')
 
# Редагування запису для конкретного працівника
sql = """ UPDATE lab10_11  SET position = 'main secretary'  WHERE position = 'secretary' """ 
 
cursor.execute(sql)
conn.commit() 
 
# Виводимо список всіх інженерів
print("Список всіх smm:")

 
sql = "SELECT * FROM lab10_11 WHERE position=?"
cursor.execute(sql, [("smm")])
print(cursor.fetchall())
print('____________________________________________________________________________')

#Видалення певного запису
sql = "DELETE FROM lab10_11 WHERE name = 'Ivanov Ivan'"

cursor.execute(sql)
conn.commit()
 
#  Виведення на екран всіх записів 
 
print("Список всіх записів в таблиці:")
for row in cursor.execute("SELECT rowid, * FROM lab10_11 ORDER BY name"):
    print(row) 

 
p1 = Person('nina', 'prih', 'developer')
print (p1.display())
 
p2 = Person('petro', 'ivaniv', 'smm')
print (p2.display())
 
p3 = Person('dmtro', 'vik', 'engineer')
print (p3.display())
 
del p1 

try:
    input("Press Enter and exit")
except SyntaxError:
    exit()
