# Text-to-SQL using Gemini LLM

Demo Video Link :- https://drive.google.com/file/d/1xeaCsaJ1XQQrt-ONZiLon1IHOc1gMD4F/view?usp=sharing

This is a simple AI-powered web app that lets you ask natural language questions and get answers from a SQL database. It uses **Google Gemini LLM** to convert your question to a SQL query and fetches data from a **SQLite** database.

---

##  Features

- Ask plain English questions like "How many students in class A?"
- Automatically generates SQL using **Google Gemini Pro**
- Executes the query on a local **SQLite** database
- Uses **Streamlit** for an easy-to-use UI

---

##  Tech Stack

- Python
- Streamlit
- Google Generative AI (Gemini)
- SQLite
- Dotenv

---

##  Project Structure

```
text-to-sql-gemini/
├── app.py            # Main Streamlit app
├── sql.py             # Script to create student.db and insert records
├── student.db         # SQLite database file (created by sql.py)
├── .env               # Stores your Google API key
├── requirements.txt   # List of dependencies
└── README.md          # Documentation
```

---

##  Setup Instructions

### 1. Clone the Repository


### 2. Create a Virtual Environment (optional)


### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Your Google API Key

Create a `.env` file in the root folder and paste your Gemini API key:

```
GOOGLE_API_KEY=your_gemini_api_key_here
```

## 🗃️ Create Database

Run the `sql.py` file once to generate the `student.db` database and insert sample records:

```bash
python sql.py
```

This will create a table called `STUDENT` and insert 5 sample records.

---

##  Run the Application

```bash
streamlit run main.py
```

Then open the app in your browser and try questions like:

- “How many students are in the Gen ai class?”
- “Show all students with marks greater than 90.”

---

##  Sample Prompt (Used in Code)

The Gemini model is prompted like this:

> "You are an expert in converting English questions to SQL query. The database is named 'student' and has columns: NAME, CLASS, SECTION, MARKS. Do not include SQL keywords like 'sql' or code blocks.
You are an expert in converting english question to sql query! The sql database has the name student and has the following columns - NAME, CLASS, SECTION and MARKS\n\n For example, \n Example 1- How many entries of records are present ?, the SQL command will be something like this SELECT COUNT (*) FROM STUDENT ; \n Example 2 - Tell me about the students studying in the generative ai class?,the SQL command will be something like this SELECT * FROM STUDENT WHERE CLASS = 'Generative ai'; also the sql code should not have sql in begging or end and sql word in the output
"

---

## Example Questions

- "How many students are in the database?"
- "List students with marks above 80"
- "Show students from section A"
