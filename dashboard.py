import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Install necessary packages
st.title("Installing Dependencies")
st.write("This may take a minute.")
st.info("Installing dependencies...")
st.code("pip install pandas streamlit matplotlib seaborn")

# Once the installation is complete, remove the installation message
st.success("Dependencies installed successfully!")
st.balloons()

# Load data from GitHub
url = "https://raw.githubusercontent.com/fulazz/911-dashboard/main/shopping_new.csv"
df = pd.read_csv(url)

# Create a Streamlit app
st.title("Shopping Dashboard")

# Display some basic information about the data
st.write("### Sample Data:")
st.dataframe(df.head())

# Summary Statistics
st.write("### Summary Statistics:")
st.write(df.describe())

# Visualize order count and revenue on a daily basis
daily_orders_df = create_daily_orders_df(df)
st.write("### Daily Order Count and Revenue:")
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
sns.lineplot(data=daily_orders_df, x='order_date', y='order_count', ax=ax1, color='b', label='Order Count')
sns.lineplot(data=daily_orders_df, x='order_date', y='revenue', ax=ax2, color='r', label='Revenue')
ax1.set_xlabel('Date')
ax1.set_ylabel('Order Count', color='b')
ax2.set_ylabel('Revenue', color='r')
st.pyplot(fig)

# Visualize product category distribution
st.write("### Product Category Distribution:")
plt.figure(figsize=(10, 6))
sns.countplot(data=df, y='product_category_name', order=df['product_category_name'].value_counts().index)
plt.xlabel('Count')
plt.ylabel('Product Category')
st.pyplot()

# Map showing the distribution of customers
st.write("### Customer Distribution Map:")
# Add code to create a map (if geographical information is available)

# Display the raw data (optional)
if st.checkbox("Show Raw Data"):
    st.write("### Raw Data:")
    st.dataframe(df)
# Convert 'order_purchase_timestamp' to datetime
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

# Streamlit App
st.title('Olist E-commerce Dashboard')

# Bar chart comparing seller_state and customer_state
fig1 = px.bar(df, x=['seller_state', 'customer_state'], title='Seller State vs Customer State')
st.plotly_chart(fig1)

# Line graph showing trend order purchase by month
df['order_month'] = df['order_purchase_timestamp'].dt.to_period('M')
fig2 = px.line(df.groupby('order_month').size().reset_index(name='order_count'), x='order_month', y='order_count', title='Order Purchase Trend by Month')
st.plotly_chart(fig2)

# Bar chart showing top 5 product sells
top_products = df['product_category_name'].value_counts().head(5)
fig3 = px.bar(top_products, x=top_products.index, y=top_products.values, title='Top 5 Product Sells')
st.plotly_chart(fig3)

# Monthly income from variable price and order_purchase_timestamp
monthly_income = df.groupby('order_month')['price'].sum().reset_index()
fig4 = px.bar(monthly_income, x='order_month', y='price', title='Monthly Income')
st.plotly_chart(fig4)

# Run the Streamlit app
st.show()


