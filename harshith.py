import streamlit as st
st.set_page_config(page_title='dogs and hero')
st.header("Types of dogs and heros")

col1, col2 = st.columns(2)
with col1:
  st.subheader("Persian dog")
  st.image("./dog-puppy-on-garden-royalty-free-image-1586966191.jpg", caption="Persian dog", width=300,use_column_width=True)
  st.write("Persian dog are cute")
with col2:
  st.subheader("hero")
  st.image("./prabha.jpeg", caption="hero", width=300,use_column_width=True)
  st.write("hero are proud")
