import sqlite3
import streamlit as st 
#import twilio 

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

    f_name = st.text_input("First Name:", key="f_name")
    l_name = st.text_input("Last Name:", key="l_name")
    cycle_id = st.text_input("Cycle_ID:", key="cycle_id")
    email = st.text_input("Email:", key="email")
    number = st.text_input("Phone Number:", key="number")
    birth_date = st.date_input("Date of Birth: ", key="birth_date")
    comments = st.text_area("Patient Comment", max_chars=150, placeholder="Comments", key='Comm')

    def add_values(f_name, l_name, cycle_id, email, number, birth_date, comments):
        try: 
            conn = sqlite3.connect("birth_track.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO birth_tracker(f_name,l_name,cycle_id,email,number,birth_date,comments) VALUES (?,?,?,?,?,?,?)", 
                         (f_name, l_name, cycle_id, email, int(number), birth_date, comments))
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
