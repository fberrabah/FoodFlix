import sys
sys.path.insert(0,"/home/apprenant/Desktop/FARIZD/FOOD/")

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from src.data.load_data import listings, STOPWORDSFR
from sentence_transformers import SentenceTransformer, models
import torch
import warnings



warnings.filterwarnings('ignore')

# word_embedding_model = models.Transformer("camembert-base")

# # Spécifie le calcul à mettre en place pour passer du word embedding au sentence embedding
# pooling_model = models.Pooling(word_embedding_model.get_word_embedding_dimension(),
#                               pooling_mode_mean_tokens=True,
#                               pooling_mode_max_tokens=False)

# model = SentenceTransformer(modules=[word_embedding_model, pooling_model])

# tfidf_matrix = tf.model(listings['content'])

#tfidf_matrix = tf.encode(listings['content'])

model = SentenceTransformer('paraphrase-distilroberta-base-v1')

tf = TfidfVectorizer(analyzer = 'word', ngram_range = (1, 2), min_df = 0, stop_words = ['le', 'la', 'de', 'du', 'au', 'les', 'aux', 'null'])
tfidf_matrix = tf.fit_transform(listings['content'])

#comtevectoriezer 