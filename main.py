# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 09:36:54 2022

@author: phwangk
"""

import streamlit as st
import selftesting as test
# import re

st.set_page_config(layout="centered", page_icon="🎓", page_title="ME369/ME396/ES122 Assignment2")
st.title("🎓 MyAwesomeMatrix Class Self-Test")

st.write(
    "This app provide a function for students to test their assignement2-Q1 (noted: this just for testing purpose, it will not be our final official grading script"
)

st.header('1. Normalization methods test')

st.subheader('Step1: Input your test matrix as a `list` structure ')

size = st.text_input('Enter matrix size here', placeholder="n=2, 3, 4..etc")
matrix_input = st.text_input('Enter matrix details here', placeholder="[[1, 3, 3],[2, 1, 3],[4, 3, 3]]")

st.subheader('Step2: Click Submit ')
if st.button('Submit'):        
        
    a = test.gNorm(matrix_input, size)
    b = test.oneNorm(matrix_input, size)
    st.write('Groot Norm result is %.2f' %a)
    st.write('One Norm result is %d' %b)




st.header('2. Format check (TBD, developing)')