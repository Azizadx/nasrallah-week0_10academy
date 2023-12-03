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
    query = "SELECT * FROM reaction_count;"
    df_message_count = pd.read_sql(query, conn)
    conn.close()
    return df_message_count.to_dict(orient='records')

# ... (your existing code)


@app.get("/avg_top20_reply_users_count")
async def fetch_avg_top20_reply_users_count(channel: str = 'Random'):
    conn = connect_to_db()
    query = f"SELECT * FROM reaction_count WHERE channel = '{channel}';"
    df_reaction_count = pd.read_sql(query, conn)
    conn.close()

    top20_senders = df_reaction_count.groupby(
        'sender_name')['reply_users_count'].mean().sort_values(ascending=False)[:20]
    return top20_senders.to_dict()


@app.get("/sentiment")
async def fetch_sentiment_data():
    conn = connect_to_db()
    query = "SELECT * FROM sentiment_for_day;"
    df_sentiment = pd.read_sql(query, conn)
    conn.close()
    return df_sentiment.to_dict(orient='records')
