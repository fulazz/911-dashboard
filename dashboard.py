import pandas as pd
import streamlit as st
import plotly.express as px

# Load data from GitHub
url = "https://raw.githubusercontent.com/fulazz/911-dashboard/main/shopping_new.csv"
df = pd.read_csv(url, low_memory=False)  # Add low_memory=False to handle DtypeWarning

# Create a Streamlit app
st.title("E-Commerce Public Dataset Dashboard")

# Visualize product category distribution
st.write("### Product Category Distribution:")

# Use plotly express to create a bar chart
fig_category = px.bar(df['product_category_name'].value_counts().reset_index(), x='index', y='product_category_name',
                      labels={'index': 'Product Category', 'product_category_name': 'Count'},
                      title='Product Category Distribution')

# Display the plot using st.plotly_chart
st.plotly_chart(fig_category)

# Display the raw data (optional)
if st.checkbox("Show Raw Data"):
    st.write("### Raw Data:")
    st.dataframe(df)

# Convert 'order_estimated_delivery_date' to datetime
df['order_estimated_delivery_date'] = pd.to_datetime(df['order_estimated_delivery_date'])

# The rest of your Streamlit app remains the same...
