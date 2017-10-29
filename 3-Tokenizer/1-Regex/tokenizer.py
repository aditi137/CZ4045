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

    importDetector = 'import\s+[a-zA-Z0-9]+'
    functionDetector = '[a-zA-Z0-9]+\(.*?\):'
    defDetector = 'def\s+' + functionDetector
    asignDetector = '[a-zA-Z0-9]+\s*[+\-]*=\s*[a-zA-Z0-9]+'
    
    # THE ORDER IN THIS ARRAY IS IMPORTANT, THE FIRST MATCH IS THE SELECTED ONE
    regexExpressions = [
        importDetector,
        defDetector,
        functionDetector,
        asignDetector,
        '[^\n\t ]+'
    ]

    # Construct the regex espression from the array
    regex = ''
    for expression in regexExpressions:
        regex += '(' + expression + ')' + '|'
    regex = regex[:-1] #Remove last character
    
    print regex
    tokenizer = RegexpTokenizer(regex)

    posts = pandas.read_csv(os.path.join(inputSubdir, 'selectedPosts.csv'), encoding='utf-8')['post']

    postsSubdir = outputSubdir + '/PostCollection'
    if not os.path.exists(postsSubdir):
        os.makedirs(postsSubdir)

    for i, post in enumerate(posts):
        words = tokenizer.tokenize(post)
    
        filename = 'Post' + str(i + 1) + '.csv'
        df = pandas.DataFrame(words)
        df.to_csv(os.path.join(postsSubdir, filename), encoding='utf-8')

    print "Finished"

main()
