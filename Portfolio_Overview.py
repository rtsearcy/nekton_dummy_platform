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


## Initiate Streamlit App
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


# Title bar
col1, col2 = st.columns([9,1])
with col1:
    st.title('United Tools Corp.')
#with col2:
    #st.image('./nekton_logos/nekton_logo.png')
    #st.title('Integrated Data System')
    
add_line()
    
# Overall Metrics 
col1, col2, col3 = st.columns(3)
col1.metric(label="Removed", value='29,543 tCO2', delta='+11,000',
            help= 'Total carbon removed by your projects (and the change this year')
col2.metric(label="Invested", value='$ 359,294', delta='+$13,000',
            help= 'Amount your organization has invested in CDR solutions')
col3.metric(label="Projects", value=projects.projects.sum(), delta=2,
            help='Number of projects in your portfolio')
#style_metric_cards()
add_line()


# Overview charts
col1, col2, col3 = st.columns([9,9,1])
with col1:
    #st.header('Portfolio Ocean IQ')
    
    names = ['BC','Kelp','OAE', 
              'Tomales','Baja','Virginia','Monterey','S. Africa','Spain',
              '92','90', '84', '75', '82', '80']
    parents = ['','','',
                'BC','BC','BC','Kelp','Kelp','OAE',
                'Tomales','Baja','Virginia','Monterey','S. Africa','Spain']
    values = [300,200,100,
               100,100,100,100,100,100,
               92, 90, 84, 75, 82, 80]
    colors = ['rgb(33, 75, 99)', 'rgb(79, 129, 102)', 'rgb(129, 180, 179)', 
              'rgb(33, 75, 99)','rgb(33, 75, 99)','rgb(33, 75, 99)','rgb(79, 129, 102)','rgb(79, 129, 102)','rgb(129, 180, 179)',
              'rgb(33, 75, 99)','rgb(33, 75, 99)','rgb(33, 75, 99)','rgb(79, 129, 102)','rgb(79, 129, 102)','rgb(129, 180, 179)'
              ]
    color_map = {'BC':'rgb(33, 75, 99)',
                 'Kelp':'rgb(79, 129, 102)',
                 'OAE':'rgb(129, 180, 179)',
                 'Tomales':'rgb(33, 75, 99)',
                 'Baja':'rgb(33, 75, 99)',
                 'Virginia':'rgb(33, 75, 99)',
                 'Monterey':'rgb(79, 129, 102)',
                 'S. Africa':'rgb(79, 129, 102)',
                 'Spain':'rgb(129, 180, 179)',
                 '92': 'white',
                 '84': 'white',
                 '90': 'white',
                 '75': 'white',
                 '82': 'white',
                 '80': 'white'}
    
    tree = px.treemap(
        names=names,
        parents=parents,
        values=values,
        color=names,
        color_discrete_map=color_map,
        #title='Portfolio Ocean IQ',
        branchvalues='total',
        width=450, height=400)
    
    
    tree.update_layout(
        title={
            'text': "Portfolio Ocean IQ",
            'y':0.95,
            'x':0.01,
            'xanchor': 'left',
            'yanchor': 'top',
            'font':{'family':"Helvetica", 'size':34}
            },
        )
    
    st.plotly_chart(tree, use_container_width=True)
    
with col2:

    donut = px.pie(projects, 
                   names='type', 
                   values='projects',
                   category_orders= {'type':['Blue Carbon','Kelp Restoration','OAE']},
                   hole=0.5,
                   color='type',
                   color_discrete_map={'Blue Carbon':'rgb(33, 75, 99)',
                                       'Kelp Restoration':'rgb(79, 129, 102)',
                                       'OAE':'rgb(129, 180, 179)'},
                   width=500, height=350)
    
    donut.update_traces(textinfo='none', 
                        marker=dict(line=dict(color='#FFFFFF', width=5)))
    
    donut.update_layout(
        title={
            'text': "Project Breakdown",
            'y':0.95,
            'x':0.99,
            'xanchor': 'right',
            'yanchor': 'top',
            'font':{'family':"Helvetica", 'size':34}
            },
        legend=dict(
            yanchor="middle",
            y=0.5,
            xanchor="left",
            x=0.95,
            itemwidth= 80,
            itemsizing='constant',
            bgcolor = 'rgba(0,0,0,0)',
            font=dict(
                family="Helvetica",
                size=22,
                color="black")),
        margin=dict(r=10,b=5))
    
    st.plotly_chart(donut, use_container_width=True)

with col3:
    add_vertical_space(18)
    report_button = st.button(":page_facing_up:", 
                              type='secondary', 
                              use_container_width=False,
                              help='Build a summary report for your stakeholders')
    if report_button:
        switch_page("Reporting")   

st.divider()

## Project Map
m = leafmap.Map(zoom=2)
# m.add_planet_by_month(year=slider.year, month=slider.month)
pcolors = {
    'Blue Carbon': 'darkblue',
    'Kelp Restoration': 'green',
    'OAE': 'lightblue'
    }

for p in range(0, len(projects)):
    P = projects.iloc[p]
    c = pcolors[P.type]
    popup_text = P.project_name + ' | Type: ' + P.type
    m.add_marker(P.location,  
                 tooltip=popup_text,
                 #popup=popup_text,
                 icon=Icon(color=c, icon='')
                  )

#m.to_streamlit(height=500)


# Change Page To Different Projects
click = st_folium(m, 
                  height=500, 
                  returned_objects=["last_object_clicked_tooltip"], 
                  use_container_width=True)

if click["last_object_clicked_tooltip"] == None:
    st.write('')
else:
    if 'Virginia' in click["last_object_clicked_tooltip"]:
        switch_page('Virginia Seagrass')
    elif 'Tomales' in click["last_object_clicked_tooltip"]:
        switch_page('Other Projects')
    elif 'Monterey' in click["last_object_clicked_tooltip"]:
        switch_page('Monterey Kelp')
    elif 'Spain' in click["last_object_clicked_tooltip"]:
        switch_page('Other Projects')
    elif 'South Africa' in click["last_object_clicked_tooltip"]:
        switch_page('Other Projects')
    elif 'Baja' in click["last_object_clicked_tooltip"]:
        switch_page('Other Projects')
    else:
        st.write('')
        
    