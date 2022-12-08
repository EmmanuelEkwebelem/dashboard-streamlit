import pandas 
import streamlit 

# Load Data CSVs
Education = pandas.read_csv('data/education_data.csv')
Layoffs = pandas.read_csv('data/layoffs_data.csv')

# Header
streamlit.header('US Education Level & Layoff Data')

### Dataset # 1 ###
# Dropdown Checkbox to View Data
if streamlit.checkbox('US Education Level Data'):
    streamlit.dataframe(Education)    
# Barchart
streamlit.subheader('Bar Chart Visual of Level of Education in US')
US_Education_Level = Education.loc[Education['native-country'] == ' United-States']['Education'].value_counts()
streamlit.bar_chart(US_Education_Level)
streamlit.caption('This Figure Illustrates the Education Level of US Citizens')

### Dataset # 2 ###
# Dropdown Checkbox to View Data
if streamlit.checkbox('US Layoffs Data'):
    streamlit.dataframe(Layoffs)
# Line Chart
streamlit.subheader('Line Chart Visual of Layoffs in US')
US_Layoffs = Layoffs.loc[Layoffs['Country'] == 'United States']['Industry'].value_counts()
streamlit.line_chart(US_Layoffs)
streamlit.caption('This Figure Illustrates The Number of Layoffs in Each State In the US')

# Code Block
code = '''## Code for Dropdown Check Box to View Layoff Data
if streamlit.checkbox('US Layoffs Data'):
    streamlit.dataframe(Layoffs)'''
streamlit.code(code, language='python')

