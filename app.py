import streamlit as st
import hydralit_components as hc

from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import requests 
import itertools
import streamlit.components.v1 as components

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
    ############### Search ##################

    ###################### END SEARCH ###############
    st.markdown("<h5 style='text-align: center; font-family:  cursive, sans-serif; color: #B3E1E2;'>Your Personal Assistant</h3>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center; font-family:  cursive, sans-serif; color: black;'>One-stop solution for your services. Order any service, anytime.</h3>", unsafe_allow_html=True)
        ############### Search ##################

    query = st.text_input("", "Search...")
    query_manual = "bike"
    print(len(query))
    button_clicked = st.button("Find")   
    ###################### END SEARCH ###############
    if(len(query)>9):
        url =f"https://unsplash.com/napi/search?query={query} Wash&per_page=10&xp="
        r = requests.get(url)
    else:
        url =f"https://unsplash.com/napi/search?query={query_manual}&per_page=10&xp="
        r = requests.get(url)
    data = r.json()
    url_array=[]
    name_array=[]

    for item in data['photos']['results']:
        name = item['user']['name']
        name_array.append(name)
        url = item['urls']['full']
        url_array.append(url)
    imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")
    selectedImageUrl = imageCarouselComponent(imageUrls=url_array, height=200)

    if selectedImageUrl is not None:
        st.image(selectedImageUrl)
#     sunset_imgs = [
#     'https://unsplash.com/photos/-IMlv9Jlb24/download?force=true',
#     'https://unsplash.com/photos/ESEnXckWlLY/download?force=true',
#     'https://unsplash.com/photos/mOcdke2ZQoE/download?force=true',
#     'https://unsplash.com/photos/GPPAjJicemU/download?force=true',
#     'https://unsplash.com/photos/JFeOy62yjXk/download?force=true',
#     'https://unsplash.com/photos/kEgJVDkQkbU/download?force=true',
#     'https://unsplash.com/photos/i9Q9bc-WgfE/download?force=true',
#     'https://unsplash.com/photos/tIL1v1jSoaY/download?force=true',
#     'https://unsplash.com/photos/-G3rw6Y02D0/download?force=true',
#     'https://unsplash.com/photos/xP_AGmeEa6s/download?force=true',
#     'https://unsplash.com/photos/4iTVoGYY7bM/download?force=true',
#     'https://unsplash.com/photos/mBQIfKlvowM/download?force=true',
#     'https://unsplash.com/photos/A-11N8ItHZo/download?force=true',
#     'https://unsplash.com/photos/kOqBCFsGTs8/download?force=true',
#     'https://unsplash.com/photos/8DMuvdp-vso/download?force=true'
# ]
    # image_iterator = paginator( "",url_array)
    # indices_on_page, images_on_page = map(list, zip(*image_iterator))
    # st.image(images_on_page, width=100, caption=indices_on_page)

    st.markdown("<h5 style='text-align: center; font-family:  cursive, sans-serif; color: #B3E1E2;'>-----WHY CHOOSE US------</h5>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; font-family:  cursive, sans-serif; color: black;'>Because we care about your safety..</h3>", unsafe_allow_html=True)


    ### Safety Signs #########
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        
        st.image("https://cdn-marketplacexyz.s3.ap-south-1.amazonaws.com/sheba_xyz/images/png/usp_mask.png")
        st.subheader("Ensuring Mask")
    with col2:
        st.image("https://cdn-marketplacexyz.s3.ap-south-1.amazonaws.com/sheba_xyz/images/png/usp_24_7.png")
        st.subheader("24/7 Support")
    with col3:
        st.image("https://cdn-marketplacexyz.s3.ap-south-1.amazonaws.com/sheba_xyz/images/png/usp_sanitized.png")
        st.subheader("Sanitising Hands & Equipment")

    with col4:
        st.image("https://cdn-marketplacexyz.s3.ap-south-1.amazonaws.com/sheba_xyz/images/png/usp_gloves.png")
        st.subheader("Ensuring Gloves")
    #########

    ###### How It Works ##########
    st.markdown("<h5 style='text-align: center; font-family:  cursive, sans-serif; color: #B3E1E2;'>-----HOW IT WORKS------</h5>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; font-family:  cursive, sans-serif; color: black;'>Easiest way to get a service</h3>", unsafe_allow_html=True)

    #### Step by step ###

    col1, col2 = st.columns(2)

    with col1:
        st.video("https://www.youtube.com/watch?v=kdRSObObCy4")
    with col2:
        working_array = {"Select the Service","Pick your schedule","Place Your Order & Relax"}

    ############
        st.markdown(
                            " ".join([
                                "<div class='r-text-recipe'>",
                                # "<div class='food-title'>",
                                # #f"<img src='{food_image}' />",
                                # #f"<h2 class='font-title text-bold'>{title}</h2>",
                                # "</div>",
                                '<div class="divider"><div class="divider-mask"></div></div>',
                                #"<h3 class='ingredients font-body text-bold'>Ingredients</h3>",
                                "<ul class='ingredients-list font-body'>",
                                " ".join([f'<li><h4 >{item}</h4></li>' for item in working_array]),
                                "</ul>",
                                # "<h3 class='directions font-body text-bold'>Directions</h3>",
                                # "<ol class='ingredients-list font-body'>",
                                # " ".join([f'<li>{item}</li>' for item in directions]),
                                # "</ol>",
                                "</div>"
                            ]),
                            unsafe_allow_html=True
                        )

    st.markdown("<h5 style='text-align: center; font-family:  cursive, sans-serif; color: #B3E1E2;'>-----CONTACT US------</h5>", unsafe_allow_html=True)
    st.text("16516 |info@smartgarage.com Corporate Address | House # 57, Road # 25, Block - A,Banani, Dhaka 1212")

