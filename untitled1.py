import streamlit as st
import pandas as pd

# Function to load data
def load_data():
    data = pd.DataFrame({
        'Team': ['Chennai Super Kings', 'Deccan Chargers', 'Delhi Capitals', 'Gujarat Lions', 'Gujarat Titans', 
                 'Kochi Tuskers Kerala', 'Kolkata Knight Riders', 'Lucknow Super Giants', 'Mumbai Indians', 'Pune Warriors', 
                 'Punjab Kings', 'Rajasthan Royals', 'Rising Pune Supergiant', 'Royal Challengers Bangalore', 
                 'Sunrisers Hyderabad'],
        'Matches Played': [225, 75, 238, 30, 33, 14, 237, 30, 247, 46, 232, 206, 30, 241, 166],
        'Won': [131, 29, 105, 13, 23, 6, 119, 17, 138, 12, 104, 101, 15, 114, 78],
        'Lost': [91, 46, 127, 16, 10, 8, 114, 12, 105, 33, 124, 100, 15, 120, 84]
    })
    return data

# Function to calculate winning percentage
def calculate_winning_percentage(df):
    df['Winning Percentage'] = (df['Won'] / df['Matches Played']) * 100
    return df

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

# Winner Prediction Section
st.subheader('Predict the Winner')
team1_select = st.selectbox('Select Team 1:', ipl_data_with_percentage['Team'].unique())
team2_select = st.selectbox('Select Team 2:', ipl_data_with_percentage['Team'].unique())

if st.button('Predict Winner'):
    team1_data = ipl_data_with_percentage[ipl_data_with_percentage['Team'] == team1_select]
    team2_data = ipl_data_with_percentage[ipl_data_with_percentage['Team'] == team2_select]

    if not team1_data.empty and not team2_data.empty:
        if team1_data.iloc[0]['Winning Percentage'] > team2_data.iloc[0]['Winning Percentage']:
            winner = team1_select
        else:
            winner = team2_select
        st.success(f'The predicted winner is: {winner}')
