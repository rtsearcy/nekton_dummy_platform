#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 17:17:40 2023

@author: rtsearcy
"""

import streamlit as st
from streamlit_extras.app_logo import add_logo
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.colored_header import colored_header
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.add_vertical_space import add_vertical_space
#import leafmap.foliumap as leafmap
import leafmap
from ipyleaflet import LegendControl
from folium import Icon
from streamlit_folium import st_folium
import plotly.express as px

import pandas as pd
import os

## Functions
def add_line(c='light-blue-60'):
    colored_header(
        label="",
        description="",
        color_name=c,
    )


## Load Data
projects = pd.read_csv(os.path.join('.','data','dummy_projects.csv'))
projects['location'] = list(zip(projects.lat,projects.lon))

# Streamlit App
st.set_page_config(layout="wide", page_icon = './nekton_logos/nekton_logo.png')

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

# Title bar
col1, col2 = st.columns([9,1])
with col1:
    st.header('Monterey Kelp Restoration Project')
    st.write('Monterey Bay, CA, USA (For illustrative purposes only)')
with col2:
    st.image('./data/kelp_symbol.png')

add_line()
        

# Site Metrics
col1, col2 = st.columns([1,2])
with col1:
    col1.metric(label="Nekton Ocean IQ", 
                value='B+', 
                help= 'Cumulative score after assessing carbon, ecosystem, and social impacts of the project')
    col1.metric(label="Carbon Removed", 
                value='5,881  tCO2', 
                delta=+750,
                help= 'Total carbon removals you have purchased from this project (and the change this year')
    style_metric_cards()
    # st.write('Methodology:')
    # st.image('./data/verra_logo.png')

    
with col2:
    
    df = pd.DataFrame(dict(
                        r=[5, 4, 2, 3],
                        theta=['Carbon Removal Quality',
                               'Ecosystem Co-Benefit',
                               'Community Co-Benefit ',
                               'Transparency']))
    
    fig = px.line_polar(df, r='r', theta='theta', line_close=True)
    
    fig.update_traces(fill='toself')
    
    fig.update_layout(
                      # title={
                      #     'text': "Nekton Ocean IQ",
                      #      'y':0.95,
                      #      'x':0.5,
                      #      'xanchor': 'center',
                      #      'yanchor': 'bottom',
                      #     'font':{'family':"Helvetica", 'size':30}
                      #     },
                      polar = dict(
                              radialaxis = dict(range=[0, 5], showticklabels=False, ticks=''),
                              angularaxis = dict(showticklabels=True, tickfont={'size':20}, ticks='')))
    
    st.plotly_chart(fig, use_container_width=True)
    
st.divider()

# Site Description
col1, col2 = st.columns([1,2])
with col1:
    st.header('Site Description')
    st.write('''Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
             sed do eiusmod tempor incididunt ut labore et dolore magna 
             aliqua. Dignissim enim sit amet venenatis urna. Consectetur 
             adipiscing elit duis tristique sollicitudin nibh sit amet 
             commodo. Tincidunt augue interdum velit euismod. Hac 
             habitasse platea dictumst vestibulum rhoncus est 
             pellentesque elit. Ipsum faucibus vitae aliquet 
             nec ullamcorper sit amet risus. Dictum sit amet 
             justo donec enim. Neque egestas congue quisque 
             egestas diam in arcu cursus euismod. Tortor id aliquet 
             lectus proin nibh nisl condimentum id. Feugiat sed 
             lectus vestibulum mattis ullamcorper velit sed ullamcorper.
             
             ''')
             
 
with col2: # Map
    os.environ["PLANET_API_KEY"] = '6b4d53883da74c35852dc7a342c42c74'
    map_center = [36.52, -121.951478]
    
    m = leafmap.Map(center=map_center, zoom=13)
    m.add_xyz_service("qms.Google Satellite")
    
    shp1 = './data/shapefiles/kelp_monterey1.shp'
    shp2 = './data/shapefiles/kelp_monterey2.shp'
    # shp3 = './data/shapefiles/VA_seagrass_2019.shp'
    
    style = {'fillOpacity': 0.3}
    
    m.add_shp(
        shp1,
        layer_name="2021",
        style=style,
        fill_colors=['yellow'])
    
    m.add_shp(
        shp2,
        layer_name="2022",
        style=style,
        fill_colors=['orange'])
    
    # m.add_shp(
    #     shp3,
    #     layer_name="2019",
    #     style=style,
    #     fill_colors=['red'])
    
    legend = LegendControl(legend={'2021':'yellow',
                                   '2022':'orange',
                                    #'2019':'red'
                                    },
                                   name="Year", position="topright")
    m.add_control(legend)
    
    m.to_streamlit(height=500)

st.divider()


col1, col2, col3 = st.columns(3)
col1.image('./data/sdg_4.png')
col1.write('The project proponents....')
col2.image('./data/sdg_6.png')
col2.write('The project proponents....')
col3.image('./data/sdg_14.png')
col3.write('The project proponents....')