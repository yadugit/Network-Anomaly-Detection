import streamlit as st


# Home Page
def home_page():
    st.image('bkg.png', use_column_width=True)
    st.title('Home')
    st.write('Welcome to the Network Anomaly Detection App!')

    # Embed video
    # Embed Loom video
    st.markdown("""
    ### 📹 Demo Video
    [Click here to watch the Loom video](https://www.loom.com/share/935407b16d2d437eb8102005406ace29?sid=8a8334b0-e987-475c-8a34-6d5d92455034)
    """)
