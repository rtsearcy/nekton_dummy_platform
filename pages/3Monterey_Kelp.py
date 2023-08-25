#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 17:17:40 2023

@author: rtsearcy
"""

import streamlit as st
import pandas as pd
import os

# Import  data


# Streamlit App
st.set_page_config(layout="wide", page_icon = './nekton_logos/nekton_logo.png')

# Title bar
_, col, _ = st.columns([1,4,1])
with col:
    st.image('./nekton_logos/nekton_logo_blue.png')
    #st.title('Integrated Data System')

# hide streamlit components

# Sidebar
def add_sidebar_title():
    st.markdown(
        """
        <style>
            
              [data-testid="stSidebarNav"]::before {
                content: "Nekton Labs Platform";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 50px;
                
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
add_sidebar_title()

# Hide Streamlit logos
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# # Content
with st.expander('Overview'):
    st.write('''
              Nekton's Integrated Data System is the engine behind all of the
              Nekton ocean MRV models and data products. Our data have been
              specifically curated to be effectively used to improve ocean health.
              ''')
#     st.write('''
#              It contains an aggregation of environmental
#              data from public and private sources into a single organized 
#              repository. These data are efficiently available for our tools 
#              and products. Some upcoming features include:
#                  ''')
#     st.write('1. Automated ingestion, pre-processing, analyses/visualizations')
#     st.write('2. Data fusion techniques to increase compatibility and facilitate modeling')
#     st.write('''3. AI-based quality testing of and knowledge generation from the data, 
#              including NLP performed on thousands of peer-reviewed papers and 
#              semantic data matching to identify and link related data
            
#              ''')
#     st.write('''The system will be cloud-based, API-accessible, scalable, and secure.''')

# st.write('Some of our sources:')
# logos = os.listdir('./source_logos')
# col1, col2, col3 = st.columns(3)
# with col1:
#     st.image(os.path.join('./source_logos/', logos[0]))
#     st.image(os.path.join('./source_logos/', logos[1]))
#     st.image(os.path.join('./source_logos/', logos[2]))

# with col2:
#     st.image(os.path.join('./source_logos/', logos[3]))
#     st.image(os.path.join('./source_logos/', logos[4]))
#     st.image(os.path.join('./source_logos/', logos[5]))

# with col3:
#     st.image(os.path.join('./source_logos/', logos[6]))
#     st.image(os.path.join('./source_logos/', logos[7]))
    
    
    