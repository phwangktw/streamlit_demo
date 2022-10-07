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




st.header('2. Style/Format check')
st.subheader('2-1. Style test')
style_size = st.text_input('Enter matrix size here', placeholder="n=2, 3, 4..etc", key='style')
style_option = st.selectbox(
    'Select the style you want to test',
    ('symmetric', 'upper', 'lower', 'diagonal'))
st.warning('In our test app, please manually break a new line to each row (only in app)', icon="⚠️")
st.warning('The first line myAwesomeMatrix Test X is automatically added from our grade script', icon="⚠️")
txt = st.text_area('Paste your test matrix', '''myAwesomeMatrix Test 7 \n
                     1 0 0 0 \n
                     0 1 0 0 \n
                     0 0 1 0 \n
                     0 0 0 1 \n
    ''')
if st.button('Go Check!'):
    count = test.extractNumbers_NoFormat_Square(txt, int(style_size), style_option)
    if count==0:
        st.success('PASS')
    else:
        st.error('%d non-match found' % (count))
        
        
st.subheader('2-2. Format test (TBD)')
        