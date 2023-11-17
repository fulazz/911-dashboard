import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

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

# Run the Streamlit app
st.show()


