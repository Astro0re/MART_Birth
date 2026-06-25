# Packages 
import os
import streamlit as st
from dotenv import load_dotenv
from supabase import create_client
import datetime 



# Web app structure
state = st.session_state

st.title("MART BABIES")

f_name = st.text_input("First Name:", key="f_name_d")
l_name = st.text_input("Last Name:", key="l_name_d")
# cycle_id = st.text_input("Cycle_ID:", key="cycle_id_d")
email = st.text_input("Email:", key="email_d")
number = st.text_input("Phone Number:", key="number_d")

# Dropdown menu that generates the input field
num_baby = st.selectbox("How many babies do you have with us?" , options = [1,2,3,4,5], index = 0, key= "baby_num")

# num_baby = int(st.text_input("How many babies(0-5)", key="Baby_num"))

for i in range(num_baby):
    st.text(f"Baby {i+1}")
    name_baby = st.text_input(f"Baby Name: ", key=f"baby_name_{i+1}")
    #birth_year = st.text_input(f"Birth Year: ", key=f"birth_year{i}")
    #birth_month = st.selectbox(f"Birth Month: ",options=['Jan',# 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], index= 0)
    #birth_date= st.text_input(f"Birth Day(1-31): ", key=f"birth_date{i}")
    min_date = datetime.date(1990, 1, 1)
    date_ =st.date_input("Birthday", min_value= min_date, key=f"birth_date_{i+1}")
    
comments = st.text_area("Comment", max_chars=150, placeholder="Comments", key='Comm_d') 

#date_.isoformart

 

if st.button("Submit", key='SUB'):
    # Load environment variables from .env

    SUPABASE_URL = 'https://qeecgamtitjgtrjfgavs.supabase.co'
    SUPABASE_KEY = 'sb_publishable_wrTu9IK5z9iQyt0C7dYk0g_xfOztP_L'

    if not SUPABASE_URL or not SUPABASE_KEY:
        raise ValueError("SUPABASE_URL and SUPABASE_KEY environment variables must be set")

    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


    # Supabase input command
    supabase.table("birth_track").insert({
                "f_name" : state["f_name_d"],
                "l_name" : state["l_name_d"], 
                #"cycle_id" : state["cycle_id_d"], 
                "email" : state["email_d"], 
                "p_number" : state["number_d"],
                #if state["baby_name_1"] is True:
                    "baby_name_1": state["baby_name_1"],
                #elif state["baby_name_2"] is True:
                #    "baby_name_2": state["baby_name_2"],
                #elif state["baby_name_3"] is True:
                  #  "baby_name_3": state["baby_name_3"],
                #elif state["baby_name_4"] is True:
                 #   "baby_name_4": state["baby_name_4"],
                #elif state["baby_name_5"] is True:
                   # "baby_name_5": state["baby_name_5"],
                #"baby_name" : state[["baby_name_1", "baby_name_2", "baby_name_3", "baby_name_4", "baby_name_5"]],
                "baby_num" : state["num_baby"],
                #"birth_year" : state["birth_year"],
                #"birth_year" : state[f"birth_year{i}"], ??
                #"birth_month" : state["birth_month"],
                #if state["birth_date_1"] is True: 
                    "birth_date_1" : state["birth_date_1"],
                #elif state["birth_date_2"] is True: 
                   # "birth_date_2" : state["birth_date_2"],
                #elif state["birth_date_3"] is True: 
                   # "birth_date_3" : state["birth_date_3"],
                #elif state["birth_date_4"] is True: 
                    #"birth_date_4" : state["birth_date_4"],
                #elif state["birth_date_5"] is True: 
                   # "birth_date_5" : state["birth_date_5"],
                #"birth_date" : state[["birth_date_1", "birth_date_2", "birth_date_3", "birth_date_4", "birth_date_5"]], 
                "comments" : state["Comm_d"]
                }).execute()

    if state["baby_name_2"] is True:
        supabase.table("birth_track").insert({
            "baby_name_2": state["baby_name_2"], 
            "birth_date_2" : state["birth_date_2"]
        }).execute()

    if state["baby_name_3"] is True:
        supabase.table("birth_track").insert({
            "baby_name_3": state["baby_name_3"], 
            "birth_date_3" : state["birth_date_3"]
        }).execute()

    if state["baby_name_4"] is True:
        supabase.table("birth_track").insert({
            "baby_name_4": state["baby_name_4"], 
            "birth_date_4" : state["birth_date_4"]
        }).execute()

    if state["baby_name_5"] is True:
        supabase.table("birth_track").insert({
            "baby_name_5": state["baby_name_5"], 
            "birth_date_5" : state["birth_date_5"]
        }).execute()
        
    if True: 
        st.info('Data Saved')
