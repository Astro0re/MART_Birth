import os
import sqlite3
from dotenv import load_dotenv
import streamlit as st

# Load environment variables from .env (if present)
load_dotenv()

def create_table():
    try: 
        conn = sqlite3.connect("birth_track.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS birth_tracker(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                f_name TEXT NOT NULL,
                l_name TEXT NOT NULL,
                cycle_id VARCHAR UNIQUE,
                email VARCHAR(25), 
                number INT,
                birth_date DATE NOT NULL,
                comments TEXT
            )
        """)
        conn.commit()
        print("Database Created")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def main():
    create_table()
    st.title("MART BABIES")

    # Authentication: require an access code stored in environment variable ACCESS_CODE
    ACCESS_CODE = os.getenv("ACCESS_CODE")
    if not ACCESS_CODE:
        st.error("Server not configured: set ACCESS_CODE in a .env file or environment variables.")
        st.stop()

    access = st.text_input("Access code:", type="password", key="access_code")
    if access != ACCESS_CODE:
        st.warning("Enter the correct access code to use this app.")
        st.stop()

    f_name = st.text_input("First Name:", key="f_name")
    l_name = st.text_input("Last Name:", key="l_name")
    cycle_id = st.text_input("Cycle_ID:", key="cycle_id")
    email = st.text_input("Email:", key="email")
    number = st.text_input("Phone Number:", key="number")
    birth_date = st.date_input("Date of Birth: ", key="birth_date")
    comments = st.text_area("Patient Comment", max_chars=150, placeholder="Comments", key='Comm')

    def add_values(f_name, l_name, cycle_id, email, number, birth_date, comments):
        try: 
            # Use an exclusive transaction so the DB file is locked for the duration
            conn = sqlite3.connect("birth_track.db", timeout=30)
            cursor = conn.cursor()
            cursor.execute('PRAGMA busy_timeout = 5000')
            cursor.execute('PRAGMA locking_mode = EXCLUSIVE')
            cursor.execute('BEGIN EXCLUSIVE')
            cursor.execute(
                "INSERT INTO birth_tracker(f_name,l_name,cycle_id,email,number,birth_date,comments) VALUES (?,?,?,?,?,?,?)",
                (f_name, l_name, cycle_id, email, int(number), birth_date, comments),
            )
            conn.commit()
            print("Data added successfully")
        except sqlite3.IntegrityError:
            print("Error: Cycle Case Already Reported")
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            conn.close()

    if st.button("Submit", key='SUB'):
        add_values(f_name, l_name, cycle_id, email, number, birth_date, comments)

if __name__ == "__main__":
    main()
