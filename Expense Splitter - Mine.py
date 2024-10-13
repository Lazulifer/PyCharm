"""
HW
1. Edit the script to give the user the option to enter uneven splits (20%-40%-40%)
2. Make it so that if the user encounters an error, the program nicely asks them to
try again with a proper value, instead of just terminating the program.
"""


def final_split_declaration(total_amount: float, number_of_people: int, currency: str) -> None:

    print(f'Total Expense: {currency}{total_amount:,.2f}')
    print(f'Number of People: {number_of_people}')

#Declares the amount a named person is paying
def payment_declaration(total_amount: float, fraction: float, names: str, currency: str) -> None:

    #Gets the dollar amount of someone's split
    split: float = total_amount * fraction
    #Prints out what someone is paying
    print(f'{names} is paying: {currency}{split:,.2f}')
    print('')


#Entry point
def main() -> None:

    #Asks for total expenses, total number of people, and defines the variable for total splits
    try:
        total_amount: str = input("Enter the total amount of the expense: ")

        #As long as it isn't getting a digit, it will ask to try again
        while not total_amount.isdigit():
            total_amount: str = input("That's okay, try again: ")

        #Turns the string into a float
        total_amount = float(total_amount)

        #As long as it isn't getting an int, it will ask to try again
        number_of_people: int = int(input("Number of people sharing: "))
        while number_of_people < 2:
            number_of_people: int = int(input("That's okay, try again: "))

        sum_of_splits: float = 0
        print('')

        #Loops the code for however many people there are
        for num in range(number_of_people):

            #Asks for payer's name
            names: str = str(input("What's your name? "))

            #Asks the users how much they want to pay for as a float from 0 to 1
            fraction: float = float(input("How much are you paying? "))

            # If the fraction submitted is greater than one, then stop the program
            while fraction > 1:
                fraction: float = float(input("That's okay, try again: "))

            #Tracks the total amount of splits to make sure it doesn't go beyond 1
            sum_of_splits += fraction

            # Declares how much someone is paying
            payment_declaration(total_amount, fraction, names, currency="$")

            # If the sum of the splits is 1, leave the program
            if sum_of_splits == 1:
                break

            #If the sum of the splits is greater than 1, declare the tip and leave the program
            if sum_of_splits > 1:
                tip = sum_of_splits - 1
                tip = tip * 100
                currency: str = "$"
                print(f"Party paid {currency}{tip:,.2f} in tips")
                print('')
                break

        final_split_declaration(total_amount, number_of_people, currency="$")

    except ValueError as e: #Be sure to encounter exceptions explicitly
        print(f'Error: {e}')

if __name__ == "__main__":
    main()

"""   
HW
1. Edit the script to give the user the option to enter uneven splits (20%-40%-40%)
2. Make it so that if the user encounters an error, the program nicely asks them to 
try again with a proper value, instead of just terminating the program.
"""