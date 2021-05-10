import sys
import streamlit as st
sys.path.insert(0,"/home/apprenant/Desktop/FARIZD/FOOD/")

from sklearn.metrics.pairwise import linear_kernel
from src.data.load_data import listings
from src.modeling.train_model import tf, tfidf_matrix


@st.cache

def get_similar_products(user_input):
    # user_input = input("Enter product name:")
    #print("product name is: " + user_input)

    user_matrix = tf.transform([user_input])
    #user_matrix = tf.encode([user_input])
    cosine_similarities = linear_kernel(user_matrix, tfidf_matrix)
    similar_indices = cosine_similarities[0].argsort()[:-100:-1]
    similar_items = [(cosine_similarities[0][i], i) for i in similar_indices]
    results = []
    for i in range(10):
        results.append(listings.iloc[similar_items[i][1]])
        # print(listings.iloc[results[i][1]])
    return results
