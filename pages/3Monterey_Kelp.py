#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 17:17:40 2023

@author: rtsearcy
"""

import streamlit as st
import pandas as pd
from streamlit_extras.app_logo import add_logo
import os

# Streamlit App
st.set_page_config(layout="wide", page_icon = './nekton_logos/nekton_logo.png')

# Title bar
_, col, _ = st.columns([1,4,1])
with col:
    st.image('./nekton_logos/nekton_logo_blue.png')
    #st.title('Integrated Data System')

# hide streamlit components

# Sidebar

# add logo

add_logo("./nekton_logos/nekton_logo_blue_small.png", height=30)


# Hide Streamlit logos
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)



# # Content
_, col, _ = st.columns([1,3,1])
with col:
    st.subheader('Monterey Kelp Data Coming Soon')
    st.write('''Return to portfolio view or check out the VA Seagrass Project''')
       
    
    