import streamlit.components.v1 as components
from wordcloud import WordCloud
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import requests
import streamlit as st


def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        return None


def main():
    st.title('Slack Data Analysis Dashboard')

    # Fetching message count from FastAPI
    message_count_url = "http://127.0.0.1:8000/message_count"
    message_count = fetch_data(message_count_url)

    # Fetching reaction count from FastAPI
    reaction_count_url = "http://127.0.0.1:8000/reaction_count"
    reaction_count = fetch_data(reaction_count_url)
    if all(data is not None for data in [message_count, reaction_count]):
        # Creating a Word Cloud
        st.subheader('Message Count Analysis by Sender')
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(
            dict(zip(message_count['sender_name'], message_count['count']))
        )

        # Displaying the Word Cloud
        fig, ax = plt.subplots(figsize=(20, 18))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        st.pyplot(fig)

        # Creating a Seaborn pairplot for sentiment
        # st.subheader('Sentiment Analysis by Day')
        # pair_plot = sns.pairplot(sentiment)
        # st.pyplot(pair_plot)

        # Creating a pie chart for reaction_count
        st.subheader('Reaction Count Analysis by User')
        fig, ax = plt.subplots()
        ax.pie(reaction_count['reaction_count'],
               labels=reaction_count['user'], autopct='%1.1f%%')
        st.pyplot(fig)
    else:
        st.error("Failed to fetch data from FastAPI.")


if __name__ == '__main__':
    main()
