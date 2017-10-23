import nltk
import re
import random
import pandas
import os

nltk.download('averaged_perceptron_tagger')

def tagSentencesFrom(sentences, fileName):
    data = []
    
    for sent in random.sample(sentences, 10):
        data += [nltk.pos_tag(nltk.word_tokenize(sent))]

    df = pandas.DataFrame(data)
    df.to_csv(fileName, encoding='utf-8')

def main():
    inputSubdir = 'InputData'
    outputSubdir = 'OutputData'
    if not os.path.exists(outputSubdir):
        os.makedirs(outputSubdir)

    posts = pandas.read_csv(os.path.join(inputSubdir, 'posts.csv'), encoding='utf-8')['Text']

    sentences = []
    for post in posts:
        sentences += nltk.sent_tokenize(post)

    qualitySentences = []
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        alphabeticalWords = filter(re.compile(r'[a-zA-Z,.?!]+').search, words)
        if len(words) == len(alphabeticalWords) and len(words) > 10: 
            qualitySentences.append(sentence)

    tagSentencesFrom(sentences, os.path.join(outputSubdir, 'taggedSentences.csv'))
    tagSentencesFrom(qualitySentences, os.path.join(outputSubdir, 'taggedQualitySentences.csv'))
    print "Finished"

main()