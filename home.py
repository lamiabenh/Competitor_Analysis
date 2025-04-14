import streamlit as st #Import the streamlit library

st.set_page_config(layout="wide")
st.title('Competitor Analysis') #Set title of the webpage
st.markdown ('## Overview') #Set markdown of the webpage


st.write('This is a rapid prototype of a Competitor Analysis application.  \n\
Based on a search query, the app provides an Analysis of mobile apps in the targeted market for competitive insights.')

col_1, col_2 = st.columns([1,1])

with col_1:
    st.markdown('## Key Features \n\
    - Search for Apps \n\
    - Listing results \n\
	- Filtering results \n\
    - Sorting results \n\
    - Data visualizations for Competitor analysis \n\
    - Conducting Sentiment Analysis on Applications\' reviews')

with col_2:
    st.markdown('## Improvements \n\
    - Enhance data visualizations \n\
    - Load more data \n\
    - Revise features based on feedback \n\
    ')
    