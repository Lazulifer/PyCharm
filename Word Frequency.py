#This project will be able to count how often a given word appears in
#A block of text

from collections import Counter
import re #RegEx import
#ReGex (Regular Expression), is a sequence of characters that forms
#a search pattern. RegEx can be used to check if
#a string contains the specified search pattern.

#Function that returns in a list of tuples the specified word
#and how often it appears
def get_frequency(text: str) -> list[tuple[str, int]]:
    lowercase_text: str = text.lower()
    words: list[str] = re.findall(r'\b\w+\b', lowercase_text) #"Simple" RegEx code
    #RegEx is supposedly one of the most annoying things in Python.
    #Likely worth learning on our own

    word_counts: Counter = Counter(words) #It will be a counter object
    #Objects are instantiations of classes
    return word_counts.most_common()
    #Other way to specify only the n most common:
    #return word_counts.most_common(n=?)

def main() -> None:
    text: str = input("Enter your text: ").strip()
    #Normally, you'd also want to make sure you get rid of leading and trailing whitespace,
    # but RegEx actually prevents that on its own
    word_frequencies: list[tuple[str, int]] = get_frequency(text)

    for word, count in word_frequencies: #Two arguments in this loops because it's a tuple
        print(f'{word}: {count}')

if __name__ == '__main__':
    main()