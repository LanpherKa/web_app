# views/overview.py
import streamlit as st
import backend

st.title("Illegal Dumping in Philadelphia Overview")

#test backend

numbers = backend.show_data()

st.subheader("Backend Test")
for number in numbers:
    st.write(number)

#image test
st.subheader("Image Test")
st.image("assets/cats.jpg", width= 300,  caption="Mrs. Lanpher's Cats Please Change")