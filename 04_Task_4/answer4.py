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
    if not name or '@' not in email:
        error = "Error: Invalid data. Provide a name and a valid email."
        return render_template('form.html', error=error)
    try:
        insert_into_readers(name, email)
        success = "Data successfully submitted."
        return render_template('form.html', success=success)
    except psycopg2.Error as e:
        error = f"Error: {str(e)}"
        return render_template('form.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)
