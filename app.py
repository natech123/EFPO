import streamlit as st

import numpy as np
import pandas as pd

st.set_page_config(layout = "wide")


st.header('Welcome to the Emotional Faces of Public Opinion')


page = st.sidebar.selectbox('Select page',
  ['About','Find Other Perspectives'])
if page == 'About':
    # Display the About content here
    st.subheader('About this app')
    st.write("Currently, people are stuck in echo chambers on social media, meaning that they are not always seeing all the sides of a story.  We developed a tool that allows people to break out of these echo chambers, giving them the opportunity to explore and understand different public opinions to what they see in day-to-day life. In doing so, we hope this will reduce polarisation due to exposure theory.")
else:
    # Display the Search Twitter content here
    st.subheader('Find other perspectives')
    my_expander = st.expander(label='Click on me to expand search terms!')
    with my_expander:
        st.write('Please enter the Twitter search term, followed by the search dates')
        title = st.text_input('Enter search term here:')
        start_date=st.date_input('Enter start date:')
        end_date=st.date_input('Enter end date:')
        st.button('Submit search')
