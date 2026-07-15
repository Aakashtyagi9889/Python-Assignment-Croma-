import streamlit as st

# st.set_page_config(layout= 'wide' , page_title='Chai-Code')
st.title("My Practice Page")
st.header("Here You can chose your Favourite Programming langugae! ")
st.subheader('__________________________________________________________________________')
lang = st.selectbox("Choose Your favourite langugae" , ['Python' , 'Java' , 'C' , 'C++' , 'C#'] , index = None)
st.success(f"Congrats! {lang}")

st.slider("choose sugar spoon" , 0 , 5 , 4)
st.time_input('enter time')
st.text_input("Enter Text")


st.number_input("Enter Number" , min_value=1 , max_value=10 , step=1)

