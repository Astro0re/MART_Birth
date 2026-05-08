# Packages 
import os
import requests
from dotenv import load_dotenv
from supabase import create_client, Client 
from '\Birth_t.py' import st.session_state["f_name_d"],
            st.session_state["l_name_d"], 
            st.session_state["cycle_id_d"], 
            st.session_state["email_d"], 
            st.session_state["number_d"], 
            st.session_state["birth_date_d"], 
            st.session_state["Comm_d"]

# Load environment variables from .env
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("SUPABASE_URL and SUPABASE_KEY environment variables must be set")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

client.send

if st.button("Submit", key='SUB'):
        data = {
            f_name : st.session_state["f_name_d"],
            l_name : st.session_state["l_name_d"], 
            cycle_id : st.session_state["cycle_id_d"], 
            email : st.session_state["email_d"], 
            number : st.session_state["number_d"], 
            birth_date : st.session_state["birth_date_d"], 
            comments : st.session_state["Comm_d"]
            }
    
        add_values('birth_track', data)

# Supabase input command
supabase.table("").insert({
            f_name : st.session_state["f_name_d"],
            l_name : st.session_state["l_name_d"], 
            cycle_id : st.session_state["cycle_id_d"], 
            email : st.session_state["email_d"], 
            number : st.session_state["number_d"], 
            birth_date : st.session_state["birth_date_d"], 
            comments : st.session_state["Comm_d"]
            }).execute()