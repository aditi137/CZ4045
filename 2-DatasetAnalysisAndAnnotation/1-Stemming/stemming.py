import os
import re
import pandas
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from collections import Counter

nltk.download('stopwords')

# Functions

def countSortAndSave(list, fileName):
    count = Counter(list)
    countDataFrame = pandas.DataFrame.from_dict(count, orient='index').reset_index()
    countDataFrame.columns = ['stem', 'count']
    countDataFrame.sort_values(by='count', ascending=False, inplace=True)
    countDataFrame.to_csv(fileName, index=False, encoding='utf-8')

def main():
    inputSubdir = 'InputData'
    outputSubdir = 'OutputData'
    if not os.path.exists(outputSubdir):
        os.makedirs(outputSubdir)

    stemmer = PorterStemmer()
    tokenizer = RegexpTokenizer('\w+')

    stopWords = set(stopwords.words('english'))
    posts = pandas.read_csv(os.path.join(inputSubdir, 'posts.csv'), encoding='utf-8')['Text']

    wordsBeforeStem = []
    wordsAfterStem = []

    for post in posts:
        words = tokenizer.tokenize(post)
        for word in words:
            if word not in stopWords and not bool(re.search(r'\d', word)):
                lowerWord = word.lower()
                wordsBeforeStem.append(lowerWord)
                wordsAfterStem.append(stemmer.stem(lowerWord))

    countSortAndSave(wordsBeforeStem, os.path.join(outputSubdir, 'wordsBeforeStemming.csv'))
    countSortAndSave(wordsAfterStem, os.path.join(outputSubdir, 'wordsAfterStemming.csv'))
    print("Finished")

main()



