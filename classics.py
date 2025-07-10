import nltk

text = "monticello wasn't designated as a UNESCO World Heritage Site until 1987"
import regex
print(regex.split("[\s\.\,]", text))

# 
print(nltk.word_tokenize(text))

# 
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
plurals = ["caresses", "seizing", "owned"]

for word in plurals:
    print(f"{word} >>> {stemmer.stem(word)})")

# snowball is better at english and supports other languages

from nltk.stem import SnowballStemmer
sn_stemmer = SnowballStemmer("english")

for word in plurals:
    print(f"{word} >>> {sn_stemmer.stem(word)})")
    
# 
from nltk.stem import WordNetLemmatizer
lemm = WordNetLemmatizer()

for word in plurals:
    print(f"{word} >>> {lemm.lemmatize(word)}")