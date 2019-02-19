#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :

import nltk
import nltk
#nltk.download('stopwords')
#nltk.download('punkt')
import csv
import nltk.data
import re
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

from nltk import word_tokenize as wt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import AffinityPropagation
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA, IncrementalPCA
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
import matplotlib.pyplot as plt
from mlxtend.frequent_patterns import association_rules

sp_pattern = re.compile( """[\.\!\"\s\?\-\,\']+""", re.M)
stupid_tokenizer = sp_pattern.split

french_stopwords = set(stopwords.words('french'))

filt_out =  lambda text: [token for token in text if token.lower() not in french_stopwords]
fr_stop =  lambda token: len(token) and token.lower() not in french_stopwords

data = u"""Nous recherchons -pour les besoins d'une société en plein essor- un petit jeune passionné,
plein d'entrain, pour travailler dans un domaine intellectuellement stimulant."""

data2 = u"""pour le compte d'une société en plein essor, nous recherchons un jeune qui veut se faire exploiter"""

data3 = u"""Nous avons un vrai métier, et on a besoin de produire
"""
## we are brave, we execute arbitrary code from unchecked origin \o/
## this code does a nltk.data.load('tokenizers/punkt/french.pickle') in your back
## executing unknown code from unchecked origin. I do not advise to do so!
print ("//".join(filt_out( wt(data, language="french"))))

### let's see if a regexp does better
print ("//".join(filt_out( stupid_tokenizer(data))))
stemmer = SnowballStemmer("french", ignore_stopwords=True)
stemmer2 = SnowballStemmer("french", ignore_stopwords=False)

print ("//".join(
    map(
        stemmer2.stem, filter(
            fr_stop,
            stupid_tokenizer(data)
        )
    )
))

text = " ".join(
    map(
        stemmer2.stem, filter(
            fr_stop,
            stupid_tokenizer(data)
        )
    )
)

corpus = []

with open('eggs.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        data=row[2]
        text = " ".join(
            map(
                stemmer2.stem, filter(
                    fr_stop,
                    stupid_tokenizer(data.replace("é", "e").replace("è", "e").replace("â", "a")
                                     .replace("ê", "e").replace("ù","u").replace("û","u")
                                     .replace("ë","e").replace("ü","u").replace("à","a"))
                )
            )
        )
        corpus.append(text)
        
vectorizer = TfidfVectorizer(ngram_range=(1,1), max_features=3000)
X = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())
print(X.shape)
print(X)
X_train, X_test = train_test_split( X, test_size=0.90, random_state=42)
clustering = KMeans(n_clusters=5, random_state=0).fit(X_train.toarray())
clustering

pca = PCA(n_components=100)
X_pca = pca.fit_transform(X_train.toarray())

plt.scatter(X_pca[:, 0], X_pca[:, 1], c=clustering.labels_,
                        cmap=plt.cm.nipy_spectral)
plt.show()

te = TransactionEncoder()
te_ary = te.fit(X_train.toarray()).transform(X_train.toarray())
df = pd.DataFrame(te_ary, columns=te.columns_)
frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)

frequent_itemsets

association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)

