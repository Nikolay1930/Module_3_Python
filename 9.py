import sqlite3


'''try:
    connection = sqlite3.connect('urok_11_27.db')
    cursor = connection.cursor()
except sqlite3.DatabaseError:
    print('Ошибка при работе с БД')
finally:
    connection.close()'''

"""with sqlite3.connect('urok_11_27.db') as connection:
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')"""


class Database:
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()

    def create_table(self):
        with self.connection:
            self.cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')

    def add_user(self, name, age):
        with self.connection:
            self.cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))

    def get_users_list(self):
        with self.connection:
            return self.cursor.execute('SELECT * FROM users').fetchall()

    def get_user(self, user_id):
        with self.connection:
            return self.cursor.execute('SELECT name, age FROM users WHERE id = ?', (user_id, )).fetchone()

    def update_user_age(self, user_id, age):
        with self.connection:
            self.cursor.execute('UPDATE users SET age = ? WHERE id = ?', (age, user_id))

    def del_user(self, user_id):
        with self.connection:
            self.cursor.execute('DELETE FROM users WHERE id = ?', (user_id, ))

    def del_all_users(self):
        with self.connection:
            self.cursor.execute('DELETE FROM users')


if __name__ == '__main__':
    db = Database('urok_11_27.db')
    # db.create_table()
    db.add_user('DIMA', 21)
    print(db.get_users_list())
    print(db.get_user(6))
    db.update_user_age(1, 1999)
    db.del_user(2)
    print(db.get_users_list())
    db.del_all_users()
    print(db.get_users_list())
