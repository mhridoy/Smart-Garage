import streamlit as st
import hydralit_components as hc
# Page Config
st.set_page_config(layout="wide")


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
# specify the primary menu definition
menu_data = [
        {'id': "Copy", 'icon':'🚗', 'label':"Our Services"},
       # {'id':'Copy','icon':"🐙",'label':"Copy"},
        {'icon': "far fa-chart-bar", 'label':"Available Solts"},#no tooltip message
        {'icon': "far fa-address-book", 'label':"Booking"},
        {'id':' Crazy return value 💀','icon': "💼", 'label':"Career"},
        {'icon': "🔒", 'label':"Login"},
        {'icon': "📝", 'label':"Registration",'ttip':"I'm the Dashboard tooltip!"}, #can add a tooltip message
        {'icon': "📟", 'label':"About Us"},
]
# we can override any part of the primary colors of the menu
#over_theme = {'txc_inactive': '#FFFFFF','menu_background':'red','txc_active':'yellow','option_active':'blue'}
over_theme = {'txc_inactive': '#FFFFFF'}
menu_id = hc.nav_bar(menu_definition=menu_data,home_name='Home',override_theme=over_theme)

    
#get the id of the menu item clicked
#st.info(f"{menu_id=}")
if(menu_id=="Home"):
    st.title("GOT Home")