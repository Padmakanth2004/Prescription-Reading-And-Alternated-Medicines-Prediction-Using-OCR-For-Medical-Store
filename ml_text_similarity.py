from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def suggest_alternate_tablets(extracted_tablet_name, dataset_path):
    # Load the dataset
    df = pd.read_csv(dataset_path)
    tname=extracted_tablet_name
    filtered_df = df[df['name'] == tname]
    composition_name=filtered_df['shortcomposition1'].iloc[0]
    # Calculate TF-IDF vectors for compositions
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(df['shortcomposition1'].fillna(''))

    # Calculate TF-IDF vector for the extracted tablet's composition
    extracted_tfidf = tfidf_vectorizer.transform([composition_name])

    # Calculate similarity between extracted tablet's composition and dataset compositions
    similarities = cosine_similarity(extracted_tfidf, tfidf_matrix)[0]

    # Combine tablets with their similarity scores
    tablet_similarity_pairs = list(zip(df['name'], similarities))

    # Sort tablets by similarity in descending order
    tablet_similarity_pairs.sort(key=lambda x: x[1], reverse=True)

    # Extract top 5 tablets with highest similarity
    suggestions = tablet_similarity_pairs[:10]

    return suggestions
