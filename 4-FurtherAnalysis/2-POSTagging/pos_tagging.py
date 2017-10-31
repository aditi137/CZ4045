import nltk
import random
import pandas as pd
import os
from nltk.stem import PorterStemmer
import string

nltk.download('averaged_perceptron_tagger')


def main():
    inputSubdir = 'InputData'
    outputSubdir = 'OutputData'
    if not os.path.exists(outputSubdir):
        os.makedirs(outputSubdir)

    tokenized_result = pd.read_csv(os.path.join(inputSubdir, 'allTokenizedPosts.csv'), encoding='utf-8')['Tokens']

    data = []

    delimiter = ['.', '!', '?']
    sent = []
    irreg_token = []
    eng_token = set(nltk.corpus.words.words()).union(set(string.punctuation))
    ps = PorterStemmer()
    
    for i, word in tokenized_result.iteritems():
        word = str(word)
        sent.append(word)
        if word in delimiter:
            if len(irreg_token) and len(sent) > 8:
                data.append(nltk.pos_tag(sent))
            sent = []
            irreg_token = []
        elif not (word.isalpha() or word.isdigit()) and ps.stem(word.lower()) not in eng_token:
            irreg_token.append(word)

    df = pd.DataFrame(random.sample(data, 10))
    df.to_csv(os.path.join(outputSubdir, 'taggedSentences.csv'), encoding='utf-8')

    print("Finished")

main()