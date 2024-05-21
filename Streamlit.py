import pandas as pd
import streamlit as st
import pymongo
from datetime import date
import time

# Setting Title
st.title("Stock Price")

# Setting Header
st.subheader("Choose a stock and duration to see graph")

# Creating a dropdown
# symbol = st.selectbox("Select an option", options)

# Taking Date Inputs
choose_date = str(st.date_input("Select a date", date.today()))

submit = st.button("Get Graphs")

# creating a single-element container
placeholder = st.empty()

for seconds in range(30):
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = myclient["your_database"]
    mycol = mydb["your_collection"]

    df = pd.DataFrame(list(mycol.find()))
    df = df[["date", "Name", "open", "high", "low", "close", "volume"]]
    df['date'] = pd.to_datetime(df['date'])

    with placeholder.container():
        options = ["AAPL", "GOOGL", "AMZN", "TSLA", "JNJ", "XOM"]

        # Getting stock Data from yahoo finance
        # tickerData = df[df['Name'] == symbol]
        tickerData = df
        mask = (tickerData['date'] == choose_date)
        tickerDf = tickerData[mask]

        if submit:
            # Ploting Data
            # st.markdown("""
            # ### Closing Price & Volume
            # """)
            # st.scatter_chart(tickerDf, x= 'volume', y= 'close')

            st.markdown("""
            ### Volume
            """)
            st.dataframe(tickerDf)
        time.sleep(1)


