import pandas as pd
import streamlit as st
data = {
    "Product" : ['laptop','mobile','smartwatch','earbuds','headphones'],
    "Category" :['electronics','electronics','wearables','hearables','hearables'],
    "Sales" : [2000,3000,4000,6000,7000] 
    }
df = pd.DataFrame(data)
st.header("Sales Data")
# Sidebar Filter
st.sidebar.header("Filter Options")
category = st.sidebar.selectbox("Select Category", df["Category"].unique())

# Filter Data
filtered_df = df[df["Category"] == category]

# Display Data
st.write(f"### Showing data for: {category}")
st.dataframe(filtered_df)

# Line Chart
st.write("### Sales Trend")
st.line_chart(filtered_df["Sales"])