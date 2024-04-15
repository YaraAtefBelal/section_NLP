import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

def get_stopwords(language):
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords')
    
    # Get the list of stop words for the specified language
    stop_words = stopwords.words(language)
    return stop_words

# Specify the languages for which you want to retrieve stop words
languages = ['english', 'french', 'german', 'spanish','arabic']

# Retrieve and print the stop words for each language
for language in languages:
    stop_words = get_stopwords(language)
    print(f"Stop words in {language}:")
    print(stop_words)
    print()