import sqlite3


def create_database():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE users(
            first_name text,
            last_name text,
            year_of_birth integer,
            country text,
            email text,
            password text
            )""")

    cursor.execute("""CREATE TABLE bank_data(
            bank_id integer,
            USD real,
            USDT real,
            BTC real
            )""")

    conn.commit()
    conn.close()


def return_loggins():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT email, password FROM users")
    data = cursor.fetchall()
    conn.close()
    return data


def construct_user(user_email, user_password):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * from users WHERE email = (?) AND password = (?)", (user_email, user_password))
    data = cursor.fetchall()
    conn.close()
    return data

# TODO: create construct_bank to retrieve the bank object data
def add_user(first_name, last_name, year_of_birth, country, email, password):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users VALUES (?,?,?,?,?,?)", (first_name, last_name, year_of_birth, country, email, password))

    conn.commit()
    conn.close()


def construct_bank_user(email):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * from bank_data WHERE email = (?)", (email,))
    data = cursor.fetchall()
    conn.close()
    return data[0][0:6] #Returns the tuple as a list ignoring the email column at the end


















def main():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    #c.execute("DELETE from users WHERE rowid = 6")

    c.execute("SELECT * FROM users")
    items = c.fetchall()
    for item in items:
        print(item)

    print("\n")
    c.execute("SELECT * FROM bank_data")
    items = c.fetchall()
    for item in items:
        print(item)


    conn.commit()
    conn.close()



if __name__ == "__main__":
    main()
