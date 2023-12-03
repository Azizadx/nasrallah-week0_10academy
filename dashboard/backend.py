from fastapi import FastAPI
import psycopg2
import pandas as pd

app = FastAPI()


def connect_to_db():
    conn = psycopg2.connect(
        dbname='slack_db',
        user='postgres',
        password='123',
        host='localhost',
        port='5435'
    )
    return conn




@app.get("/reply_count")
async def fetch_message_count():
    conn = connect_to_db()
    query = "SELECT * FROM reply_count;"
    df_message_count = pd.read_sql(query, conn)
    conn.close()
    return df_message_count.to_dict(orient='records')



@app.get("/message_count")
async def fetch_message_count():
    conn = connect_to_db()
    query = "SELECT * FROM message_count;"
    df_message_count = pd.read_sql(query, conn)
    conn.close()
    return df_message_count.to_dict(orient='records')




@app.get("/reaction_count")
async def fetch_message_count():
    conn = connect_to_db()
    query = "SELECT * FROM user_reaction_counts;"
    df_message_count = pd.read_sql(query, conn)
    conn.close()
    return df_message_count.to_dict(orient='records')
