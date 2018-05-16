import sqlite3

conn = sqlite3.connect(r'C:\Users\student\PycharmProjects\telebot\us.db')
cursor = conn.cursor()

# cursor.execute("""CREATE TABLE Users (id text, first_name text, last_name text)""")
# cursor.execute("""CREATE TABLE Images (id text, image blob)""")
conn.commit()
all = cursor.execute("""SELECT * FROM '{}'""".format('Users'))
print(all.fetchall())


all = cursor.execute("SELECT * FROM Images")
print(all.fetchall())



