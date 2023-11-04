import sqlite3

connection = sqlite3.connect("itstep.sl3", 5)

cur = connection.cursor()

cur.execute("ALTER TABLE users RENAME e TO phone_number;")

connection.commit()

# res = cur.fetchall()
# print(res)

connection.close()
#("INSERT INTO users (user_name) VALUES ('Illya');")
#("CREATE TABLE users (user_name TEXT);")
#("SELECT rowid, user_name FROM users;")
#("ALTER TABLE users ADD email TEXT")
#("UPDATE users SET email='super.admin@u.a' where rowid=1;")
#("ALTER TABLE users RENAME e TO phone_number;")
#("DELETE FROM users where rowid=4;")
#("DELETE FROM users;")
#("DELETE FROM users where user_name=admin;")
#("DROP TABLE users;")