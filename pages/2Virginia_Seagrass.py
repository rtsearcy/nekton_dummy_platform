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
import leafmap.foliumap as leafmap
#import leafmap
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
    st.header('Virginia Coast Reserve Seagrass Restoration Project')
    st.write('Virginia, USA')
with col2:
    st.image('./data/seagrass_symbol.png')

add_line()
        

# Site Metrics
col1, col2 = st.columns([1,2])
with col1:
    col1.metric(label="Nekton Ocean IQ", 
                value='B', 
                help= 'Cumulative score after assessing carbon, ecosystem, and social impacts of the project')
    col1.metric(label="Carbon Removed", 
                value='1,953  tCO2', 
                delta=+400,
                help= 'Total carbon removals you have purchased from this project (and the change this year')
    style_metric_cards()
    st.write('Verifying Agency:')
    st.image('./data/verra_logo.png')

    
with col2:
    
    df = pd.DataFrame(dict(
                        r=[4, 5, 3, 3],
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
    st.write('''The Virginia Coast Reserve (VCR), managed by The Nature 
             Conservancy’s (TNC) Virginia State Chapter, encompasses 
             protected lands and coastal bays of the Virginia Eastern 
             Shore that constitute the longest expanse of coastal 
             wilderness remaining on the United States East Coast.
             ''') 
    st.write('''
             Seagrass restoration directly increases carbon storage 
             in submerged aquatic vegetation (SAV) and marine 
             sediments, enhancing greenhouse gas (GHG) emission 
             removals from the atmosphere. Over the 30-year 
             crediting period the project activity is estimated 
             to generate 40,486t CO2e net GHG emission removals. (VERRA)
             ''')
             
 
with col2: # Map
    os.environ["PLANET_API_KEY"] = '6b4d53883da74c35852dc7a342c42c74'
    map_center = [37.2, -75.85]
    
    m = leafmap.Map(center=map_center, zoom=11)
    m.add_planet_by_month(year=2022, month=10)
    
    shp1 = './data/shapefiles/VA_seagrass_2021.shp'
    shp2 = './data/shapefiles/VA_seagrass_2020.shp'
    shp3 = './data/shapefiles/VA_seagrass_2019.shp'
    
    style = {'fillOpacity': 0.3}
    
    m.add_shp(
        shp1,
        layer_name="2021",
        style=style,
        fill_colors=['yellow'])
    
    m.add_shp(
        shp2,
        layer_name="2020",
        style=style,
        fill_colors=['orange'])
    
    m.add_shp(
        shp3,
        layer_name="2019",
        style=style,
        fill_colors=['red'])
    
    # legend = LegendControl(legend={'2021':'yellow',
    #                                 '2020':'orange',
    #                                 '2019':'red'}, name="Year", position="topright")
    # # m.add_control(legend)
    
    m.to_streamlit(height=500)

st.divider()


col1, col2, col3 = st.columns(3)
col1.image('./data/sdg_4.png')
col1.write('The project proponents....')
col2.image('./data/sdg_6.png')
col2.write('The project proponents....')
col3.image('./data/sdg_14.png')
col3.write('The project proponents....')