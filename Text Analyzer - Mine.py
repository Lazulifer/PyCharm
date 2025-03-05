
'''
HW
1. Create a much more user-friendly message regarding the analysis
2. Add the top 5 most common words to the analysis message
'''

def open_file(path: str) -> str:
    with open(path, 'r') as file:
        text: str = file.read()
        return text


def analyze(text: str) -> dict[str, int]:
    print(f'"{text}"')

    word_counts: dict = {}
    sentences = text.split()

    # For each word in the file, count how often they appear and put them in a dictionary
    for word in sentences:
        word_sum: int = 0
        word_sum += sentences.count(word)
        word_counts[word] = word_sum

    # For each word in the dictionary, count the 5 most frequent ones
    word_counts = dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True))
    ordered_list = list(word_counts.keys())
    top_5 = ordered_list[:5]

    result: dict[str, int] = {
        'The total amount of characters including spaces': len(text),
        'The total amount of characters excluding spaces': len(text.replace(' ','')),
        'The total number of spaces': text.count(''),
        'The total number of words': len(text.split()),
        'The 5 most common words in the phrase are': top_5
    }
    return result


def main() -> None:
    text: str = open_file('note.txt')
    analysis: dict[str, int] = analyze(text)

    for key, value in analysis.items():
        print(f'{key}: {value}')


if __name__ == '__main__':
    main()

'''
HW
1. Create a much more user-friendly message regarding the analysis
2. Add the top 5 most common words to the analysis message
'''