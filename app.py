import streamlit as st
import hydralit_components as hc
import scipy
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import requests
import itertools
import streamlit.components.v1 as components
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.figure_factory as ff

# Page Config
st.set_page_config(
    page_title="Smart Garage",
    page_icon="🚗",
    layout="wide",
)


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Animation
# Function of Lottie URL


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_url_car = "https://assets3.lottiefiles.com/packages/lf20_cyn8dgwy.json"
lottie_car = load_lottieurl(lottie_url_car)
# specify the primary menu definition
menu_data = [
    {'icon': "🚗", 'label': "Our Services"},
    # {'id':'Copy','icon':"🐙",'label':"Copy"},
    {'icon': "far fa-chart-bar", 'label': "Available Slots"},  # no tooltip message
    {'icon': "far fa-address-book", 'label': "Booking"},
    {'id': ' Crazy return value 💀', 'icon': "💼", 'label': "Career"},
    {'icon': "🔒", 'label': "Login"},
    # can add a tooltip message
    {'icon': "📝", 'label': "Registration", 'ttip': "I'm the Dashboard tooltip!"},
    {'icon': "📟", 'label': "About Us"},
]
# we can override any part of the primary colors of the menu
# over_theme = {'txc_inactive': '#FFFFFF','menu_background':'red','txc_active':'yellow','option_active':'blue'}
over_theme = {'txc_inactive': '#FFFFFF'}
menu_id = hc.nav_bar(menu_definition=menu_data,
                     home_name='Home', override_theme=over_theme)
# menu_id = hc.nav_bar(
#     menu_definition=menu_data,
#     override_theme=over_theme,
#     home_name='Home',
#     login_name='Logout',
#     hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
#     sticky_nav=True, #at the top or not
#     sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
# )


# get the id of the menu item clicked
# st.info(f"{menu_id=}")
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
    def page_format_func(i): return "Page %s" % i
    #page_number = location.selectbox(label, range(n_pages), format_func=page_format_func)

    # Iterate over the items in the page to let the user display them.
    min_index = 0 * items_per_page
    max_index = min_index + items_per_page
    return itertools.islice(enumerate(items), min_index, max_index)


####################
if(menu_id=="Available Slots"):
    #st.write("Gotcha")
    st.markdown("<h3 style='text-align: center; font-family:  Consolas, sans-serif; color: #F1330A;'>Available Slots</h3>", unsafe_allow_html=True)
    df = pd.read_csv("slots.csv")
    col1, col2 = st.columns(2)
    with col1 :

        st.write(df)
    with col2 : 
        x1 = np.random.randn(200) - 2
        x2 = np.random.randn(200)
        x3 = np.random.randn(200) + 2

# Group data together
        hist_data = [x1, x2, x3]

        group_labels = ['Type 1', 'Type 2', 'Type 3']

