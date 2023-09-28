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
#add_logo("./nekton_logos/nekton_logo_blue_small.png", height=30)
add_logo("./nekton_logos/nekton_logo_small.png", height=75)

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
    st.write('Monterey Bay, CA, USA')
with col2:
    st.image('./data/kelp_symbol.png')

add_line()
        

# Site Metrics
col1, col2, col3 = st.columns([1,2,2])
with col1:
    col1.metric(label="Carbon Removed", 
                value='5,881  tCO2', 
                delta=+750,
                help= 'Total carbon removals you have purchased from this project (and the change this year')
    col1.metric(label="ECO", 
                value='4/5', 
                help= 'Cumulative score after assessing carbon, ecosystem, and social impacts of the project')
    col1.metric(label="SOCIO", 
                value='5/5', 
                help= 'Cumulative score after assessing carbon, ecosystem, and social impacts of the project')
    style_metric_cards()
    # st.write('Methodology:')
    # st.image('./data/verra_logo.png')

    
with col2:
    #st.header('Nekton Ocean IQ')
    
    names=['75','CO2','ECO','SOC','DATA','LEAK','PERM','UNCERT','WQ','BIO','EDU','JOB','OPEN']
    parents=['','75','75','75','75','CO2','CO2','CO2','ECO','ECO','SOC','SOC','DATA']
    values=[1000,250,200,200,100,100,75,50,60,80,100,100,100]
    
    fig = px.sunburst(names=names,
                      values=values,
                      parents=parents,
                      branchvalues='total'
                      )
                     
    fig.update_layout(
                        title={
                            'text': "Nekton Ocean IQ",
                            'y':0.9,
                            'x':0.05,
                            'xanchor': 'left',
                            'yanchor': 'bottom',
                            'font':{'family':"Helvetica", 'size':30}
                            }
                        )
    #                   polar = dict(
    #                           radialaxis = dict(range=[0, 5], showticklabels=False, ticks=''),
    #                           angularaxis = dict(showticklabels=True, tickfont={'size':20}, ticks='')))
    
    st.plotly_chart(fig, use_container_width=True)
    
col3.header('SDGs')
col3.image('./data/sdg_14_seal.png')
col3.write('''Dedicated efforts are underway to restore sea lion populations 
           along coastal regions. These initiatives aim to protect marine 
           biodiversity, ensure sustainable fishing practices, and preserve the 
           delicate balance of ocean ecosystems for future generations...''')
    

st.divider()

# Site Description
col1, col2 = st.columns([1,2])
with col1:
    st.header('Site Description')
    st.write('''Nestled along the shores of Monterey, California, this kelp restoration 
             site is a significant effort in advancing marine carbon sequestration 
             research. Through rigorous planning and meticulous ecosystem restoration, 
             the project developers aim to enhance carbon storage capacity by 
             revitalizing kelp forests in the region. This project, deeply rooted 
             in science and community involvement, seeks to not only understand the 
             intricacies of carbon capture by kelp but also actively engage local
             residents in the restoration process.''')
    st.write('''At the Monterey site, carbon storage is a focal point, as developers deploy 
            artificial kelp forests to measure their effectiveness in sequestering 
            carbon dioxide from the atmosphere. This endeavor aligns with a broader mission 
            to combat climate change by utilizing nature-based solutions. These efforts 
            extend beyond research, actively involving the local community in the 
            restoration project, fostering awareness and empowering residents to 
            contribute to marine ecosystem health and the mitigation of climate change. 
            Together, they are unlocking the potential of kelp ecosystems as a tool for 
            carbon capture while building a deeper connection between science and the 
            community.
             
             ''')
             
 
with col2: # Map
    os.environ["PLANET_API_KEY"] = '6b4d53883da74c35852dc7a342c42c74'
    map_center = [36.555, -121.951478]
    
    m = leafmap.Map(center=map_center, zoom=14)
    m.add_xyz_service("qms.Google Satellite")
    
    shp1 = './data/shapefiles/kelp_monterey1.shp'
    shp2 = './data/shapefiles/kelp_monterey2.shp'
    # shp3 = './data/shapefiles/VA_seagrass_2019.shp'
    
    style = {'fillOpacity': 0.1}
    
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

    # legend = LegendControl(legend={'2021':'yellow',
    #                                '2022':'orange',
    #                                 #'2019':'red'
    #                                 },
    #                                name="Year", position="topright")
    # m.add_control(legend)
    
    m.to_streamlit(height=500)

st.divider()


# col1, col2, col3 = st.columns(3)
# col1.image('./data/sdg_4.png')
# col1.write('The project proponents....')
# col2.image('./data/sdg_6.png')
# col2.write('The project proponents....')
# col3.image('./data/sdg_14.png')
# col3.write('The project proponents....')