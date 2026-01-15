import sqlite3
import gradio as gr
import pandas as pd

def fetchTeams():
    conn = sqlite3.connect('playoffTeams.db')

    cursor = conn.cursor()

    query = """
        SELECT * 
        FROM teams;
    """

    cursor.execute(query)
    results = cursor.fetchall()

    conn.close()

    df = pd.DataFrame(results, columns = ['id', 'city', 'names'])

    return df

iface = gr.InterFace(
    fn = fetchTeams,
    inputs = [],
    outputs = gr.TextBox()
)

iface.launch()