# Packages 
import streamlit as st


def main():
    st.title("MART BABIES")

    f_name = st.text_input("First Name:", key="f_name_d")
    l_name = st.text_input("Last Name:", key="l_name_d")
    cycle_id = st.text_input("Cycle_ID:", key="cycle_id_d")
    email = st.text_input("Email:", key="email_d")
    number = st.text_input("Phone Number:", key="number_d")
    birth_date = st.date_input("Date of Birth: ", key="birth_date_d")
    comments = st.text_area("Patient Comment", max_chars=150, placeholder="Comments", key='Comm_d')



    def add_values(table_name : str ,data : dict ):

        try: 
            response = supabase.table(table_name).insert(data).execute()
            if response.data:
                st.text('Data added successfully')
            else:
                st.text('Error in Input')
        except Exception as e:
            print(f'Erro due to :{e}')  

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


if __name__ == "__main__":
    
    main()