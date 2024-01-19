import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# [Previous code for loading data and calculating winning percentage]

# Load the IPL data
ipl_data = load_data()

# Calculate winning percentage
ipl_data_with_percentage = calculate_winning_percentage(ipl_data)

# Streamlit app layout
st.title('IPL Team Performance Dashboard')

# Display the dataframe with winning percentage
st.write("IPL Team Data:")
st.dataframe(ipl_data_with_percentage)

# Bar Chart for Total Wins
st.write("Total Wins by Team:")
st.bar_chart(ipl_data_with_percentage[['Team', 'Won']].set_index('Team'))

# Interactive Team Selection for Pie Chart
team_for_pie_chart = st.selectbox('Select a Team for Win/Loss Distribution:', ipl_data_with_percentage['Team'].unique())
team_data = ipl_data_with_percentage[ipl_data_with_percentage['Team'] == team_for_pie_chart]

# Pie Chart for Win/Loss Distribution
if not team_data.empty:
    fig, ax = plt.subplots()
    ax.pie([team_data.iloc[0]['Won'], team_data.iloc[0]['Lost']], labels=['Wins', 'Losses'], autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
    st.write(f"Win/Loss Distribution for {team_for_pie_chart}")
    st.pyplot(fig)

# Histogram for Match Distribution
st.write("Distribution of Matches Played by Teams")
st.bar_chart(ipl_data_with_percentage['Matches Played'])

# [Rest of your code for Winner Prediction]
