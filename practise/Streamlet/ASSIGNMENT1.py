# Part A - Basic UI
# Create a Streamlit page with:
# Page Title
# Wide Layout
# Custom Title
# Display
# Header
# Subheader
# Text
# Markdown
# Take user input:
# Name
# Age
# City
# Display all entered values using st.write().

import streamlit as st
# st.set_page_config( layout='wide' , page_title="My First Assignment")
st.title("My First Assignment")
st.header('This is header')
st.subheader('This is Subheader')
st.text('Normal Text')
st.markdown('###markdown')
Name = st.text_input("Enter Your Name: ")
Age = st.number_input('Enter Age', min_value=1 , max_value=110 )
City = st.text_input('Enter Your City : ')
st.write(f'Your Name is {Name} Age = {Age} and Your city is {City}')


# Create a slider for Age (18-60).
# Create a Number Input for Salary.
# Create a Radio Button
slider = st.slider('Select Age',18,60,25)
st.write(slider)

salary = st.number_input('Enter Salary : ', min_value= 10000,max_value= 50000  ,step= 1000 )
st.write(salary)

st.radio('Select Gender' , ['Male' , 'Female' , 'Other'])

# Q8. SelectBox
st.selectbox('Choose Course : ' , ['python' , 'PowerBi' , 'Databricks' , 'Snowflakes'])

# Q9. MultiSelect
multi = st.multiselect('Choose Course : ' , ['python' , 'PowerBi' , 'Databricks' , 'Snowflakes'])

# Q10. Show Selected Skills
for i in multi:
  st.write(i)
