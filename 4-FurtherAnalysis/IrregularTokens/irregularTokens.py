import pandas as pd
import os
import math
import string
import nltk
from nltk.corpus import words
from nltk.stem import PorterStemmer

def getSortedWordCounts(tokenized_result):
    print("Getting sorted word counts... (incl regular tokens)")
    word_counts = dict()
    for word in tokenized_result:
        if(isinstance(word,float)):     # getting rid of NaN values
            continue
        word = word.lower()
        if(word in word_counts):
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    sorted_word_counts = sorted(word_counts.iteritems(), key = lambda (k,v): v, reverse=True)
    return sorted_word_counts

def getIrregularTokenCounts(word_counts):
    en_dict = set(words.words())
    punctuation = set(string.punctuation)
    ps = PorterStemmer()
        
    irregular_word_counts = []
    stemmed_en_dict = []

    print("Preparing dictionary...(this will take a while)")
    for word in en_dict:
        stemmed_en_dict.append(ps.stem(word))

    print("Removing regular tokens...")
    for word,count in word_counts:
        if(len(irregular_word_counts) == 20):
            break
        if not isinstance(word,unicode):
            continue

        try:
            word = word.encode("ascii", "strict")
        except UnicodeEncodeError as e:
            continue
        
        word = word.strip()
        if(ps.stem(word) in stemmed_en_dict):
            print "Removed english word: " + word
            continue
        elif(word in punctuation):
            print "Removed punctuation: " + word
            continue
        elif(any(char in punctuation and char is not '(' and char is not ')' for char in word)):
            print "Removed punctuation in word: " + word
            continue
        elif(word.isdigit()):
            print "Removed digit word: " + word
            continue
        else:
            irregular_word_counts.append((word,count))

    # remove punctuation
    print irregular_word_counts
    return irregular_word_counts

'''
def readInPosts(inputSubdir):
    tokenized_result = []
    postsSubdir = inputSubdir + '/PostCollection'

    for i in range (1,3057):
        print "Reading in tokenized post " + str(i) + " out of 3057"
        current_post = pd.read_csv(os.path.join(postsSubdir, 'Post'+ str(i) +'.csv'), encoding='utf-8', header=None)
        tokenized_result += current_post.values.tolist()

    return tokenized_result
'''

def main():
    inputDir = 'InputData'
    outputDir = 'OutputData'

    #tokenized_result = readInPosts(inputDir)

    tokenized_result = pd.read_csv(os.path.join(inputDir, 'allTokenizedPosts.csv'), encoding='utf-8')['Tokens']
    wordCounts = getSortedWordCounts(tokenized_result)
    irrWordCounts = getIrregularTokenCounts(wordCounts)

    if not os.path.exists(outputDir):
        os.makedirs(outputDir)
        
    outputDF = pd.DataFrame(irrWordCounts)
    outputDF.columns = ['Irregular Tokens', 'Count']
    outputDF.index += 1        

    outputDF.to_csv(os.path.join(outputDir, 'top20IrregularTokens.csv'))
    print("Finished")

main()
        


        
