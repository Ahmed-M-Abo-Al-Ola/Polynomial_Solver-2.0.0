import streamlit as st
from maths import *

st.title("Welcome to Polynomial Solver")
highest_degree = int(st.number_input('Enter Higest Degree', min_value=1))
cff = []
columns = st.columns(int(highest_degree) + 1)
for i in reversed(range(int(highest_degree) + 1)):
    with columns[i]:
        cffi = st.number_input(f"Enter Coefficint for x^({i})", key=i)
        cff.append(int(cffi))

Start = st.button('Start')
if Start:
    result = zeros(highest_degree,cff)
    st.write(result)