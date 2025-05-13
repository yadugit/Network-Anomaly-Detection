import streamlit as st


# Home Page
def home_page():
    st.image('bkg.png', use_column_width=True)
    st.title('Home')
    st.write('Welcome to the Network Anomaly Detection App!')

    # Embed video
    # Embed Loom video
    st.markdown("""
    <div style="position: relative; padding-bottom: 64.98194945848375%; height: 0;">
        <iframe src="https://www.loom.com/share/935407b16d2d437eb8102005406ace29?sid=8a8334b0-e987-475c-8a34-6d5d92455034" 
                frameborder="0" 
                webkitallowfullscreen 
                mozallowfullscreen 
                allowfullscreen 
                style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;">
        </iframe>
    </div>
    """, unsafe_allow_html=True)