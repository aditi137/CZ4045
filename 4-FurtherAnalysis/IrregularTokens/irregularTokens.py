import pandas as pd
import os
import math
import nltk
from nltk.corpus import words

def getSortedWordCounts(tokenized_result):
    print("Getting sorted word counts... (incl regular tokens)")
    word_counts = dict()
    for word in tokenized_result:
        if(word in word_counts):
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    sorted_word_counts = sorted(word_counts.iteritems(), key = lambda (k,v): v, reverse=True)
    return sorted_word_counts

def getIrregularTokenCounts(word_counts):
    print("Removing regular tokens...")
    en_dict = words.words()
    irregular_word_counts = []
           
    for word,count in word_counts:
        if(len(irregular_word_counts) == 20):
            break
        elif(word.lower() in en_dict):
            continue
        else:
            irregular_word_counts.append((word,count))

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
        


        
