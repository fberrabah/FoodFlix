import sys
sys.path.insert(0,"/home/apprenant/Desktop/FARIZD/FOOD/")
import pandas as pd
import streamlit as st

from src.data import load_data
from src.modeling import train_model
from src.visu.user_visu import get_similar_products

df = pd.read_csv("/home/apprenant/Desktop/FARIZD/FOOD/Data/intermediate.csv")



st.title("Bienvenue sur FOODFLIX")


user_input = st.sidebar.text_input('Entrer le produit que vous cherchez :').lower() 
st.write(user_input)
st.sidebar.selectbox('Select methode', ["tfidf","BERT"])



 
if user_input :
    results = get_similar_products(user_input) 
    for item in results:
        st.title("{}".format(item['product_name']))
        st.image("{}".format(item['image_url']))
        
        st.write("Marque : {}".format(item['brands']))
        st.write("Graisse: {}".format(item['fat_100g']))
        st.write("Sucre: {}".format(item['sugars_100g']))
        st.write("Fibre: {}".format(item['fiber_100g']))
        st.write("Proteine: {}".format(item['proteins_100g']))
        st.write("Sel: {}".format(item['salt_100g']))
        st.write("Énergie: {}".format(item['energy_100g']))
        st.write("Liste des ingrédients: {}".format(item['ingredients_text']))
        if item['nutrition_grade_fr'] == "a":
             st.image("https://www.apivia-prevention.fr/wp-content/uploads/2019/09/Nutri-score.png", width=250)
        if item['nutrition_grade_fr'] == "b":
            st.image("https://www.coordinationrurale.fr/wp-content/uploads/2017/11/le-nouveau-logo-nutriscore-ministere-de-la-sante-1489594533.jpg", width=250)
        if item['nutrition_grade_fr'] == "c":
            st.image("https://s3.eu-central-1.amazonaws.com/media.quitoque.fr/blog/2018/06/logo-nutri-score.jpg", width=250)
        if item['nutrition_grade_fr'] == "d":
            st.image("https://www.nutractiv.fr/files/cto_layout/images/RVB%20D%20cerne%C2%A6%C3%BC.jpg", width=250)
        if item['nutrition_grade_fr'] == "e":
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Nutri-score-E.svg/1024px-Nutri-score-E.svg.png", width=250)
        st.write("----------------")
        st.write("----------------")

