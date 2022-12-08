# Importing packages
import pandas as pd
import streamlit as st

# Loading dataset
registry_df = pd.read_csv('follow_up.csv')
vehicle_df = pd.read_csv('vehicle_accident_data1.csv')
# Creating a dashboard header
st.header('Patient Follow-Up & Vehicle Accident Data')

# Creating a caption
st.caption('Patient follow-up recorded within the last year')

# Displaying the dataframe
if st.checkbox('Hospital 03 Follow-Up'):
    st.dataframe(registry_df)

if st.checkbox('Vehicle Accident Data'):
    st.dataframe(vehicle_df)

# Creating a barchart
st.subheader('Display of Patients Primary Hospital')
hosp_num = registry_df['Hospital_Code'].value_counts()
st.bar_chart(hosp_num)
st.caption('Visual provides insight of the number of patients per hospital')

# Creating a line chart
st.subheader('Accidents based on the Day of the Week')
day_week = vehicle_df['Day_of_Week'].value_counts()
st.bar_chart(day_week)
st.caption('Visual provides insight on the popular days of the week for accidents')

# Creating a code block
code = '''## Code behind the Bar Chart for Day of the Week
day_week = vehicle_df['Day_of_Week'].value_counts()
st.bar_chart(day_week)'''
st.code(code, language='python')