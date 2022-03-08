from logging import PlaceHolder
import streamlit as st

import numpy as np
import pandas as pd
import time
CSS = """
h2 {
    color: #34ebc6;
    font-size: 20;
    text-shadow: 2px 2px 4px #000000;
    text-align: center;
}

h3 {
    text-shadow: 2px 2px 4px #000000;
    font-size: 16;
}

h4 {
    text-shadow: 2px 2px 4px #000000;
    font-size: 12;
}

body{
    font-size: 20;
}
"""

# Page setup
st.set_page_config(layout = "wide")
st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

# Display image and header
col1, col2, col3, col4, col5 = st.columns(5)
with col3:
    st.image('EFPO.png')
col1, col2, col3 = st.columns([0.5,2,0.5])
with col2:
    st.header('Welcome to the Emotional Faces of Public Opinion!',anchor='h2')

# Page selectors
page = st.sidebar.selectbox('Select page',
  ['About','Find Other Perspectives'])

# About page
if page == 'About':
    # Display the About content here
    st.subheader('About this app')
    st.write("Currently, people are stuck in echo chambers on social media,\
            meaning that they are not always seeing all the sides of a story.\
            We developed a tool that allows people to break out of these echo chambers,\
            giving them the opportunity to explore and understand different public opinions \
            to what they see in day-to-day life. In doing so, we hope this will reduce polarisation due to exposure theory.")
    # guide = st.expander(label='Need help to run the app?  Click here!' )
    # with guide:
    #     st.subheader('How to use this app')
    #     st.write('1️⃣ Naviagate to the Find Other Perspectives page on the side bar')
    #     # Insert image here
    #     # st.image('step1.png')
    #     st.write('2️⃣ Expland the search terms container')
    #     # Insert image here
    #     st.write('3️⃣ Enter your search term, dates, and the number of tweets you would like to scrape (minimum value of 500 tweets).')
    #     # Insert image here
    #     st.write('4️⃣ Click on the Submit Search button.')
    #     # Insert image here
    #     st.write("5️⃣ RECOMMENDED BUT OPTIONAL: Remain calm while the models run and the data loads (it shouldn't take too long). 😌")


# Find other perspectives page
else:
    # Display the Search Twitter content here
    st.subheader('Find other perspectives',anchor='h3')
    tweet_search = st.expander(label='Click on me to expand search terms!')
    with tweet_search:
        st.write('Please enter the Twitter search term, followed by the search dates and the number of tweets you would like to scrape:')
        col1, col2, col3, col4 = st.columns([3,1,1,1.25])
        with col1:
            title = st.text_input('Enter search term here:')
            # Connect to api

        with col2:
            start_date=st.date_input('Enter start date:')
            # Connect to api
        with col3:
            end_date=st.date_input('Enter end date:')
            # Connect to api
        with col4:
            num_tweets= st.number_input('Enter number of tweets',min_value=500, step=100)
            # Connect to api
        if st.button('Submit Search'):
            col1, col2, col3, = st.columns([1,2,1])
            with col2:
                result = st.image('keep-calm-we-are-loading-data.png',caption='Data is laoding...')
                #Once data has loaded
                # result.empty()

            # Graph display
            data_display = st.container()
            with data_display:
                st.subheader('Search Results',anchor='h3')
                col1, col2 = st.columns([3,2])
                with col1:
                    st.write('TensorFlow embedding will go here')
                with col2:
                    st.subheader('Data Frame',anchor='h4')
                    df = pd.read_csv('raw_data/euphoria.csv')
                    st.dataframe(df)
                    time.sleep(3)
                    result.empty()

    # Download file
    file_download=st.container()
    with file_download:
        col1, col2, col3, col4, col5 = st.columns([1.5,1.5,3.5,1.5,1.5])
        with col3:
            st.write(' Click on the button 👇 to save your search')
        col1, col2, col3, col4, col5 = st. columns(5)
        with col3:
            download_file = st.download_button(label='Download File', data='', file_name=f'{title} Results - {start_date} to {end_date}.pdf', mime=None, key=None, help=None, on_click=None, disabled=False)
