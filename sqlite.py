import sqlite3


def main():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE users
                      (id TEXT,
                      lang TEXT,
                      last_request TEXT)""")
    conn.commit()
    conn.close()


def get_users():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users")
    users = cursor.fetchall()
    conn.close()
    result = []
    for user in users:
        result.append(user[0])
    return result


def get_language(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT lang FROM users WHERE id = '{user_id}'")
    lang = cursor.fetchone()
    conn.close()
    return lang[0]


def get_last_request(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT last_request FROM users WHERE id = '{user_id}'")
    req = cursor.fetchone()
    conn.close()
    return req[0]


def add_user(user_id, lang=''):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO users VALUES ('{user_id}', '{lang}', '')")
    conn.commit()
    conn.close()


def change_last_request(user_id, req):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"UPDATE users SET last_request = '{req}' WHERE id = '{user_id}'")
    conn.commit()
    conn.close()


def change_language(user_id, lng):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"UPDATE users SET lang = '{lng}' WHERE id = '{user_id}'")
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
