import nltk
import pandas
import os
from nltk.tokenize import RegexpTokenizer

inputSubdir = 'InputData'
outputSubdir = 'OutputData'

def cleanRead(filename):
    df = pandas.read_csv(os.path.join(inputSubdir, filename), encoding='utf-8', names=list(range(1000)))
    df = df.iloc[1:] #Remove first row, with the column index
    df.reset_index(drop=True, inplace=True)
    return df

def createmanuallyAnnotatedPostsForDiff(tokenizer):
    manuallyAnnotatedPostsSubdir = outputSubdir + '/ManuallyAnnotatedPosts'
    if not os.path.exists(manuallyAnnotatedPostsSubdir):
        os.makedirs(manuallyAnnotatedPostsSubdir)

    posts = pandas.DataFrame()
    posts = posts.append(cleanRead('annotatedPosts1.csv'), ignore_index=True)
    posts = posts.append(cleanRead('annotatedPosts2.csv'), ignore_index=True)
    posts = posts.append(cleanRead('annotatedPosts3.csv'), ignore_index=True)
    posts = posts.append(cleanRead('annotatedPosts4.csv'), ignore_index=True)

    posts.drop(posts.columns[0], axis=1, inplace=True)
        
    for i, post in posts.iterrows():    
        filename = 'Post' + str(i + 1) + '.csv'
        cleanRow = post.to_frame().transpose().dropna(axis=1)
        cleanRow.to_csv(os.path.join(manuallyAnnotatedPostsSubdir, filename), encoding='utf-8', index=False, header=None)

def main():
    if not os.path.exists(outputSubdir):
        os.makedirs(outputSubdir)

    # Negative lookahead
    #(?!term1|term2|term3)

    importDetector = 'import\s+[\w]+'
    functionDetector = '([\w]+\.)*[\w]+\(.*?\)'
    defDetector = 'def\s+' + functionDetector + ':'
    asignDetector = '[\w]+\s*[+\-]*=\s*[\w]+'
    urlDetector = 'http[^\s()[\]]*'
    etcDetector = 'etc\.*'
    utcDetector = '(utc|UTC)\s*[+\-]\s*\d'
    word = '[\w$&@]+' 
    wordMidLettersDetector = word + '([^\w\s,/[\]]*' + word + ')*'
    arrayDetector = '\[((\s*[\w]+\s*)(,\s*[\w]+\s*)*)?\]'
    anything = '[^\s]'
    ellipsisDetector = '\.{3,}'
    mrDetector = 'M(r|s|Mrs)\.'
    arrowDetector = '(<+-+)|(-+>+)'
    mathDetector = '\d(\s*[-+*%/]\s*\d)+'
    versionDetector = '(\d[-./])*\d+[-+*]([\s,.:]|$)+'
    forExampleDetector = 'i\.e\.'


    # THE ORDER IN THIS ARRAY IS IMPORTANT, THE FIRST MATCH IS THE SELECTED ONE
    regexExpressions = [
        importDetector,
        defDetector,
        functionDetector,
        ##asignDetector,
        arrayDetector,
        urlDetector,
        utcDetector,
        etcDetector,
        ellipsisDetector,
        mrDetector,
        arrowDetector,
        #mathDetector,
        #versionDetector, #We need to match the version without matching the next stop character (coma, dot...) This does not seem possible
        forExampleDetector,
        wordMidLettersDetector,
        word,
        anything
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

        selectedWords = []

        for row in words:    
            for column in row:
                if len(column) > 0:
                    selectedWords.append(column)
                    break
    
        filename = 'Post' + str(i + 1) + '.csv'
        df = pandas.DataFrame(selectedWords)
        cleanDf = df.transpose().dropna(axis=1)
        cleanDf.to_csv(os.path.join(postsSubdir, filename), encoding='utf-8', index=False, header=None)

    createmanuallyAnnotatedPostsForDiff(tokenizer)

    print "Finished"

main()
