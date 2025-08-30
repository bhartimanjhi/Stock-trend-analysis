# Stock Trend Analysis - Data Science project

import yfinance as yf
import pandas as pd
import streamlit as st
from streamlit_autorefresh import st_autorefresh
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(
    page_title="Stock Trend Analysis", layout="wide", initial_sidebar_state="collapsed"
)
st_autorefresh = st_autorefresh(interval=300 * 1000, key="refresh")
st.markdown(
    """
    <style>
    h1 {
        animation: fadeIn 2s ease-in-out;
    }
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    </style>
    """,
    unsafe_allow_html=True,
)


st.title("Stock Trend Analysis")
st.header("Analysis Dashboard")

ticker = st.text_input("Enter Stock Ticker(AAPL, INFY.NS, TSLA etc.)", value="AAPL")
start_date = st.date_input("start Date", pd.to_datetime("01-01-2024"))

end_date = st.date_input("End Date", pd.to_datetime("today"))
latest_price = None
df = pd.DataFrame()

if st.button("Fetch Data"):
    with st.spinner("Fetching Stock Data..."):
        df = yf.download(ticker, start=start_date, end=end_date)
        df.columns = [col[0] if isinstance(col, tuple) else col for col in df.columns]

    if df.empty:
        st.error("⚠️ No data found for the selected ticker & date range.")
        st.stop()

    df["MA20"] = df["Close"].rolling(window=20).mean()
    df["Volatility"] = df["Close"].rolling(window=20).std()
    latest_price = float(df["Close"].iloc[-1])
    change = latest_price - float(df["Close"].iloc[0])

    pct_change = (change / float(df["Close"].iloc[0])) * 100
    c1, c2, c3 = st.columns(3)
    c1.metric(label=f"{ticker} Latest Price", value=f"${latest_price:.2f}")
    c2.metric(label="Change", value=f"{change:.2f} USD", delta=f"{pct_change:.2f}%")
    c3.metric(label="Volatility", value=f"{df['Volatility'].iloc[-1]:.2f}")

    st.subheader("📉 Price Trend")
    fig_price = px.line(
        df,
        x=df.index,
        y="Close",
        title=f"{ticker} Closing Price",
        template="plotly_dark",
    )
    fig_price.add_scatter(x=df.index, y=df["MA20"], mode="lines", name="20-Day MA")
    st.plotly_chart(fig_price, use_container_width=True)

    st.subheader("📊 Volatility Trend")
    fig_vol = px.line(
        df,
        x=df.index,
        y="Volatility",
        title="Volatility Over Time",
        template="plotly_dark",
    )
    st.plotly_chart(fig_vol, use_container_width=True)

    st.subheader("📆 Last 50 Days Trend")
    fig_last50 = px.line(
        df.tail(50),
        x=df.tail(50).index,
        y="Close",
        markers=True,
        title=f"Last 50 Days Closing Prices ({ticker})",
        template="plotly_dark",
    )
    st.plotly_chart(fig_last50, use_container_width=True)

    st.subheader("📋 Stock Data (Last 10 rows)")
    st.dataframe(df.tail(10).style.highlight_max(axis=0))

    if len(df) > 1:
        change = float(df["Close"].iloc[-1]) - float(df["Close"].iloc[0])
        pct_change = (
            (float(df["Close"].iloc[-1]) - float(df["Close"].iloc[0]))
            / float(df["Close"].iloc[0])
            * 100
        )

        st.metric(label="Change", value=f"{change:.2f} USD", delta=f"{pct_change:.2f}%")

        st.subheader("Last 50 Days Trend")
        window = 50
        fig3, ax3 = plt.subplots(figsize=(10, 4))
        ax3.plot(df["Close"].tail(window), marker="o", linestyle="-", color="green")
        ax3.set_title(f"Last {window} Days Trend for {ticker}")
        st.pyplot(fig3)

        st.subheader(f"Stock Data for {ticker}")
        st.dataframe(df.tail())

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(df["Close"], label="Close Price", color="blue")
        ax.plot(df["MA20"], label="20-Day MA", color="orange")

        ax.xaxis.set_major_formatter(mdates.DateFormatter("%d-%m-%Y"))
        ax.xaxis.set_major_locator(mdates.AutoDateLocator())
        plt.xticks(rotation=90)

        ax.set_title(f"{ticker} Stock Price Trend")

        ax.set_ylabel("Price")
        ax.legend()
        st.pyplot(fig)

        st.subheader("Volatitliy Trend")
        fig2, ax2 = plt.subplots(figsize=(10, 3))
        ax2.plot(df["Volatility"], label="Volatility", color="red")

        ax2.xaxis.set_major_formatter(mdates.DateFormatter("%d-%m-%Y"))
        ax2.xaxis.set_major_locator(mdates.AutoDateLocator())
        plt.setp(ax2.get_xticklabels(), rotation=90)

        ax2.set_title("Volatility Over Time")
        ax2.legend()
        st.pyplot(fig2)
