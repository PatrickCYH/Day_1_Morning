import streamlit as st

#Exercise 1.1
st.title("Hello world!")

#Exercise 1.2
name = st.text_input("What is your name?")
st.write("Your name is",name)

#Exercise 1.3
st.write(f"Welcome, {name}!")