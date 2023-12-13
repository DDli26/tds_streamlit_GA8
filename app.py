import streamlit as st

st.title("Abhinandan's App to find Largest among 3 numbers")

def code(x,y,z):
  answer = max(x,y,z)
  return answer

x = st.number_input("first number : ")
y = st.number_input("second number : ")
z = st.number_input("third number : ")

st.write("The Largest Number = ", code(x,y,z))
