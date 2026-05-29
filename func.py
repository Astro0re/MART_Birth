# Packages 
import os
import streamlit as st
from dotenv import load_dotenv
from supabase import create_client

import Birth_t  

# Load environment variables from .env

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("SUPABASE_URL and SUPABASE_KEY environment variables must be set")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


# Supabase input command
supabase.table("").insert({
            "f_name" : Birth_t.st.session_state["f_name_d"],
            "l_name" : Birth_t.st.session_state["l_name_d"], 
            "cycle_id" : Birth_t.st.session_state["cycle_id_d"], 
            "email" : Birth_t.st.session_state["email_d"], 
            "number" : Birth_t.st.session_state["number_d"], 
            "birth_date" : Birth_t.st.session_state["birth_date_d"], 
            "comments" : Birth_t.st.session_state["Comm_d"]
            }).execute()
if True: 
    st.info('Data Saved')
