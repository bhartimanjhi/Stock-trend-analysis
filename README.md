# Stock Trend Analysis - Data Science Project

[![Python](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.30-orange)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Project Overview
This project is a **Stock Trend Analysis Dashboard** that allows users to fetch historical stock data and visualize trends interactively. It provides insights into **price movement, volatility, and moving averages**, helping users understand stock behavior over time.

- Interactive dashboard using **Streamlit**
- Fetches real-time stock data via **Yahoo Finance (yfinance)**
- Visualizes trends using **Matplotlib** and **Plotly**
- Auto-refresh feature to keep data updated

---

## Features

1. **Fetch Stock Data**
   - Enter a stock ticker (e.g., `AAPL`, `TSLA`, `INFY.NS`) and select a date range.
   - Automatically fetches historical stock data.

2. **Price Trend Analysis**
   - Visualizes closing prices over time.
   - Calculates and plots **20-day moving average (MA20)**.

3. **Volatility Analysis**
   - Computes rolling **volatility** (standard deviation) over 20-day windows.
   - Visualizes volatility trends to assess risk.

4. **Interactive Metrics**
   - Shows latest price, change, and percentage change.
   - Highlights volatility dynamically.

5. **Recent Trends**
   - Visualizes the **last 50 days** of stock prices with markers.
   - Data tables for last 10 rows of stock history for quick review.

---

## Tools & Libraries

- **Python 3.x**  
- **yfinance** – To fetch stock data  
- **pandas** – Data manipulation and processing  
- **matplotlib** – Static plots  
- **plotly** – Interactive visualizations  
- **streamlit** – Dashboard UI  
- **streamlit_autorefresh** – Auto-refresh dashboard
