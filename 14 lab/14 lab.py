import os
import sqlite3
from datetime import date

# Удаление существующего файла hospital.db, если он существует
if os.path.exists('hospital.db'):
    os.remove('hospital.db')

# Класс "Прив. сертификат"
class Certificate:
    def __init__(self, id, number):
        self.id = id
        self.number = number

# Класс "Ребёнок"
class Child:
    def __init__(self, id, name, birthdate, gender, certificate):
        self.id = id
        self.name = name
        self.birthdate = birthdate
        self.gender = gender
        self.certificate = certificate

    def get_age(self):
        today = date.today()
        age = today.year - self.birthdate.year
        if today.month < self.birthdate.month or (today.month == self.birthdate.month and today.day < self.birthdate.day):
            age -= 1
        return age

# Класс "Врач"
class Doctor:
    def __init__(self, id, name, profession):
        self.id = id
        self.name = name
        self.profession = profession

    def get_number_of_children(self, children):
        return sum(child.certificate.number == self.id for child in children)

# Функция для заполнения БД данными
def fill_database():
    connection = sqlite3.connect('hospital.db')
    cursor = connection.cursor()

    # Создание таблиц
    cursor.execute('''CREATE TABLE IF NOT EXISTS Certificates (
                        id INTEGER PRIMARY KEY,
                        number INTEGER)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Children (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        birthdate TEXT,
                        gender TEXT,
                        certificate_id INTEGER,
                        FOREIGN KEY(certificate_id) REFERENCES Certificates(id))''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Doctors (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        profession TEXT)''')

    # Заполнение таблиц данными
    certificate1 = Certificate(1, 123)
    certificate2 = Certificate(2, 456)
    certificate3 = Certificate(3, 789)
    certificate4 = Certificate(4, 101)
    certificate5 = Certificate(5, 112)
    certificate6 = Certificate(6, 131)
    certificate7 = Certificate(7, 415)
    certificate8 = Certificate(8, 161)
    certificate9 = Certificate(9, 718)
    certificate10 = Certificate(10, 192)

    certificates = [certificate1, certificate2, certificate3, certificate4, certificate5, certificate6,
                    certificate7, certificate8, certificate9, certificate10]

    for certificate in certificates:
        cursor.execute("INSERT INTO Certificates (id, number) VALUES (?, ?)", (certificate.id, certificate.number))

    children = [
        Child(1, "Иванов Иван Иванович", date(2010, 1, 15), "Мужской", certificates[0]),
        Child(2, "Петрова Анна Сергеевна", date(2011, 3, 25), "Женский", certificates[1]),
        Child(3, "Смирнов Денис Игоревич", date(2012, 6, 10), "Мужской", certificates[2]),
        Child(4, "Сидорова Елена Петровна", date(2013, 9, 8), "Женский", certificates[3]),
        Child(5, "Васильева Ольга Андреевна", date(2014, 12, 1), "Женский", certificates[4]),
        Child(6, "Павлов Николай Сергеевич", date(2015, 2, 18), "Мужской", certificates[5]),
        Child(7, "Кузнецов Максим Викторович", date(2016, 4, 5), "Мужской", certificates[6]),
        Child(8, "Морозова Екатерина Ивановна", date(2017, 7, 9), "Женский", certificates[7]),
        Child(9, "Николаев Владислав Олегович", date(2018, 10, 20), "Мужской", certificates[8]),
        Child(10, "Орлова Анастасия Степановна", date(2019, 11, 28), "Женский", certificates[9])
    ]

    for child in children:
        cursor.execute("INSERT INTO Children (id, name, birthdate, gender, certificate_id) VALUES (?, ?, ?, ?, ?)",
                       (child.id, child.name, child.birthdate.isoformat(), child.gender, child.certificate.id))

    doctors = [
        Doctor(1, "Иванова Ольга Петровна", "Педиатр"),
        Doctor(2, "Петров Сергей Иванович", "Стоматолог"),
        Doctor(3, "Смирнова Анастасия Владимировна", "Офтальмолог"),
        Doctor(4, "Сидоров Иван Сергеевич", "Невролог"),
        Doctor(5, "Васильев Алексей Андреевич", "Хирург"),
        Doctor(6, "Павлова Наталья Викторовна", "Терапевт"),
        Doctor(7, "Кузнецова Екатерина Игоревна", "Гинеколог"),
        Doctor(8, "Морозов Александр Олегович", "Ортопед"),
        Doctor(9, "Николаева Мария Дмитриевна", "Лор"),
        Doctor(10, "Орлов Игорь Степанович", "Кардиолог")
    ]

    for doctor in doctors:
        cursor.execute("INSERT INTO Doctors (id, name, profession) VALUES (?, ?, ?)",
                       (doctor.id, doctor.name, doctor.profession))

    connection.commit()
    connection.close()

# Функция для выполнения запроса "Все дети"
def get_all_children():
    connection = sqlite3.connect('hospital.db')
    cursor = connection.cursor()

    cursor.execute('''SELECT Children.name, 
                            (strftime('%Y', 'now') - strftime('%Y', Children.birthdate)) - 
                            (strftime('%m-%d', 'now') < strftime('%m-%d', Children.birthdate)), 
                            Doctors.name 
                      FROM Children 
                      INNER JOIN Certificates ON Children.certificate_id = Certificates.id 
                      INNER JOIN Doctors ON Certificates.id = Doctors.id''')

    children_data = cursor.fetchall()

    for child_data in children_data:
        print("ФИО ребенка:", child_data[0])
        print("Возраст ребенка:", child_data[1])
        print("ФИО врача:", child_data[2])
        print()

    connection.close()

# Функция для выполнения запроса "Все врачи"
def get_all_doctors():
    connection = sqlite3.connect('hospital.db')
    cursor = connection.cursor()

    cursor.execute('''SELECT Doctors.name, 
                            Doctors.profession, 
                            COUNT(Children.id) 
                      FROM Doctors 
                      LEFT JOIN Certificates ON Doctors.id = Certificates.id 
                      LEFT JOIN Children ON Certificates.id = Children.certificate_id 
                      GROUP BY Doctors.id''')

    doctors_data = cursor.fetchall()

    for doctor_data in doctors_data:
        print("ФИО врача:", doctor_data[0])
        print("Профессия врача:", doctor_data[1])
        print("Сколько детей он лечит:", doctor_data[2])
        print()

    connection.close()

# Заполнение БД
fill_database()

# Ввод запроса пользователем
while True:
    print("Выберите запрос:")
    print("1. Все дети")
    print("2. Все врачи")
    print("0. Выход")

    choice = input("Введите номер запроса: ")

    if choice == "1":
        print("Все дети:")
        get_all_children()
    elif choice == "2":
        print("Все врачи:")
        get_all_doctors()
    elif choice == "0":
        break
    else:
        print("Неверный ввод. Повторите попытку.")
    print()
