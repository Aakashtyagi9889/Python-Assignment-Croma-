#pip install streamlit

#To run the file (streamlit run 0040-Streamlit-intro.py)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(layout="wide" , page_title='My First Page!')
st.title("My First Web Application")
st.header("My First Heading")
st.subheader("My Second Heading")
st.text("My Normal Text Flows here!")
text = st.text_input("")
st.write(f"your input is : {text}")

Name= st.text_input("Enter Your Full Name : ")
st.text(f"Your Name is : {Name}")

st.number_input("Enter Your Phone Number :  ")

st.selectbox("Select Your Course" , ['Data Analytics' , 'Data Engineering'])

st.radio("Select Gender" ,  ['Male' , 'Female'])

# st.html("<style>" \
# "body{" \
# "background-color:red;" \
# "}" \
# "</style>")


df = pd.read_excel(f"E:\Croma\Python\Jupyter Notebook LocalComputer\Financial_Sample.xlsx")
st.dataframe(df , height=200) # show data like Excel
st.write(df)    # show data like Excel
st.text(df) # it is like df in pandas it only shows first 5 and last 5 data 

#check profit by segment :
pbs =  df.groupby('Segment')['Profit'].sum().reset_index()
# pbs1 =  df.groupby('Segment').agg({'Profit' : 'sum'}).reset_index()
st.dataframe(pbs)
# st.dataframe(pbs1)


#Show in bar chart 
fig ,  ax = plt.subplots(figsize = (12,3))
ax.bar(pbs['Segment'] , pbs['Profit'])
st.pyplot(fig)

#metric
st.metric('Total Profit' , round(df.Profit.sum(),2))

#chart using seaborn

fig , ax = plt.subplots(figsize = (12,4))
sns.histplot(x = 'Profit' , kde = True , data=df)
st.pyplot(fig)

