# Agenda - Text to sql llm application
# prompt -> llm -> Gemini pro -> query -> sql -> database -> response
# implementation :-
# 1. sqllite -> insert some records -> python programming
# 2. llm application -> Gemini pro -> sql database

import google.generativeai as genai
import sqlite3
import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()


# configure our api key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# function to load google gemini model and provide sql query as response


def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-2.0-pro-exp')
    response = model.generate_content([prompt[0], question])
    return response

# function to retrieve query from the sql database


def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows


# define your prompt
prompt = [
    """
    You are an expert in converting english question to sql query!
    The sql database has the name student and has the following columns - NAME, CLASS, SECTION and MARKS\n\n
    For example, \n Example 1- How many entries of records are present ?,
    the SQL command will be something like this SELECT COUNT (*) FROM STUDENT ;
    \n Example 2 - Tell me about the students studying in the generative ai class?,
    the SQL command will be something like this SELECT * FROM STUDENT WHERE CLASS = 'Generative ai';
    also the sql code should not have ``` in begging or end and sql word in the output
    """
]

# streamlit app

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question = st.text_input("Input :", key="input")

submit = st.button("Ask the question")

# if submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    sql_query = response.text.strip()  # Extract text from the response
    print("Generated SQL Query:", sql_query)
    data = read_sql_query(sql_query, "student.db")
    st.subheader("The response is ")
    for row in data:
        print(row)
        st.header(row)
