# Packages 
import streamlit as st
import func.py 

def main():
    st.title("MART BABIES")

    f_name = st.text_input("First Name:", key="f_name_d")
    l_name = st.text_input("Last Name:", key="l_name_d")
    cycle_id = st.text_input("Cycle_ID:", key="cycle_id_d")
    email = st.text_input("Email:", key="email_d")
    number = st.text_input("Phone Number:", key="number_d")
    birth_date = st.date_input("Date of Birth: ", key="birth_date_d")
    comments = st.text_area("Patient Comment", max_chars=150, placeholder="Comments", key='Comm_d')

 

    if st.button("Submit", key='SUB'):
        func.py.main()  


if __name__ == "__main__":
    
    main()