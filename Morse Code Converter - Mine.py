
'''
HW
1. Edit so it also works with symbols
2. Create a function that can convert morse back into regular text
'''


morse_code_dict: dict[str, str] = {
    'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..','1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.',
    '0':'-----',
}

def convert_to_morse(text: str) -> str:
    return ''.join(morse_code_dict.get(char.upper(), '') for char in text) #comprehension
    #Takes one character at a time out of our text and putting it into the get method.

def convert_to_alphanumeric(text: str) -> str:
    return ''.join(list(morse_code_dict.keys())[list(morse_code_dict.values()).index(char)] for char in text.split(" "))

def main() -> str:
    user_input: str = input('Enter text. If morse, put a space between each letter: ')
    user_input: str = user_input.upper()
    output: str = ''
    first_letter: str = user_input[0]

    if first_letter in morse_code_dict.keys(): #If it receives an alphanum
        output: str = convert_to_morse(user_input)

    else: #first_letter in morse_code_dict.values(): #If it receives morse code
        output: str = convert_to_alphanumeric(user_input)


    print(output)


if __name__ == '__main__':
    main()


'''
HW
1. Edit so it also works with symbols
2. Create a function that can convert morse back into regular text
'''