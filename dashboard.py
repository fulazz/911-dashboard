import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
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

# Bar chart comparing seller_state and customer_state
st.title('Olist E-commerce Dashboard: Seller State vs Customer State')
fig_seller_customer_state = px.bar(df, x=['seller_state', 'customer_state'], title='Seller State vs Customer State')
st.plotly_chart(fig_seller_customer_state)

# Line graph showing trend order purchase by month
df['month_year'] = pd.to_datetime(df['month_year'])
st.title('Olist E-commerce Dashboard: Order Purchase Trend by Month')
fig_order_trend = px.line(df.groupby('month_year').size().reset_index(name='order_count'), x='month_year', y='order_count', title='Order Purchase Trend by Month')
st.plotly_chart(fig_order_trend)

# Bar chart showing top 5 product sells
st.title('Olist E-commerce Dashboard: Top 5 Product Sells')
top_products = df['product_category_name'].value_counts().head(5).reset_index()
fig_top_products = px.bar(top_products, x='index', y='product_category_name', title='Top 5 Product Sells')
st.plotly_chart(fig_top_products)

# Monthly income from variable price and order_estimated_delivery_date
st.title('Olist E-commerce Dashboard: Monthly Income')
monthly_income = df.groupby('month_year')['price'].sum().reset_index()
fig_monthly_income = px.bar(monthly_income, x='month_year', y='price', title='Monthly Income')
st.plotly_chart(fig_monthly_income)
