import os.path # Модуль, який містить функції для роботи з шляхом у файловій системі 
import datetime
import glob
import linecache

text = '''Prih Marianna-5 \nHrsh Nastia-5 \nBratakh Tania-5 \n'''
def write_text_to_file(filename, text):
    """Функція для запису у файл filename рядка text"""
    f = open(filename, "w")  # відкриття файла для запису
    f.write(text)  # Запис рядка text у файл
    f.close()  # Закриття файлу 
 
if __name__ == '__main__':
    write_text_to_file(os.path.join('data', 'task1.txt'), text)


text = '''added Kuruluik Iana - 5\n______________________________'''
if __name__ == '__main__':
    log_file = os.path.join('data', 'task1.txt')
    with open(log_file, 'a') as log:
        print('\n', text, str(datetime.datetime.now()),
file=log)

def read_file(fname):
    file = open(fname, 'r')  # відкриття файлу для зчитування
    print('File ' + fname + ':')  # виведення назви файлу     # зчитування вмісту файла по рядках
    for line in file:
        print(line, end='')  # виведення рядка s 
 
    file.close()  # закриття файлу
if __name__ == '__main__':     # функція os.path.join з'єднує частини шляху у файловій системі     # необхідним роздільником
    read_file(os.path.join('data', 'task1.txt'))

line = linecache.getline("C:\3.1\test.txt""",1) #читання рядка з файлу


for filename in os.listdir("C:\\3.2"):
    print(filename)
print('__________________________________')
for filename in glob.glob("C:\\3.2\\*.docx"):
    print(filename) 
