from flask import Flask, request, render_template
import psycopg2

import logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

DB_NAME = "exam"
DB_USER = "lukas"
DB_PASSWORD = "lukaspwd"
DB_HOST = "localhost"

def connect_to_database():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
    )
    logging.debug("Connected to DB successfully.")
    return conn

def insert_into_readers(name, email):
    conn = connect_to_database()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Readers (name, email) VALUES (%s, %s)", (name, email))
        conn.commit()
        logging.debug("Transaction saved to DB.")
    except psycopg2.Error as e:
        conn.rollback()
        logging.error("Error: Transaction rollback.")
        raise e
    finally:
        cursor.close()
        conn.close()
        logging.debug("Connection to DB closed.")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('form.html')

    name, email = request.form['name'], request.form['email']
    if not name: # @ checked on FE
        return render_template('form.html', error="Error: Name cannot be empty")
    try:
        insert_into_readers(name, email)
        return render_template('form.html', success= "Data successfully submitted.")
    except psycopg2.Error as e:
        logging.error(e)
        return render_template('form.html', error="Error: Failed insert")


if __name__ == '__main__':
    app.run(debug=True)
