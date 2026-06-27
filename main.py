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

    SUPABASE_URL = 'https://qeecgamtitjgtrjfgavs.supabase.co'
    SUPABASE_KEY = 'sb_publishable_wrTu9IK5z9iQyt0C7dYk0g_xfOztP_L'

    if not SUPABASE_URL or not SUPABASE_KEY:
        raise ValueError("SUPABASE_URL and SUPABASE_KEY environment variables must be set")

    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


    # Supabase input command
    #try:
        supabase.table("birth_track").insert({
            "f_name" : st.session_state["f_name_d"],
            "l_name" : st.session_state["l_name_d"], 
            "email" : st.session_state["email_d"], 
            "p_number" : st.session_state["number_d"],
            "baby_name_1": st.session_state["baby_name_1"],
            "baby_num" : st.session_state["baby_num"], 
            "birth_date_1" : st.session_state["birth_date_1"].isoformat(),
            "comments" : st.session_state["Comm_d"]
            }).execute()

    if st.session_state.get("baby_name_2", False):
        supabase.table("birth_track").insert({
            "baby_name_2": st.session_state["baby_name_2"], 
            "birth_date_2" : st.session_state["birth_date_2"].isoformat()
        }).execute()

    if st.session_state.get("baby_name_3", False):
        supabase.table("birth_track").insert({
            "baby_name_3": st.session_state["baby_name_3"], 
            "birth_date_3" : st.session_state["birth_date_3"].isoformat()
        }).execute()

    if st.session_state.get("baby_name_4", False):
        supabase.table("birth_track").insert({
            "baby_name_4": st.session_state["baby_name_4"], 
            "birth_date_4" : st.session_state["birth_date_4"].isoformat()
        }).execute()

    if st.session_state.get("baby_name_5", False):
        supabase.table("birth_track").insert({
            "baby_name_5": st.session_state["baby_name_5"], 
            "birth_date_5" : st.session_state["birth_date_5"].isoformat()
        }).execute()

    if True: 
        st.info('Data Saved')
