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
    df.columns = ['post']
    df.to_csv(os.path.join(outputSubdir, 'selectedPosts.csv'), encoding='utf-8')

    selectedPostsSubdir = outputSubdir + '/PostCollection'
    if not os.path.exists(selectedPostsSubdir):
        os.makedirs(selectedPostsSubdir)

    for i, post in enumerate(selectedPosts):
        filename = 'Post' + str(i + 1) + '.txt'
        with open(os.path.join(selectedPostsSubdir, filename),'w') as f:
            print >>f, post.encode('utf8')
            f.close()

    print "Finished"

main()