import streamlit as st
st.set_page_config(page_title='Cats')
st.header("Types of Cats and heros")

col1, col2 = st.columns(2)
with col1:
  st.subheader("Persian Cat")
  st.image("./dog-puppy-on-garden-royalty-free-image-1586966191.jpg", caption="Persian Cat", width=300,use_column_width=True)
  st.write("Persian cats are cute")
with col2:
  st.subheader("hero")
  st.image("./prabha.jpeg", caption="Ragdoll Cat", width=300,use_column_width=True)
  st.write("hero are proud")
