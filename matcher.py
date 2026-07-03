from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_score(a,b):
 v=TfidfVectorizer(stop_words='english');m=v.fit_transform([a,b]);return cosine_similarity(m[0:1],m[1:2])[0][0]*100