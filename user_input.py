import sys
sys.path.insert(0,"/home/apprenant/Desktop/FARIZD/FOOD/")

import streamlit as st
import sys
sys.path.insert(0,"/home/apprenant/Desktop/FARIZD/FOOD/")

from src.data import load_data
from src.modeling import train_model
from src.visu.user_visu import get_similar_products

get_similar_products()