import streamlit.components.v1 as components
from wordcloud import WordCloud
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import requests
import streamlit as st
from streamlit import components
import os


def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        return None


def plot_user_reaction(reaction_count):
    st.subheader(
        'Average Number of reaction user count per Sender')
    df_reaction_count = pd.DataFrame(reaction_count)
    st.bar_chart(df_reaction_count.set_index(
        'user')['reaction_count'])


def plot_user_message(message_count):
    st.subheader('Average Number of message user count per Sender')
    df_message_count = pd.DataFrame(message_count)
    st.bar_chart(df_message_count.set_index(
        'sender_name')['count'])


def plot_user_reply(reply_count):
    st.subheader('Average Number of reply user count per Sender')
    df_reply_count = pd.DataFrame(reply_count)

    st.bar_chart(df_reply_count.set_index(
        'sender_name')['reply_count'])


def main():
    st.title('Slack Data Analysis Dashboard')

    message_count_url = "http://127.0.0.1:8000/message_count"
    message_count = fetch_data(message_count_url)

    reaction_count_url = "http://127.0.0.1:8000/reaction_count"
    reaction_count = fetch_data(reaction_count_url)

    reply_count_url = "http://127.0.0.1:8000/reply_count"
    reply_count = fetch_data(reply_count_url)

    sentiment_url = "http://127.0.0.1:8000/sentiment"
    sentiment = fetch_data(sentiment_url)

    # Create a sidebar menu
    selected_option = st.sidebar.selectbox(
        "Plot for User", ["Message Count", "Reaction Count", "Reply Count"])

    # Display the selected data in the main content area
    if selected_option == "Message Count":
        plot_user_message(message_count)
        st.subheader("Table view")
        st.write(message_count)
    if selected_option == "Reaction Count":
        plot_user_reaction(reaction_count)
        st.write(reaction_count)
    elif selected_option == "Reply Count":
        plot_user_reply(reply_count)
        st.write(reply_count)

    if all(data is not None for data in [message_count, reaction_count, reply_count, sentiment]):
        # Creating a Word Cloud
        st.subheader('Message Count Analysis by User')
        wordcloud = WordCloud(width=800, height=400, background_color='pink').generate_from_frequencies(
            dict(zip(message_count['sender_name'], message_count['count']))
        )

        # Displaying the Word Cloud
        fig, ax = plt.subplots(figsize=(20, 18))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        st.pyplot(fig)

        # Creating a pie chart for reaction_count
        # Sort the DataFrame by 'reaction_count' in descending order
        reaction_count_sorted = reaction_count.sort_values(
            by='reaction_count', ascending=False)

    # Take only the top 20 users
        top_20_users = reaction_count_sorted.head(20)
        st.subheader('Reaction Count Analysis by top 20 User')
        fig, ax = plt.subplots()
        ax.pie(top_20_users['reaction_count'],
               labels=top_20_users['user'], autopct='%1.1f%%')
        st.pyplot(fig)

        # Creating a Seaborn pairplot for sentiment
        st.subheader('Sentiment Analysis Per Day')
        pair_plot = sns.pairplot(sentiment)
        st.pyplot(pair_plot)
    else:
        st.error("Failed to connected to backend.")


if __name__ == '__main__':
    main()


# Rest of your Streamlit code goes here
# ...
