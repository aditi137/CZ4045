import nltk
import pandas
import os
from nltk.tokenize import RegexpTokenizer

def main():
    inputSubdir = 'InputData'
    outputSubdir = 'OutputData'
    if not os.path.exists(outputSubdir):
        os.makedirs(outputSubdir)

    # Negative lookahead
    #(?!term1|term2|term3)

    # Issue with RegexpTokenizer - added ?: after each left parenthesis to make the capturing group a non-capturing group
    importDetector = 'import\s+[\w]+'
    functionDetector = '[\w]+\(?:.*?\)'
    defDetector = 'def\s+' + functionDetector + ':'
    asignDetector = '[\w]+\s*[+\-]*=\s*[\w]+'
    word = '[\w]+'
    arrayDetector = '\[(?:(?:\s*[\w]+\s*)(?:,\s*[\w]+\s*)*)?\]'
    anything = '[^\s]+'

    
    # THE ORDER IN THIS ARRAY IS IMPORTANT, THE FIRST MATCH IS THE SELECTED ONE
    regexExpressions = [
        importDetector,
        defDetector,
        functionDetector,
        asignDetector,
        arrayDetector,
        word,
        anything
    ]

    # Construct the regex expression from the array
    regex = ''
    for expression in regexExpressions:
        regex += '(?:' + expression + ')' + '|'
    regex = regex[:-1] #Remove last character
    
    print regex
    tokenizer = RegexpTokenizer(regex)

    #posts = pandas.read_csv(os.path.join(inputSubdir, 'selectedPosts.csv'), encoding='utf-8')['post']
    posts = pandas.read_csv(os.path.join(inputSubdir, 'posts.csv'), encoding='utf-8')['Text']

    postsSubdir = outputSubdir + '/PostCollection'
    if not os.path.exists(postsSubdir):
        os.makedirs(postsSubdir)

    all_tokens_output = []
    for i, post in enumerate(posts):
        words = tokenizer.tokenize(post)
        all_tokens_output += words
        
        filename = 'Post' + str(i + 1) + '.csv'
        df = pandas.DataFrame(words)
        df.to_csv(os.path.join(postsSubdir, filename), encoding='utf-8')

    combinedDF = pandas.DataFrame(all_tokens_output)
    combinedDF.columns = ['Tokens']
    combinedDF.to_csv(os.path.join(outputSubdir, "allTokenizedPosts.csv"), encoding='utf-8')
    
    print "Finished"

main()
