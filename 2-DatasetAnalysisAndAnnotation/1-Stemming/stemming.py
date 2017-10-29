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


def includeStemOriginalWords(originalWords, filename):
    stems = pandas.read_csv(filename, encoding='utf-8')
    stems['original words'] = ""
    stems = stems.fillna('nan')
    for index, row in stems.iterrows():
        stem = row['stem']
        stems.loc[index, 'original words'] = ','.join(originalWords[stem])
    stems.to_csv(filename, index=False, encoding='utf-8')


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
    stemOriginalWords = {}

    for post in posts:
        words = tokenizer.tokenize(post)
        for word in words:
            lowerWord = word.lower()
            if lowerWord not in stopWords and not bool(re.search(r'\d', lowerWord)):
                wordsBeforeStem.append(lowerWord)
                stemWord = stemmer.stem(lowerWord)
                if stemWord in stemOriginalWords:
                    stemOriginalWords[stemWord].add(lowerWord)
                else:
                    stemOriginalWords[stemWord] = {lowerWord}
                wordsAfterStem.append(stemWord)

    countSortAndSave(wordsBeforeStem, os.path.join(outputSubdir, 'wordsBeforeStemming.csv'))
    countSortAndSave(wordsAfterStem, os.path.join(outputSubdir, 'wordsAfterStemming.csv'))
    includeStemOriginalWords(stemOriginalWords, os.path.join(outputSubdir, 'wordsAfterStemming.csv'))
    print("Finished")

main()



