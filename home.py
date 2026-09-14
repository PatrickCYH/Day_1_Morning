import streamlit as st



#Exercise 1.1
st.header("Exercise 1.1")

st.write("Hello world!")



#Exercise 1.2
st.header("Exercise 1.2")

name = st.text_input("What is your name?")
st.write("Your name is",name)



#Exercise 1.3
st.header("Exercise 1.3")

if st.button("Say Hi!"):
    st.write(f"Welcome, {name}!")

if (name == "Jack"):
    st.write("You are in fact not welcome!")



#Sub-boxes (Dictionary = person)
st.header("Dictionary")

person = {
    "name": "Jack",
    "age": 34,
    "occupation": "lawyer"
}

st.write(person.get("name"),"is a",person.get("occupation"))



#Exercise 1.4
st.header("Exercise 1.4")

name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value = 0)

dictionary = {
    "name":name,
    "age":age
}

if st.button("Click the button"):
    st.write(f"Hello, {dictionary.get("name")}. I understand you are {dictionary.get("age")} years old.")

#Exercise 1.6
st.header("Exercise 1.6")

name = st.text_input("Enter your name_2")
age = st.number_input("Enter your age_2", min_value = 0)

dictionary = {
    "name":name,
    "age":age
}

if st.button("Click the button_2") and dictionary.get("name") == True and dictionary.get("age") >= 0:
    st.write(f"Hello, {dictionary.get("name")}.")
    if dictionary.get("age") <= 24:
        st.write("You were born this millennium")
    else:
        st.write("You were born last millennium")
else:
    st.write("Fill in the blank")