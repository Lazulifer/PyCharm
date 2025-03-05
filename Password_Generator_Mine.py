import secrets
import string
from enum import verify

'''
HW
1. Create a method in the Password class which checks the password's strength
- Password must be 16+ characters long
- Password must contain uppercase characters and symbols
(Mayhaps return a boolean or print statement that confirms either of these)
'''

class Password:
    #Initializer entity that describes what traits are needed for the password
    #Length, uppercase characters, and symbols. Returns None
    def __init__(self, length: int = 12, uppercase: bool = True, symbols: bool = True) -> None:

        #Gives the information to the instance
        self.length = length
        self.use_uppercase = uppercase
        self.use_symbols = symbols

        #Gets characters from string module
        self.base_characters: str = string.ascii_lowercase + string.digits

        #Checks if the password has uppercase characters or symbols
        if self.use_uppercase:
            self.base_characters += string.ascii_uppercase
        if self.use_symbols:
            self.base_characters += string.punctuation


    def generate(self) -> str:

        #Takes the password as a list of string characters
        password: list[str] = [] #initially empty to append and join symbols to it

        for i in range (self.length):

            #Creates a set of random characters the length of the init
            password.append(secrets.choice(self.base_characters))
            #choice method picks a random element from any iterable,
            #which is the string self.base_characters here

        #Converts list into a string and joins it all together with no spaces
        return ''.join(password)

    def verify(self) -> bool:

        if self.length < 17:
            return False
        if self.use_uppercase == False:
            return False
        if self.use_symbols == False:
            return False
        else:
            return True


def main() -> None:
    amount = int(input("How many characters? "))

    password: Password = Password(length=amount)

    #Generates 10 different passwords and their length
    for i in range(10):
        generated: str = password.generate()
        Verify: bool = password.verify()
        print(f'{generated} ({len(generated)} chars) {Verify}')


if __name__ == '__main__':
    main()

'''
HW
1. Create a method in the Password class which checks the password's strength
- Password must be 16+ characters long
- Password must contain uppercase characters and symbols
(Mayhaps return a boolean or print statement that confirms either of these)
'''