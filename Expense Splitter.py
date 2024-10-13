def calculate_split(total_amount: float, number_of_people: int, currency: str) -> None:
    if number_of_people < 1:
        raise ValueError("Number of people must be more than 1")

    share_per_person: float = total_amount / number_of_people

    print(f'Total Expense: {currency}{total_amount:,.2f}')
    print(f'Number of People: {number_of_people}')
    print(f'Each person should pay: {currency}{share_per_person:,.2f}')

def main() -> None:
    try:
        total_amount: float = float(input("Enter the total amount of the expense: "))
        number_of_people: int = int(input("Number of people sharing: "))

        calculate_split(total_amount, number_of_people, currency="$")
    except ValueError as e: #Be sure to encounter exceptions explicitly
        print(f'Error: {e}')

if __name__ == "__main__":
    main()