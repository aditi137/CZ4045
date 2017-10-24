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
    selectedPosts = random.sample(posts, 100)

    df = pandas.DataFrame(selectedPosts)
    df.to_csv(os.path.join(outputSubdir, 'selectedPosts.csv'), encoding='utf-8')

    print "Finished"

main()