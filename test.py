import streamlit as st
import streamlit.components.v1 as components

food_image= "https://assets.vogue.in/photos/5ed8e32c64872e9ac717c767/master/pass/pizza%20recipe%20pizza%20to%20make%20at%20home%20quick%20and%20easy%20recipes.jpg"
title="How to make a Pizza"
ingredients =[
            "1 lb. phyllo dough, thawed 1 lb. phyllo dough, thawed",
            "1 c. unsalted butter, melted",
            "2 c chopped walnuts",
            "1/2 tsp. cinnamon",
            "1 1/2 c water",
            "3/4 c honey",
            "1/4 c melted chocolate",
        ]

directions =[
            "in a large skillet, heat oil to 375.",
            "season chops on both sides with salt and pepper.",
            "dredge chops in flour, shaking off excess.",
            "dip chops into eggs, then coat with breadcrumbs.",
            "fry chops until golden brown, about 3 minutes per side.",
            "transfer to a platter and keep warm.",
            "pour off all but 1 tablespoon of fat from skillet.",
            "add gravy and cook over medium heat, stirring occasionally, until thickened, about 5 minutes.",
            "spoon gravy over chops and sprinkle with parsley.",
            "makes 4 servings.",
        ]

def prepare_frame(self, recipe, chef_name):
        frame_path = self.chef_frames[chef_name.lower()]
        food_logo = generate_food_with_logo_image(frame_path, self.logo_frame, recipe["image"])
        frame = generate_recipe_image(
            recipe,
            self.main_frame,
            food_logo,
            self.fonts,
            bg_color="#ffffff"
        )
        return frame
def generate_frame(self, recipe, chef_name):
        return self.prepare_frame(recipe, chef_name)

r1, r2 = st.columns([6, 2])

with r2:
                    # st.write(st.session_state.get_random_frame)
                    # if hasattr(st, "session_state"):
                    #     recipe_post = generator.generate_frame(generated_recipe, st.session_state.get_random_frame)
                    # else:
                    #     recipe_post = generator.generate_frame(generated_recipe, get_random_frame)

                    recipe_post = generator.generate_frame(generated_recipe, chef.split()[-1])

                    st.image(
                        recipe_post,
                        # width=500,
                        caption="Save image and share on your social media",
                        use_column_width="auto",
                        output_format="PNG"
                    )

with r1:
                    st.markdown(
                                    " ".join([
                                        "<div class='r-text-recipe'>",
                                        "<div class='food-title'>",
                                        f"<img src='{food_image}' />",
                                        f"<h2 class='font-title text-bold'>{title}</h2>",
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