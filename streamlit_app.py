import streamlit
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.title('My parents new healthy diner')
   
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 and bluberry oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket smoothie')
streamlit.text('🐔 Hard-Boiled free-range egg')
streamlit.text('🥑🍞 Avocado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),['Avocados','Strawberries'])
streamlit.dataframe(my_fruit_list)