elif(menu_id=="Login"):
    names = ['Sadia','Tonmoy']
    usernames = ['sadia','tonmoy']
    passwords = ['123','456']
    #hashed_passwords = stauth.Hasher(passwords).generate()
  #  authenticator = stauth.Authenticate(names,usernames,hashed_passwords,
    #'some_cookie_name','some_signature_key',cookie_expiry_days=30)
   # name, authentication_status, username = authenticator.login('Login','main')
    flag = True
    if(flag):
        st.markdown("<h2 style='text-align: center; font-family:  cursive, sans-serif; color: #B3E1E2;'>-----LOGIN------</h2>", unsafe_allow_html=True)
        my_form = st.form(key='form-1')

        username =my_form.text_input("UserName")
        passwords = my_form.text_input("Password")
        submit=my_form.form_submit_button('Submit')
    if(submit=='Submit'):
            flag= False
            st.balloons()
            st.write("Welcome")

elif (menu_id=="Registration"):
    st.markdown("<h2 style='text-align: center; font-family:  cursive, sans-serif; color: #B3E1E2;'>-----Registration------</h2>", unsafe_allow_html=True)
    # creating a form
    my_form=st.form(key='form-1')
    # creating input fields
    fname=my_form.text_input('First Name:')
    lname=my_form.text_input('Last Name:')
    email=my_form.text_input('Email:')
    # creating radio button 
    gender=my_form.radio('Gender',('Male','Female'))
    # creating slider 
    age=my_form.slider('Age:',1,120)
    # creating date picker
    bday=my_form.date_input('Enter Birthdate:')
    # creating a text area
    address=my_form.text_area('Enter Address:')
    # creating a submit button
    submit=my_form.form_submit_button('Submit')
    # the following gets updated after clicking on submit, printing the details of the fields that are submitted in the form
    if(submit=='Submit'):
        st.write('Name is '+fname+' '+lname)
        st.write('Email is '+email)
        st.write('Gender is '+gender)
        st.write('Age is '+str(age))
        st.write('Birthday is '+str(bday))
        st.write('Address is '+address)