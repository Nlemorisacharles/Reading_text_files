# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


def read_file_content(storyfile):
    storyfile = open(storyfile , "r")
    storyfile = storyfile.read()

    return  storyfile 

def count_words():
    text = read_file_content("./story.txt").lower()
    count_words = {}
    for word in text.split():

        if word in count_words:
            count_words[word] += 1
        else:
            count_words[word]= 1
    return count_words

print (count_words())