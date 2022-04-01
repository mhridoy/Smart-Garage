import streamlit as st
import hydralit_components as hc

from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import requests 
import itertools
# Page Config
st.set_page_config(layout="wide")


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

## Animation 
#Function of Lottie URL 

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_car = "https://assets3.lottiefiles.com/packages/lf20_cyn8dgwy.json"
lottie_car =load_lottieurl(lottie_url_car)
st_lottie(lottie_car, height=100)
st.markdown("<h3 style='text-align: center; font-family:  cursive, sans-serif; color: #B3E1E2;'>SMART GARAGE</h3>", unsafe_allow_html=True)
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
######### HOME PAGE ############################
def paginator(label, items, items_per_page=10, on_sidebar=True):
    
    # Figure out where to display the paginator
    if on_sidebar:
        location = ""
    else:
        location = ""

    # Display a pagination selectbox in the specified location.
    items = list(items)
    n_pages = len(items)
    n_pages = (len(items) - 1) // items_per_page + 1
    page_format_func = lambda i: "Page %s" % i
    #page_number = location.selectbox(label, range(n_pages), format_func=page_format_func)

    # Iterate over the items in the page to let the user display them.
    min_index = 0 * items_per_page
    max_index = min_index + items_per_page
    return itertools.islice(enumerate(items), min_index, max_index)
####################
if(menu_id=="Home"):
    sunset_imgs = [
    'https://unsplash.com/photos/-IMlv9Jlb24/download?force=true',
    'https://unsplash.com/photos/ESEnXckWlLY/download?force=true',
    'https://unsplash.com/photos/mOcdke2ZQoE/download?force=true',
    'https://unsplash.com/photos/GPPAjJicemU/download?force=true',
    'https://unsplash.com/photos/JFeOy62yjXk/download?force=true',
    'https://unsplash.com/photos/kEgJVDkQkbU/download?force=true',
    'https://unsplash.com/photos/i9Q9bc-WgfE/download?force=true',
    'https://unsplash.com/photos/tIL1v1jSoaY/download?force=true',
    'https://unsplash.com/photos/-G3rw6Y02D0/download?force=true',
    'https://unsplash.com/photos/xP_AGmeEa6s/download?force=true',
    'https://unsplash.com/photos/4iTVoGYY7bM/download?force=true',
    'https://unsplash.com/photos/mBQIfKlvowM/download?force=true',
    'https://unsplash.com/photos/A-11N8ItHZo/download?force=true',
    'https://unsplash.com/photos/kOqBCFsGTs8/download?force=true',
    'https://unsplash.com/photos/8DMuvdp-vso/download?force=true'
]
    image_iterator = paginator( "",sunset_imgs)
    indices_on_page, images_on_page = map(list, zip(*image_iterator))
    st.image(images_on_page, width=100, caption=indices_on_page)