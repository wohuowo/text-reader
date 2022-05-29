# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from itertools import count


def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename, "r") as file:
        var = file.read()
    for line in var:
        line = line.strip()
        line = line.lower()
        line = line.strip("/n,.?")
    words = var.split(" ")
    return words


def count_words():
    text = read_file_content("story.txt")
    # [assignment] Add your code here
    counts = dict()
    for words in text:
        if words in counts:
            counts[words] += 1
        else:
            counts[words] = 1
    for key in list(counts.keys()):
        print(key, ":", counts[key])
    return count_words


filename = str(input('enter filename: '))
print(read_file_content(filename))

print(count_words())
