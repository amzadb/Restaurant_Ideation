import streamlit as st
import langchain_helper

st.title("Restaurant Ideation")

def generate_restaurant_name_and_menu_items(cuisine):
    return {
        'restaurant_name' : 'Hyderabadi Delicious Delights',
        'menu_items' : 'Chicken Dum Biryani, Murg Malai Kabab, Chicken Tandoori, Chicken Tikka, Mutton Marag, Kadai Chicken'
    }

cuisine = st.sidebar.selectbox("Select a cuisine:", ("Hyderabadi", "Punjabi", "Udipi", "Indian", "Arabic", "American", "Italian", "Mexican", "Chinese", "Japanese"))

if cuisine:
    response = langchain_helper.generate_restaurant_name_and_menu_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")

    st.write("*** Menu Items ***")
    for item in menu_items:
        st.write("-", item)