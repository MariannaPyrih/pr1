import sqlite3

class Person:
 
    def __init__(self, name, surname, position=1):
        self.name = name
        self.surname = surname
        self.position = position
 
    def display(self):
        return self.name, self.surname, self.position
 
    def __del__(self):
        print ('OUR WORKER IS:  {} {}\n'.format(self.name, self.surname, self.position))

p1 = Person(name = 'Marianna', surname = 'Prih', position = 'hfgu')
conn = sqlite3.connect('lab10.db')
cursor = conn.cursor()

# Створення першого запису в таблиці "вручну"
cursor.execute("""INSERT INTO lab10
VALUES ('Ivanov Ivan', 'director', 'smm')"""                )
# Створення першого запису в таблиці із екземпляра класу Worker
cursor.execute("""INSERT INTO staff                    VALUES (?,?,?)""", p1.__del__()                ) # Зберігаємо зміни conn.commit() 
 
# Вставляємо список з трьох працівників
all_workers = [(' Mykola', 'fvvrtrvu', 'smm'),
(' Inna','Njkvjed', 'secretary', ),
            ('Kolodych Leonid', 'gfbtbu', 'sql')] 
 
cursor.executemany("INSERT INTO lab10 VALUES (?,?,?)", all_workers)
conn.commit() 
 
#  Виведення на екран всіх записів 
 
print("Записи в таблиці бази даних у вигляі списка:")
sql = "SELECT * FROM lab10"
cursor.execute(sql)
print(cursor.fetchall()) 
 
# Редагування запису для конкретного працівника sql = """ UPDATE staff  SET position = 'main ingeneer'  WHERE name = 'Kolodych Leonid' """ 
 
cursor.execute(sql)
conn.commit() 
 
# Виводимо список всіх інженерів print("Список всіх ingeneer:") 
 
sql = "SELECT * FROM staff WHERE position=?"
cursor.execute(sql, [("ingeneer")])
print(cursor.fetchall()) 
 
#  Виведення на екран всіх записів 
 
print("Список всіх записів в таблиці:")
for row in cursor.execute("SELECT rowid, * FROM lab10 ORDER BY name"):
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
