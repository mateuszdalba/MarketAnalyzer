import pandas as pd
import pickle
import re, string, time, os
from nltk.corpus import stopwords
import nltk, spacy
from nltk.stem.snowball import SnowballStemmer


#Loading data
def load_data(dataset):
    df = pd.read_pickle(f'{dataset}')
    return df


#convert to lowercase, strip and remove punctuations
def preprocess(text):
    text = text.lower() 
    text=text.strip()  
    text=re.compile('<.*?>').sub('', text) 
    text = re.compile('[%s]' % re.escape(string.punctuation)).sub(' ', text)  
    text = re.sub('\s+', ' ', text)  
    text = re.sub(r'\[[0-9]*\]',' ',text) 
    text=re.sub(r'[^\w\s]', '', str(text).lower().strip())
    text = re.sub(r'\d',' ',text) 
    text = re.sub(r'\s+',' ',text) 
    return text

with open('polish_stopwords.txt') as file:
    lines = [line.rstrip() for line in file]   #stopwords.words('polish') # wrzucone do zmiennej, żeby nie zaczytywało za każdym razem z biblioteki

stop_words = lines

#remove stopwords
def stopword(string):
    a= [i for i in string.split() if i not in stop_words]
    return ' '.join(a)

#en_core_web_lg
lemmatizer = spacy.load('pl_core_news_sm', disable=['parser', 'ner'])


def lemmatize(string):
    return ' '.join(token.lemma_ for token in lemmatizer(string))

# snow_stemmer = SnowballStemmer(language='polish')
# def stemm(string): 
#     a= [snow_stemmer.stem(i) for i in string.split()]
#     return ' '.join(a)


def finalpreprocess(string, normalization = None):
    string = stopword(preprocess(string))
    if normalization == 'lemmatization':
        string = lemmatize(string)
    return string


def preprocess_data(dataset):
    df = load_data(dataset)
    df['clean_title'] = df['Title'].apply(lambda x: finalpreprocess(x))
    return df


df = preprocess_data('elektronika.pkl')

print(df)

nlp = spacy.load("pl_core_news_sm")
from string import punctuation
def get_hotwords(text):
    result = []
    pos_tag = ['PROPN', 'ADJ', 'NOUN'] # 1
    doc = nlp(text.lower()) # 2
    for token in doc:
        # 3
        if(token.text in nlp.Defaults.stop_words or token.text in punctuation):
            continue
        # 4
        if(token.pos_ in pos_tag):
            result.append(token.text)
                
    return result # 5


#print(preprocess(df['Title'][0]))
#print(df['Title'][0])