import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

text_0 = "NLTK PUNKT is a technology, that uses statistical models to identify sentence boundaries without relying on simple period-detection rules."
print(f"\nOriginal Corpus: {text_0}")
text_1 = text_0.lower()
print(f"\n1. Lower case conversion: {text_1}")

exclude = string.punctuation
print(f"\nPunctuations in english: {exclude}")

def remove_punc(text):
    for char in exclude:
        text = text.replace(char, '')
    return text

text_2 = remove_punc(text_1)
print(f"\n2. Removed after punctuations: {text_2}")

def remove_stop_words(text):
    new_text = []
    for word in text.split():
        if word in stopwords.words('english'):
            new_text.append('')
        else:
            new_text.append(word)
    return " ".join(new_text)

text_3 = remove_stop_words(text_2)
print(f"\n3. Removed after stop-words: {text_3}")

text_4_sent = sent_tokenize(text_3)
text_4_word = word_tokenize(text_3)
print(f"\n4. Tokenization: ")
print(f"\tTokenize sentences: {text_4_sent}")
print(f"\tTokenize words: {text_4_word}")

ps = PorterStemmer()
def stem_words(text):
    return " ".join([ps.stem(word) for word in text.split()])

text_5 = stem_words(text_3)
print(f"\n Stemmed words: {text_5}")

wordnet_lemmetizer = WordNetLemmatizer()
print(f"\n Lemmatized words: ")
print("{} {}".format("Word", "Lemma"))
for word in text_4_word:
    print("{} {}".format(word, wordnet_lemmetizer.lemmatize(word, pos='v')))







