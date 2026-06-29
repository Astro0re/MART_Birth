# Packages 
import os
import streamlit as st
from dotenv import load_dotenv
from supabase import create_client
import datetime 



# Web app structure

st.title("MART BABIES")

f_name = st.text_input("First Name:", key="f_name_d")
l_name = st.text_input("Last Name:", key="l_name_d")
email = st.text_input("Email:", key="email_d")
number = st.text_input("Phone Number:", key="number_d")

# Dropdown menu that generates the input field
num_baby = st.selectbox("How many babies do you have with us?" , options = [1,2,3,4,5], index = 0, key= "baby_num")


for i in range(num_baby):
    st.text(f"Baby {i+1}")
    name_baby = st.text_input(f"Baby Name: ", key=f"baby_name_{i+1}")
    min_date = datetime.date(1990, 1, 1)
    date_ =st.date_input("Birthday", min_value= min_date, key=f"birth_date_{i+1}")
    
comments = st.text_area("Comment", max_chars=150, placeholder="Comments", key='Comm_d') 



if st.button("Submit", key='SUB'):
    # Load environment variables from .env
    load_dotenv()

    SUPABASE_URL = os.getenv("SUPABASE_URL", 'https://qeecgamtitjgtrjfgavs.supabase.co')
    SUPABASE_KEY = os.getenv("SUPABASE_KEY", 'sb_publishable_wrTu9IK5z9iQyt0C7dYk0g_xfOztP_L')

    if not SUPABASE_URL or not SUPABASE_KEY:
        raise ValueError("SUPABASE_URL and SUPABASE_KEY environment variables must be set")

    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

    data = {
        "f_name": st.session_state.get("f_name_d", ""),
        "l_name": st.session_state.get("l_name_d", ""),
        "email": st.session_state.get("email_d", ""),
        "p_number": st.session_state.get("number_d", ""),
        "baby_num": st.session_state.get("baby_num", 1),
        "comments": st.session_state.get("Comm_d", "")
    }

    for i in range(1, int(st.session_state.get("baby_num", 1)) + 1):
        baby_name_key = f"baby_name_{i}"
        birth_date_key = f"birth_date_{i}"

        baby_name = st.session_state.get(baby_name_key, "")
        if baby_name:
            data[baby_name_key] = baby_name

        birth_date = st.session_state.get(birth_date_key)
        if birth_date:
            data[birth_date_key] = birth_date.isoformat() if hasattr(birth_date, "isoformat") else birth_date

    supabase.table("birth_track").insert(data).execute()
    st.info('Data Saved')
