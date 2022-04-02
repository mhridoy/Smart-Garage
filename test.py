# import streamlit as st
# import hydralit_components as hc
# import datetime

# #make it look nice from the start
# st.set_page_config(layout='wide',initial_sidebar_state='collapsed',)

# # specify the primary menu definition
# menu_data = [
#     {'icon': "far fa-copy", 'label':"Left End"},
#     {'id':'Copy','icon':"🐙",'label':"Copy"},
#     {'icon': "fa-solid fa-radar",'label':"Dropdown1", 'submenu':[{'id':' subid11','icon': "fa fa-paperclip", 'label':"Sub-item 1"},{'id':'subid12','icon': "💀", 'label':"Sub-item 2"},{'id':'subid13','icon': "fa fa-database", 'label':"Sub-item 3"}]},
#     {'icon': "far fa-chart-bar", 'label':"Chart"},#no tooltip message
#     {'id':' Crazy return value 💀','icon': "💀", 'label':"Calendar"},
#     {'icon': "fas fa-tachometer-alt", 'label':"Dashboard",'ttip':"I'm the Dashboard tooltip!"}, #can add a tooltip message
#     {'icon': "far fa-copy", 'label':"Right End"},
#     {'icon': "fa-solid fa-radar",'label':"Dropdown2", 'submenu':[{'label':"Sub-item 1", 'icon': "fa fa-meh"},{'label':"Sub-item 2"},{'icon':'🙉','label':"Sub-item 3",}]},
# ]

# over_theme = {'txc_inactive': '#FFFFFF'}
# menu_id = hc.nav_bar(
#     menu_definition=menu_data,
#     override_theme=over_theme,
#     home_name='Home',
#     login_name='Logout',
#     hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
#     sticky_nav=True, #at the top or not
#     sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
# )

# if st.button('click me'):
#   st.info('You clicked at: {}'.format(datetime.datetime.now()))


# if st.sidebar.button('click me too'):
#   st.info('You clicked at: {}'.format(datetime.datetime.now()))

# #get the id of the menu item clicked
# st.info(f"{menu_id}")


# # can apply customisation to almost all the properties 0f the progress ba
# override_theme_1 = {'bgcolor': '#EFF8F7','progress_color': 'green'}
# override_theme_2 = {'bgcolor': 'green','content_color': 'white','progress_color': 'red'}
# override_theme_3 = {'content_color': 'red','progress_color': 'orange'}

# # can just use 'good', 'bad', 'neutral' sentiment to auto color the bar
# hc.progress_bar(25,'Something something')
# hc.progress_bar(35,'Something something',sentiment='good')
# hc.progress_bar(95,'Something something',sentiment='neutral')
# hc.progress_bar(47,'Something something',sentiment='bad')

# # customise the the theming for a neutral content
# hc.progress_bar(5,'Something something - 1a',key='pa1',override_theme=override_theme_1)
# hc.progress_bar(35,'Something something - 2a',key='pa2',sentiment='good',override_theme=override_theme_2)
# hc.progress_bar(95,'Something something - 3a',key='pa3',sentiment='neutral')
# hc.progress_bar(47,'Something something - 4a',key='pa4',sentiment='bad',override_theme=override_theme_3)

import streamlit as st
r1, r2 = st.columns([6, 2])

ingredients = {'1','2','3'}
directions = {'fjdljf','dfldsjlf','dfadslfla'}

with r2:
                    # st.write(st.session_state.get_random_frame)
                    # if hasattr(st, "session_state"):
                    #     recipe_post = generator.generate_frame(generated_recipe, st.session_state.get_random_frame)
                    # else:
                    #     recipe_post = generator.generate_frame(generated_recipe, get_random_frame)

                    recipe_post ="https://cdn-shebaxyz.s3.ap-south-1.amazonaws.com/sheba_xyz/images/app-download.webp"

                    st.image(
                        recipe_post,
                        # width=500,
                        caption="Save image and share on your social media",
                        use_column_width="auto",
                        output_format="PNG"
                    )
with r2:
    st.markdown(
                        " ".join([
                            "<div class='r-text-recipe'>",
                            "<div class='food-title'>",
                            f"<h2 class='font-title text-bold'>Hello</h2>",
                            "</div>",
                            '<div class="divider"><div class="divider-mask"></div></div>',
                            "<h3 class='ingredients font-body text-bold'>Ingredients</h3>",
                            "<ul class='ingredients-list font-body'>",
                            " ".join([f'<li>{item}</li>' for item in ingredients]),
                            "</ul>",
                            "<h3 class='directions font-body text-bold'>Directions</h3>",
                            "<ol class='ingredients-list font-body'>",
                            " ".join([f'<li>{item}</li>' for item in directions]),
                            "</ol>",
                            "</div>"
                        ]),
                        unsafe_allow_html=True
                    )