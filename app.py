# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import datetime

from price_optimizer import load_data, apply_margin_strategy
from ai_models import predict_price, predict_category
from excel_exporter import generate_excel_with_formulas

# Configure Streamlit page
st.set_page_config(page_title="Home Services Pricebook Optimizer", layout="wide")
st.title("🔧 Home Services Pricebook Optimizer")

# 📤 File Upload or Load Default
uploaded_file = st.file_uploader("Upload your home services CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully.")
else:
    st.info("ℹ️ No file uploaded. Showing demo dataset.")
    df = load_data()

# Ensure required computed columns exist
df['Total Cost'] = df['Labor Cost'] + df['Material Cost']
df['Profit Margin (%)'] = round(((df['Price'] - df['Total Cost']) / df['Price']) * 100, 2)

# Show original dataset
st.subheader("📄 Original Pricebook Data")
st.dataframe(df)

# 📊 Margin Distribution Plot
st.subheader("📊 Profit Margin Distribution by Category")
fig, ax = plt.subplots()
df.boxplot(column='Profit Margin (%)', by='Category', ax=ax)
plt.title('Profit Margin by Category')
plt.suptitle("")
plt.ylabel('Margin %')
plt.xticks(rotation=45)
st.pyplot(fig)

# 📈 Linear Regression Curve: Total Cost vs Price
st.subheader("📈 Price vs Total Cost with Trend Line")
X = df[['Total Cost']]
y = df['Price']
model = LinearRegression()
model.fit(X, y)
trend = model.predict(X)

fig2, ax2 = plt.subplots()
ax2.scatter(df['Total Cost'], df['Price'], color='blue', label='Actual')
ax2.plot(df['Total Cost'], trend, color='red', label='Trend Line')
ax2.set_xlabel('Total Cost')
ax2.set_ylabel('Price')
ax2.set_title('Price vs Total Cost with Regression Line')
ax2.legend()
st.pyplot(fig2)

# 📈 Profit Margin Optimization
margin = st.slider("📈 Set Target Profit Margin (%)", min_value=10, max_value=80, value=50, step=5)
df_optimized = apply_margin_strategy(df.copy(), margin)

# 🧠 Bulk AI Price Predictor
if st.button("🚀 Run AI Bulk Price Predictor"):
    df['AI Predicted Price'] = df.apply(
        lambda row: predict_price(row['Labor Cost'], row['Material Cost']), axis=1
    )
    st.success("✅ AI prices predicted and added to table!")
    st.subheader("🧠 AI Predicted Prices for All Services")
    st.dataframe(df[['Service', 'Labor Cost', 'Material Cost', 'Price', 'AI Predicted Price']])

# 💰 Optimized Pricing Table
st.subheader("💰 Suggested Pricing Based on Target Margin")
st.dataframe(df_optimized)

# 📥 Download Optimized Pricebook (CSV)
csv = df_optimized.to_csv(index=False).encode("utf-8")
st.download_button(
    label="📥 Download Optimized Pricebook (CSV)",
    data=csv,
    file_name=f"optimized_pricebook_margin_{margin}pct.csv",
    mime="text/csv"
)

# 📥 Download Optimized Pricebook with Excel Formulas
excel_buffer = generate_excel_with_formulas(df_optimized)
st.download_button(
    label="📥 Download Excel with Formulas",
    data=excel_buffer,
    file_name="optimized_pricebook_with_formulas.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

# 🤖 AI Tools – Sidebar
st.sidebar.header("🤖 AI Tools")
st.sidebar.subheader("🔮 Predict Price")

# Input fields
labor = st.sidebar.number_input("Labor Cost ($)", min_value=0)
material = st.sidebar.number_input("Material Cost ($)", min_value=0)

# Predict price
if st.sidebar.button("Predict Service Price"):
    predicted_price = predict_price(labor, material)
    st.sidebar.success(f"Suggested Price: ${predicted_price}")

# Predict category
st.sidebar.subheader("📌 Predict Service Category")
if st.sidebar.button("Suggest Category"):
    predicted_category = predict_category(labor, material)
    st.sidebar.success(f"Predicted Category: {predicted_category}")

# 📝 Session Logger
st.sidebar.subheader("📋 Session Logger")
log_path = "session_log.txt"

if st.sidebar.button("📝 Log This Prediction Session"):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_path, "a") as f:
        f.write(f"{now} | Labor: ${labor} | Material: ${material}\n")
    st.sidebar.success("📌 Logged successfully!")

# Show session log
try:
    with open(log_path, "r") as f:
        logs = f.read()
        st.sidebar.text_area("📄 Session Log", logs, height=150)
except FileNotFoundError:
    st.sidebar.info("No session log found yet.")
