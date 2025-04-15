import streamlit as st
from utils import search_app

st.set_page_config(layout="wide")
st.title('Searching for Apps')
                   
# Input box for search term
term = st.text_input('Choose the Apps for Competitor Analysis', value=st.session_state.get('last_query', ''))

# Add a Search button
if st.button('Search'):
    if term.strip():  # check for non-empty search
        with st.spinner(f'Getting {term} apps...'):
            data = search_app(term)
            st.session_state.data = data
            st.session_state.last_query = term
    else:
        st.warning("Please enter a search term.")

# Show results if already stored
if 'data' in st.session_state:
    data = st.session_state.data

    filtered_data = data[[
            'title', 'developer', 'genre',
            'price', 'free', 'currency', 'score', 'installs'
        ]]

    st.dataframe(filtered_data, hide_index=True) 

