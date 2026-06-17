# Packages 
import os
import streamlit as st
from dotenv import load_dotenv
from supabase import create_client




# Web app structure
st.title("MART BABIES")

f_name = st.text_input("First Name:", key="f_name_d")
l_name = st.text_input("Last Name:", key="l_name_d")
cycle_id = st.text_input("Cycle_ID:", key="cycle_id_d")
email = st.text_input("Email:", key="email_d")
number = st.text_input("Phone Number:", key="number_d")

# Dropdown menu that generates the input field
st.options([1,2,3,4,5])

num_baby = int(st.text_input("How many babies(0-5)", key="Baby_num"))

for i in num_baby:
    name_baby = st.text_input("Baby Name (Baby {i}): ", key="baby_name{i}")
    birth_year = st.text_input("Birth Year (Baby {i}): ", key="birth_year{i}")
    birth_month = st.text_input("Birth Month(1-12) (Baby {i}): ", key="birth_month{i}")
    birth_date= st.text_input("Birth Day(1-31) (Baby {i}): ", key="birth_date{i}")
    
comments = st.text_area("Patient Comment", max_chars=150, placeholder="Comments", key='Comm_d') 

 

if st.button("Submit", key='SUB'):

    # Load environment variables from .env

    SUPABASE_URL = 'https://qeecgamtitjgtrjfgavs.supabase.co'
    SUPABASE_KEY = 'sb_publishable_wrTu9IK5z9iQyt0C7dYk0g_xfOztP_L'

    if not SUPABASE_URL or not SUPABASE_KEY:
        raise ValueError("SUPABASE_URL and SUPABASE_KEY environment variables must be set")

    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


    # Supabase input command
    supabase.table("birth_track").insert({
                "f_name" : st.session_state["f_name_d"],
                "l_name" : st.session_state["l_name_d"], 
                "cycle_id" : st.session_state["cycle_id_d"], 
                "email" : st.session_state["email_d"], 
                "p_number" : st.session_state["number_d"], 
                "birth_year" : st.session_state["birth_year"],
                "birth_month" : st.session_state["birth_month"],
                "birth_date" : st.session_state["birth_date"], 
                "comments" : st.session_state["Comm_d"]
                }).execute()
    if True: 
        st.info('Data Saved')
