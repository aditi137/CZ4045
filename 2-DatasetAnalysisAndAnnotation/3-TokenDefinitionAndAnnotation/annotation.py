import os
import pandas as pd
from nltk.tokenize import TweetTokenizer

def tokeniseAndGetFrame(df):
    tokenizer = TweetTokenizer()
    posts = df[1]

    new_DF = pd.DataFrame()
    print("Now tokenizing and generating output data frame... (this does take a while)")
    for row in posts:
        row.replace('\n', ' ').replace('\r', '')
        tokens = tokenizer.tokenize(row)
        DF_row = pd.Series(tokens)
        new_DF = new_DF.append(DF_row, ignore_index=True)        

    return new_DF

def main():
    df = pd.read_csv("OutputData/selectedPosts.csv", header=None, skiprows=1)

    outputDF = tokeniseAndGetFrame(df)

    print("Now writing to csv...")
    outputSubdir = 'OutputData'
    outputDF.to_csv(os.path.join(outputSubdir, 'annotatedPosts.csv'), encoding='utf-8')
    print("Finished")
    

main()
