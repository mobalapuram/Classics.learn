import random
import nltk
from nltk.util import ngrams
import random
from nltk import word_tokenize
nltk.download('punkt')

def load_corpus(file):
    with open("usstates.txt", "r") as file:
        text = file.read()
        tokens = word_tokenize(text)
        return tokens

def build_bigram_model(tokens):
    # Create list of bigrams
    bigrams = list(ngrams(tokens, 2))
    # Build a dictionary where key=word, value=list of possible following words
    model = {}
    for w1, w2 in bigrams:
        if w1 in model:
            model[w1].append(w2)
        else:
            model[w1] = [w2]
    return model

def generate_text(file_path, length=50):
    tokens = load_corpus(file_path)
    model = build_bigram_model(tokens)
    
    # Start with a random word from corpus that starts with a capital letter (optional)
    starters = [word for word in tokens if word.istitle()]
    current_word = random.choice(starters) if starters else random.choice(tokens)

    output_words = [current_word]

    for _ in range(length - 1):
        next_words = model.get(current_word)
        if not next_words:
            # If no possible next word, pick random word to restart
            current_word = random.choice(tokens)
        else:
            current_word = random.choice(next_words)
        output_words.append(current_word)

    return ' '.join(output_words)

