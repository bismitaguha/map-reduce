import sys
from itertools import groupby
from operator import itemgetter

def main(separator='\t'):
    current_word = None
    current_count = 0
    word = None
    file = open("output.txt", "r", encoding="utf-8")

    for line in file:
        line = line.strip()
        words = line.split(f'{separator}1')
        words.sort()

        for word in words:
            if current_word == word:
                current_count += 1
            else:
                if current_word:
                    print (current_word, separator, current_count)
                current_count = 1
                current_word = word
        
    if current_word == word:
        print (current_word, separator, current_count)

if __name__ == "__main__":
    main()
