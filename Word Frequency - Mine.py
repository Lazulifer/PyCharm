#This project will be able to count how often a given word appears in
#A block of text

from collections import Counter
import re #RegEx import
#ReGex (Regular Expression), is a sequence of characters that forms
#a search pattern. RegEx can be used to check if
#a string contains the specified search pattern.

"""
HW
1. Create a function that allows the user to read a file directly (such as a txt)
so the user doesn't have to copy and paste text.
- I should be able to reference my past work for this 
"""

#Takes user input to find a file name of their choice and returns in a list
# of tuples the specified word and how often it appears
def file_finder(text: str) -> list[tuple[str, int]]:
    opened_file = open(text, 'r')
    read_file = opened_file.read()
    words: list[str] = re.findall(r'\b\w+\b', read_file)  # "Simple" RegEx code
    opened_file.close()

    word_counts: Counter = Counter(words)  # It will be a counter object
    # Objects are instantiations of classes
    return word_counts.most_common()
    # Other way to specify only the n most common:
    # return word_counts.most_common(n=?)

def main() -> None:
    text: str = input("Enter the file name: ").strip()

    word_frequencies: list[tuple[str, int]] = file_finder(text)

    for word, count in word_frequencies: #Two arguments in this loops because it's a tuple
        print(f'{word}: {count}')

if __name__ == '__main__':
    main()

"""
HW
1. Create a function that allows the user to read a file directly (such as a txt)
so the user doesn't have to copy and paste text.
- I should be able to reference my past work for this 
"""