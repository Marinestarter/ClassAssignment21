import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

year_range = st.slider('Select a year range', 2010, 2020, (2010, 2020))

if st.button('Show Analysis'):
    # Logic to compute total/average sales
    st.write('Displaying additional insights')

data = {
    'Year': [2010, 2011, 2012, 2013, 2014, 2015],
    'Region': ['North', 'South', 'East', 'West', 'North', 'South'],
    'Sales Amount': [1000, 1500, 1200, 1700, 1600, 1800]
}
df = pd.DataFrame(data)
st.dataframe(df)

# Filter data based on selected year range
filtered_data = df[(df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])]

# Plot using matplotlib
fig, ax = plt.subplots()
ax.bar(filtered_data['Year'], filtered_data['Sales Amount'])
st.pyplot(fig)

col1, col2 = st.columns(2)
with col1:
    st.header("First Column")
    st.write("hello")
with col1:
    st.header("Second Column")
    st.write("World")

with st.expander("see explanation"):
    st.write("here you could put stuff to explain things in more details.")



