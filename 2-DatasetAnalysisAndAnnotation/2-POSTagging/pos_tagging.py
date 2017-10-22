import nltk
import random
import pandas
import os

def main():
    inputSubdir = 'InputData'
    outputSubdir = 'OutputData'
    if not os.path.exists(outputSubdir):
        os.makedirs(outputSubdir)


    posts = pandas.read_csv(os.path.join(inputSubdir, 'posts.csv'), encoding='utf-8')['Text']
    
    sentences = []
    for post in posts:
        sentences = sentences + nltk.sent_tokenize(post)
    
    data = []
    for sent in random.sample(sentences, 10):
        data = data + nltk.pos_tag(nltk.word_tokenize(sent))

    df = pandas.DataFrame.from_dict(data)
    df.columns = ['word', 'tag']
    df.to_csv(os.path.join(outputSubdir, 'taggedWords.csv'), index=False, encoding='utf-8')

    print "Finished"

main()