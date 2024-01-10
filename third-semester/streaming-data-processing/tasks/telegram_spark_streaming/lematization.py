import re
import pymorphy2

morph = pymorphy2.MorphAnalyzer()

def clean_and_lemmatize_text(text):
    cleaned_text = re.sub(r'[^а-яА-Я ]', '', text)
    cleaned_text = re.sub(r'\s{2,}', ' ', cleaned_text)
    words = cleaned_text.split(" ")
    lemmatized_words = [morph.parse(word)[0].normal_form for word in words]
    return " ".join(lemmatized_words)
