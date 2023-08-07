import streamlit as st
def calculate_emi(p, n, r):
  emi = p * (r/100) * ((1+(r/100))**n)/(((1+(r/100))**n)-1)
  st.write("emi calculated = ", emi)
st.title("EMI calculator")
p=st.slider("loan amount", 100000,10000000)
n=st.slider("tenure", 24,36)
r=st.slider("interest", 12,16)
if st.button("calculate"):
  calculate_emi(p)
