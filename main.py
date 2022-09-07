from Actor import Actor
from configparser import ConfigParser
import mysql
import mysql.connector
from mysql.connector import Error
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

database_name = "pythonDB"
user = "root"
password = "Hydroo2014$%"


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.name = QLabel('Name')
        self.salary = QLabel('Salary')
        self.role = QLabel('Role')
        self.film = QLabel('Film')

        self.nameEdit = QLineEdit()
        self.slaryEdit = QLineEdit()
        self.roleEdit = QLineEdit()
        self.filmEdit = QLineEdit()

        self.button = QPushButton('Save')
        self.button1 = QPushButton('Delete')
        self.button2 = QPushButton('Show')
        self.button3 = QPushButton('Close')

        self.button.clicked.connect(self.write_to_file)
        self.button1.clicked.connect(self.delete_line_by_name)
        self.button2.clicked.connect(self.show_btn_click)
        self.button3.clicked.connect(self.close)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.name, 1, 0)
        grid.addWidget(self.nameEdit, 1, 1)

        grid.addWidget(self.salary, 2, 0)
        grid.addWidget(self.slaryEdit, 2, 1)

        grid.addWidget(self.role, 3, 0)
        grid.addWidget(self.roleEdit, 3, 1)

        grid.addWidget(self.film, 4, 0)
        grid.addWidget(self.filmEdit, 4, 1)

        grid.addWidget(self.button, 5, 0)
        grid.addWidget(self.button1, 5, 1)
        grid.addWidget(self.button2, 6, 0)
        grid.addWidget(self.button3, 6, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 150, 150)
        self.setWindowTitle('9')
        self.show()

    def write_to_file(self):
        conn = mysql.connector.connect(host='localhost', database=database_name, user=user, password=password)
        cursor = conn.cursor()

        add_person = ("INSERT INTO people "
                      "( name, salary, role, film )"
                      "VALUES (%s, %s, %s, %s)")

        data_person = (self.nameEdit.text(), self.slaryEdit.text(), self.roleEdit.text(), self.filmEdit.text())

        cursor.execute(add_person, data_person)
        conn.commit()
        cursor.close()

        conn.close()

    def delete_line_by_name(self):
        cnx = mysql.connector.connect(host='localhost', database=database_name, user=user, password=password)
        cursor = cnx.cursor()

        delete_by_name = "DELETE FROM people WHERE name = %s "
        actor_name = (self.nameEdit.text())

        cursor.execute(delete_by_name, (actor_name,))
        cnx.commit()
        cursor.close()

        cnx.close()

    def show_btn_click(self):
        cnxn = mysql.connector.connect(host='localhost', database=database_name, user=user, password=password)
        cursor = cnxn.cursor(buffered=True)
        query = "SELECT * FROM people"
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
        cnxn.commit()
        cursor.close()

        cnxn.close()

    def close(self):
        QApplication.quit()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
