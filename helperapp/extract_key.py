import nltk
from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import krovetz

def extract(text):
    stop_words = stopwords.words('english')
    # stop_words.remove('send')
    stop_words = set(stop_words)
    msg = text
    words = word_tokenize(msg.lower())
    stemmer = krovetz.PyKrovetzStemmer()
    filtered_words = set()

    for word in words:
        if word not in stop_words and word.isalnum():
            stemmed_word = stemmer.stem(word)
            filtered_words.add(stemmed_word)

    return list(filtered_words)

# print(extract("show me all health plans"))