# Create distplot with custom bin_size
        fig = ff.create_distplot(
         hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
        st.plotly_chart(fig, use_container_width=True)
        #st.write(fig)
elif(menu_id == "Home"):
    ############### Search ##################

    ###################### END SEARCH ###############

    st.markdown("<h3 style='text-align: center; font-family:  Consolas, sans-serif; color: #F1330A;'>SMART GARAGE</h3>", unsafe_allow_html=True)
    st_lottie(lottie_car, height=150)
    st.markdown("<h5 style='text-align: center; font-family:  Consolas	, sans-serif; color: #ff4b4b;'>Your Personal Assistant</h5>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center; font-family:  Consolas	, sans-serif; color: black;'>One-stop solution for your services. Order any service, anytime.</h6>", unsafe_allow_html=True)
    ############### Search ##################

    query = st.text_input("", "Search...")
    query_manual = "bike"
    print(len(query))
    button_clicked = st.button("Find")
    ###################### END SEARCH ###############
    if(len(query) > 9):
        url = f"https://unsplash.com/napi/search?query={query} Wash&per_page=10&xp="
        r = requests.get(url)
    else:
        url = f"https://unsplash.com/napi/search?query={query_manual}&per_page=10&xp="
        r = requests.get(url)
    data = r.json()
    url_array = []
    name_array = []

    for item in data['photos']['results']:
        name = item['user']['name']
        name_array.append(name)
        url = item['urls']['full']
        url_array.append(url)
    imageCarouselComponent = components.declare_component(
        "image-carousel-component", path="frontend/public")
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

    st.markdown("<h3 style='text-align: center; font-family:  Consolas, sans-serif; color: #ff4b4b;'>WHY CHOOSE US</h3>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; font-family:  cursive, sans-serif; color: black;'>Because we care about your safety..</h4>", unsafe_allow_html=True)

    ### Safety Signs #########
    from streamlit_player import st_player
    st_player("https://www.youtube.com/watch?v=Nvedr1AeQt8")
    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.image(
            "https://cdn-marketplacexyz.s3.ap-south-1.amazonaws.com/sheba_xyz/images/png/usp_mask.png", width=50)
        st.subheader("Ensuring Mask")
        st.write("In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before the final copy is available.")
    with col2:
        st.image(
            "https://cdn-marketplacexyz.s3.ap-south-1.amazonaws.com/sheba_xyz/images/png/usp_24_7.png", width=50)
        st.subheader("24/7 Support")
        st.write("In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before the final copy is available.")

    with col3:
        st.image(
            "https://cdn-marketplacexyz.s3.ap-south-1.amazonaws.com/sheba_xyz/images/png/usp_sanitized.png", width=50)
        st.subheader("Sanitising Hands & Equipment")
        st.write("In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before the final copy is available.")
    with col4:
        st.image(
            "https://cdn-marketplacexyz.s3.ap-south-1.amazonaws.com/sheba_xyz/images/png/usp_gloves.png", width=50)
        st.subheader("Ensuring Gloves")
        st.write("In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before the final copy is available.")
    #########

    ###### How It Works ##########
    st.markdown("<h3 style='text-align: center; font-family:  Consolas, sans-serif; color: #ff4b4b;'>HOW IT WORKS</h3>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; font-family:  cursive, sans-serif; color: black;'>Easiest way to get a service</h4>", unsafe_allow_html=True)

    #### Step by step ###

    # st.video("https://www.youtube.com/watch?v=kdRSObObCy4")
    col1, col2 = st.columns(2)
    with col1:
        st.image(
            "https://s3.ap-south-1.amazonaws.com/cdn-shebaxyz/images/v4_uploads/categories/223/thumb_480x320.jpg")
    with col2:
        st.image(
            "https://cdn-shebaxyz.s3.ap-south-1.amazonaws.com/images/bulk/categories/222/web_thumb_480x320.jpg")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(
            "https://proofmart.com/wp-content/uploads/2021/06/542-10.png", width=100)
        st.subheader("Select the Service")
        st.write("Pick the service you are looking for- from the website or the app.")
    with col2:
        st.image(
            "https://proofmart.com/wp-content/uploads/2021/06/542-11.png", width=100)
        st.subheader("Pick your schedule")
        st.write(
            "Pick your convenient date and time to avail the service. Pick the service provider based on their rating.")
        working_array = {"Select the Service",
                         "Pick your schedule", "Place Your Order & Relax"}
    with col3:
        st.image(
            "https://proofmart.com/wp-content/uploads/2021/06/542-22.png", width=100)
        st.subheader("Place Your Order & Relax")
        st.write("Review and place the order. Now just sit back and relax. We’ll assign the expert service provider’s schedule for you.")

    # st.markdown("<h5 style='text-align: center; font-family:  cursive, sans-serif; color: #B3E1E2;'>-----CONTACT US------</h5>", unsafe_allow_html=True)
    # st.text("16516 |info@smartgarage.com Corporate Address | House # 57, Road # 25, Block - A,Banani, Dhaka 1212")
    user_ratings = """
    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- Font Awesome Icon Library -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <style>
    * {
    box-sizing: border-box;
    }

    body {
    font-family: Arial;
    margin: 0 auto; /* Center website */
    max-width: 800px; /* Max width */
    padding: 20px;
    }

    .heading {
    font-size: 25px;
    margin-right: 25px;
    }

    .fa {
    font-size: 25px;
    }

    .checked {
    color: orange;
    }

    /* Three column layout */
    .side {
    float: left;
    width: 15%;
    margin-top:10px;
    }

    .middle {
    margin-top:10px;
    float: left;
    width: 70%;
    }

    /* Place text to the right */
    .right {
    text-align: right;
    }

    /* Clear floats after the columns */
    .row:after {
    content: "";
    display: table;
    clear: both;
    }

    /* The bar container */
    .bar-container {
    width: 100%;
    background-color: #f1f1f1;
    text-align: center;
    color: white;
    }

    /* Individual bars */
    .bar-5 {width: 60%; height: 18px; background-color: #04AA6D;}
    .bar-4 {width: 30%; height: 18px; background-color: #2196F3;}
    .bar-3 {width: 10%; height: 18px; background-color: #00bcd4;}
    .bar-2 {width: 4%; height: 18px; background-color: #ff9800;}
    .bar-1 {width: 15%; height: 18px; background-color: #f44336;}

    /* Responsive layout - make the columns stack on top of each other instead of next to each other */
    @media (max-width: 400px) {
    .side, .middle {
        width: 100%;
    }
    .right {
        display: none;
    }
    }
    </style>
    </head>
    <body>

    <span class="heading">User Rating</span>
    <span class="fa fa-star checked"></span>
    <span class="fa fa-star checked"></span>
    <span class="fa fa-star checked"></span>
    <span class="fa fa-star checked"></span>
    <span class="fa fa-star"></span>
    <p>4.1 average based on 254 reviews.</p>
    <hr style="border:3px solid #f1f1f1">

    <div class="row">
    <div class="side">
        <div>5 star</div>
    </div>
    <div class="middle">
        <div class="bar-container">
        <div class="bar-5"></div>
        </div>
    </div>
    <div class="side right">
        <div>150</div>
    </div>
    <div class="side">
        <div>4 star</div>
    </div>
    <div class="middle">
        <div class="bar-container">
        <div class="bar-4"></div>
        </div>
    </div>
    <div class="side right">
        <div>63</div>
    </div>
    <div class="side">
        <div>3 star</div>
    </div>
    <div class="middle">
        <div class="bar-container">
        <div class="bar-3"></div>
        </div>
    </div>
    <div class="side right">
        <div>15</div>
    </div>
    <div class="side">
        <div>2 star</div>
    </div>
    <div class="middle">
        <div class="bar-container">
        <div class="bar-2"></div>
        </div>
    </div>
    <div class="side right">
        <div>6</div>
    </div>
    <div class="side">
        <div>1 star</div>
    </div>
    <div class="middle">
        <div class="bar-container">
        <div class="bar-1"></div>
        </div>
    </div>
    <div class="side right">
        <div>20</div>
    </div>
    </div>

    </body>
    </html>

        """

    components.html(user_ratings, height=400,
                    )

    st.header(":mailbox: Get In Touch With US!")

    contact_form = """
    <form action="https://formsubmit.co/hridoyfaa@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css("style.css")
elif(menu_id == "Our Services"):
    services1 = """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <div class="card" style="width: 18rem;">
  <img class="card-img-top" src="https://s3.ap-south-1.amazonaws.com/cdn-shebaxyz/images/categories_images/thumbs/1617704874_carwashpolish.jpg" alt="Card image cap">
  <div class="card-body">
    <p class="card-text">Car Wash & Polish</p>
    <p> We have professional service partners with verified resources. Our resources are experienced because we try to provide punctual service. We are making a one-stop service solution because your flexibility is our main priority.
Car Cleaning (Wash & Deep Cleaning)
Car Polishing
Car Ceramic Coating
Car Detailing (Cleaning & Polishing)

Pricing & Terms   
Service Charge: The mentioned pricing is estimated service charges which might vary slightly depending on: Vehicle Type, Model, and Service Availability.

Home Service Policy: The home service charge of maximum BDT 300 is applicable if the customer decides not to take the service after the service provider visited the location. However, if the customer agrees to avail this service on scheduled time then the home service charge is not applicable.

Liability: Sheba.xyz will not be liable for any pre-existing issues/potential risks reported by the service provider but not handled due to customer refusal to car wash/polish service the same.

Payment: You can pay through online or COD. After payment please make sure, you have received the SMS containing the money receipt.
</p>
  </div>
</div>
    """
    # components.html(services, height=600,)
    st.markdown("<h2 style='text-align: center; font-family:  Inter, ui-sans-serif, system-ui, Helvetica, Arial,Inter,ui-sans-serif,system-ui,Helvetica,Arial,sans-serif ; color: rgb(255, 75, 75);'>Services</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        #components.html(services1, height=600,)
        st.markdown("<h4 style='text-align: center; font-family:  Inter, ui-sans-serif, system-ui, Helvetica, Arial,Inter,ui-sans-serif,system-ui,Helvetica,Arial,sans-serif ; color: rgb(92, 228, 136);'>1. Car Wash & Polish</h4>", unsafe_allow_html=True)

        st.image("https://s3.ap-south-1.amazonaws.com/cdn-shebaxyz/images/categories_images/thumbs/1617704874_carwashpolish.jpg")
        with st.expander("See Details"):
            st.write("""
            We have professional service partners with verified resources. Our resources are experienced because we try to provide punctual service. We are making a one-stop service solution because your flexibility is our main priority.\n
        Car Cleaning (Wash & Deep Cleaning)
        Car Polishing
        Car Ceramic Coating
        Car Detailing (Cleaning & Polishing)

🟠 Pricing & Terms   
Service Charge: The mentioned pricing is estimated service charges which might vary slightly depending on: Vehicle Type, Model, and Service Availability.

🟠 Home Service Policy: The home service charge of maximum BDT 300 is applicable if the customer decides not to take the service after the service provider visited the location. However, if the customer agrees to avail this service on scheduled time then the home service charge is not applicable.

🟠 Liability: Smart Garage will not be liable for any pre-existing issues/potential risks reported by the service provider but not handled due to customer refusal to car wash/polish service the same.

🟠 Payment: You can pay through online or COD. After payment please make sure, you have received the SMS containing the money receipt.
            """)
        #st.write("Overview of Car Washing & Polishing Service")
        
    #st.image("")
    with col2:
        #components.html(services1, height=600,)
        st.markdown("<h4 style='text-align: center; font-family:  Inter, ui-sans-serif, system-ui, Helvetica, Arial,Inter,ui-sans-serif,system-ui,Helvetica,Arial,sans-serif ; color: rgb(92, 228, 136);'>2. Car Repair & Services</h4>", unsafe_allow_html=True)

        st.image("https://s3.ap-south-1.amazonaws.com/cdn-shebaxyz/images/categories_images/thumbs/1617278510_carrepairservices.jpg")
        with st.expander("See Details"):
            st.write("""
            We have professional service partners with verified resources. Our resources are experienced because we try to provide punctual service. We are making a one-stop service solution because your flexibility is our main priority.\n
        Car Cleaning (Wash & Deep Cleaning)
        Car Polishing
        Car Ceramic Coating
        Car Detailing (Cleaning & Polishing)

🟠 Pricing & Terms   
Service Charge: The mentioned pricing is estimated service charges which might vary slightly depending on: Vehicle Type, Model, and Service Availability.

🟠 Home Service Policy: The home service charge of maximum BDT 300 is applicable if the customer decides not to take the service after the service provider visited the location. However, if the customer agrees to avail this service on scheduled time then the home service charge is not applicable.

🟠 Liability: Smart Garage will not be liable for any pre-existing issues/potential risks reported by the service provider but not handled due to customer refusal to car wash/polish service the same.

🟠 Payment: You can pay through online or COD. After payment please make sure, you have received the SMS containing the money receipt.
            """)
        #st.write("Overview of Car Washing & Polishing Service")

    with col3:
        #components.html(services1, height=600,)
        st.markdown("<h4 style='text-align: center; font-family:   ui-sans-serif, system-ui, Helvetica, Arial,Inter,ui-sans-serif,system-ui,Helvetica,Arial,sans-serif ; color: rgb(92, 228, 136);'>3. Car LPG Conversion</h4>", unsafe_allow_html=True)

        st.image("https://s3.ap-south-1.amazonaws.com/cdn-shebaxyz/images/categories_images/thumbs/1617710975_carlpgconversion.jpg")
        with st.expander("See Details"):
            st.write("""
            We have professional service partners with verified resources. Our resources are experienced because we try to provide punctual service. We are making a one-stop service solution because your flexibility is our main priority.\n
        Car Cleaning (Wash & Deep Cleaning)
        Car Polishing
        Car Ceramic Coating
        Car Detailing (Cleaning & Polishing)

🟠 Pricing & Terms   
Service Charge: The mentioned pricing is estimated service charges which might vary slightly depending on: Vehicle Type, Model, and Service Availability.

🟠 Home Service Policy: The home service charge of maximum BDT 300 is applicable if the customer decides not to take the service after the service provider visited the location. However, if the customer agrees to avail this service on scheduled time then the home service charge is not applicable.

🟠 Liability: Smart Garage will not be liable for any pre-existing issues/potential risks reported by the service provider but not handled due to customer refusal to car wash/polish service the same.

🟠 Payment: You can pay through online or COD. After payment please make sure, you have received the SMS containing the money receipt.
            """)
        #st.write("Overview of Car Washing & Polishing Service")
            
    #st.image("")

    col1, col2, col3 = st.columns(3)
    with col1:
        #components.html(services1, height=600,)
        st.markdown("<h4 style='text-align: center; font-family:  Inter, ui-sans-serif, system-ui, Helvetica, Arial,Inter,ui-sans-serif,system-ui,Helvetica,Arial,sans-serif ; color: rgb(92, 228, 136);'>4. Bike Wash & Polish</h4>", unsafe_allow_html=True)

        st.image("https://s3.ap-south-1.amazonaws.com/cdn-shebaxyz/images/categories_images/thumbs/1643638011_hybridcarsolution.jpg")
        with st.expander("See Details"):
            st.write("""
            We have professional service partners with verified resources. Our resources are experienced because we try to provide punctual service. We are making a one-stop service solution because your flexibility is our main priority.\n
        Car Cleaning (Wash & Deep Cleaning)
        Car Polishing
        Car Ceramic Coating
        Car Detailing (Cleaning & Polishing)

🟠 Pricing & Terms   
Service Charge: The mentioned pricing is estimated service charges which might vary slightly depending on: Vehicle Type, Model, and Service Availability.

🟠 Home Service Policy: The home service charge of maximum BDT 300 is applicable if the customer decides not to take the service after the service provider visited the location. However, if the customer agrees to avail this service on scheduled time then the home service charge is not applicable.

🟠 Liability: Smart Garage will not be liable for any pre-existing issues/potential risks reported by the service provider but not handled due to customer refusal to car wash/polish service the same.

🟠 Payment: You can pay through online or COD. After payment please make sure, you have received the SMS containing the money receipt.
            """)
        #st.write("Overview of Car Washing & Polishing Service")
        
    #st.image("")
    with col2:
        #components.html(services1, height=600,)
        st.markdown("<h4 style='text-align: center; font-family:  Inter, ui-sans-serif, system-ui, Helvetica, Arial,Inter,ui-sans-serif,system-ui,Helvetica,Arial,sans-serif ; color: rgb(92, 228, 136);'>5. Bike Repair & Services</h4>", unsafe_allow_html=True)

        st.image("https://s3.ap-south-1.amazonaws.com/cdn-shebaxyz/images/categories_images/thumbs/1619589579_emergencycarservices.jpg")
        with st.expander("See Details"):
            st.write("""
            We have professional service partners with verified resources. Our resources are experienced because we try to provide punctual service. We are making a one-stop service solution because your flexibility is our main priority.\n
        Car Cleaning (Wash & Deep Cleaning)
        Car Polishing
        Car Ceramic Coating
        Car Detailing (Cleaning & Polishing)

🟠 Pricing & Terms   
Service Charge: The mentioned pricing is estimated service charges which might vary slightly depending on: Vehicle Type, Model, and Service Availability.

🟠 Home Service Policy: The home service charge of maximum BDT 300 is applicable if the customer decides not to take the service after the service provider visited the location. However, if the customer agrees to avail this service on scheduled time then the home service charge is not applicable.

🟠 Liability: Smart Garage will not be liable for any pre-existing issues/potential risks reported by the service provider but not handled due to customer refusal to car wash/polish service the same.

🟠 Payment: You can pay through online or COD. After payment please make sure, you have received the SMS containing the money receipt.
            """)
        #st.write("Overview of Car Washing & Polishing Service")

    with col3:
        #components.html(services1, height=600,)
        st.markdown("<h4 style='text-align: center; font-family:   ui-sans-serif, system-ui, Helvetica, Arial,Inter,ui-sans-serif,system-ui,Helvetica,Arial,sans-serif ; color: rgb(92, 228, 136);'>6. Bike Painting</h4>", unsafe_allow_html=True)

        st.image("https://s3.ap-south-1.amazonaws.com/cdn-shebaxyz/images/categories_images/thumbs/1617278510_carrepairservices.jpg")
        with st.expander("See Details"):
            st.write("""
            We have professional service partners with verified resources. Our resources are experienced because we try to provide punctual service. We are making a one-stop service solution because your flexibility is our main priority.\n
        Car Cleaning (Wash & Deep Cleaning)
        Car Polishing
        Car Ceramic Coating
        Car Detailing (Cleaning & Polishing)

🟠 Pricing & Terms   
Service Charge: The mentioned pricing is estimated service charges which might vary slightly depending on: Vehicle Type, Model, and Service Availability.

🟠 Home Service Policy: The home service charge of maximum BDT 300 is applicable if the customer decides not to take the service after the service provider visited the location. However, if the customer agrees to avail this service on scheduled time then the home service charge is not applicable.

🟠 Liability: Smart Garage will not be liable for any pre-existing issues/potential risks reported by the service provider but not handled due to customer refusal to car wash/polish service the same.

🟠 Payment: You can pay through online or COD. After payment please make sure, you have received the SMS containing the money receipt.
            """)
        #st.write("Overview of Car Washing & Polishing Service")
            
    #st.image("")
    st.markdown("<h2 style='text-align: center; font-family:   ui-sans-serif, system-ui, Helvetica, Arial,Inter,ui-sans-serif,system-ui,Helvetica,Arial,sans-serif ; color: rgb(255, 75, 75);'>Make an Order</h2>", unsafe_allow_html=True)

    # order = st.button("Make a order")
    # if order :
    with st.container():
            option = st.selectbox(
     'Select the category ',
     ('Car Washing', 'Car Painting', 'LPG Conversion'))

            #st.write('You selected:', option)
            st.text_input("Credit Card Details")
            st.text_input("Exp Date")
            st.text_input("CVC")
            st.write("Price : 30$")
            st.button("Checkout")

#################### End Services ###############


############## Start Avaiable Solts Page ###########


elif(menu_id == "Login"):
    names = ['Sadia', 'Tonmoy']
    usernames = ['sadia', 'tonmoy']
    passwords = ['123', '456']
    #hashed_passwords = stauth.Hasher(passwords).generate()
  #  authenticator = stauth.Authenticate(names,usernames,hashed_passwords,
    # 'some_cookie_name','some_signature_key',cookie_expiry_days=30)
   # name, authentication_status, username = authenticator.login('Login','main')
    flag = True
    if(flag):
        st.markdown(
            "<h2 style='text-align: center; font-family:  cursive, sans-serif; color: #B3E1E2;'>-----LOGIN------</h2>", unsafe_allow_html=True)
        my_form = st.form(key='form-1')

        username = my_form.text_input("UserName")
        passwords = my_form.text_input("Password")
        submit = my_form.form_submit_button('Submit')
    if(submit == 'Submit'):
        flag = False
        st.balloons()
        st.write("Welcome")

elif (menu_id == "Registration"):
    st.markdown("<h2 style='text-align: center; font-family:  cursive, sans-serif; color: #B3E1E2;'>-----Registration------</h2>", unsafe_allow_html=True)
    # creating a form
    my_form = st.form(key='form-1')
    # creating input fields
    fname = my_form.text_input('First Name:')
    lname = my_form.text_input('Last Name:')
    email = my_form.text_input('Email:')
    # creating radio button
    gender = my_form.radio('Gender', ('Male', 'Female'))
    # creating slider
    age = my_form.slider('Age:', 1, 120)
    # creating date picker
    bday = my_form.date_input('Enter Birthdate:')
    # creating a text area
    address = my_form.text_area('Enter Address:')
    # creating a submit button
    submit = my_form.form_submit_button('Submit')
    # the following gets updated after clicking on submit, printing the details of the fields that are submitted in the form
    if(submit == 'Submit'):
        st.write('Name is '+fname+' '+lname)
        st.write('Email is '+email)
        st.write('Gender is '+gender)
        st.write('Age is '+str(age))
        st.write('Birthday is '+str(bday))
        st.write('Address is '+address)
# st.sidebar.header("Login")
######## Footer #########


# st.markdown(
#     """
#     <h1 class="sm:col-start-1 sm:col-end-13 xl:col-start-3 xl:col-end-11 text-5xl sm:text-7xl md:text-8xl font-bold text-gray-90 color rgb(255, 75, 75)">A faster way to build and share data&nbsp;apps</h1>
#     """,unsafe_allow_html=True
# )