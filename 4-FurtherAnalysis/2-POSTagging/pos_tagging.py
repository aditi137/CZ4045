import nltk
import random
import pandas as pd
import os

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
    eng_token = nltk.corpus.words.words()
    
    for i, word in tokenized_result.iteritems():
        sent.append(word)
        if word in delimiter:
            if len(irreg_token):
                data.append(nltk.pos_tag(sent))
            sent = []
            irreg_token = []
        elif not (word.isalpha() or word.isdigit()) and word.lower() not in eng_token:
            irreg_token.append(word)

    df = pd.DataFrame(random.sample(data, 10))
    df.to_csv(os.path.join(outputSubdir, 'taggedSentences.csv'), encoding='utf-8')

    print("Finished")

main()