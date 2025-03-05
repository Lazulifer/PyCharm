
morse_code_dict: dict[str, str] = {
    'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..','1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-','?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'
}

def convert_to_morse(text: str) -> str:
    return ''.join(morse_code_dict.get(char.upper(), '') for char in text) #comprehension
    #Takes one character at a time out of our text and putting it into the get method.


def main() -> None:
    user_input: str = input('Enter text: ')
    output: str = convert_to_morse(user_input)

    print(output)

if __name__ == '__main__':
    main()
