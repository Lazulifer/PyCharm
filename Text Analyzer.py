
def open_file(path: str) -> str:
    with open(path, 'r') as file:
        text: str = file.read()
        return text

def analyze(text: str) -> dict[str, int]:
    print(f'"{text}"')

    result: dict[str, int] = {
        'total_char_incl_spaces': len(text),
        'total_char_excl_spaces': len(text.replace(' ','')),
        'total_spaces': text.count(''),
        'total_words': len(text.split())
    }
    return result

def main() -> None:
    text: str = open_file('note.txt')
    analysis: dict[str, int] = analyze(text)

    for key, value in analysis.items():
        print(f'{key}:{value}')

if __name__ == '__main__':
    main()
