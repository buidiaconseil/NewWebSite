#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :

import nltk
import nltk
#nltk.download('stopwords')
#nltk.download('punkt')

import nltk.data
import re
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

from nltk import word_tokenize as wt
from sklearn.feature_extraction.text import TfidfVectorizer


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

corpus = [text]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())
print(X.shape)
print(X)