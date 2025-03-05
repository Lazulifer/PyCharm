import json

'''
HW
1. Right now it works fine if you insert a rate that exists, but make it so that if the user enters
enters a rate that doesn't exist, the program tells them that the currency is invalid, then
show them a list of all the valid currency options
2. Edit the script so that the "to" currency can also be specified as euro
3. [Hard Bonus] Instead of loading the data from a local JSON file, try loading the data from an API.
This task will require you to search online for a free API for currency exchange rates, and to make
a request to it so that you can load that data in this script.
'''

# Converts the JSON rates file into a dictionary in Python
def load_rates(json_file: str) -> dict[str, dict]:
    with open(json_file, 'r') as file:
        return json.load(file)

# Takes: amount of money, the base currency, the new currency
# and the conversion rate between them

def convert(amount: float, base: str, to: str, rates: dict[str, dict], json_file: str) -> float:
    with open(json_file, 'r') as file:
        base: str = base.lower() # type: ignore
        to: str = to.lower() # type: ignore

        #Getting rates from the dictionary. The type dictionary OR none
        from_rates: dict | None = rates.get(base)
        to_rates: dict | None = rates.get(to)

        try:
            if base == 'ooo': #JSON by default uses euros
                # An exception will be raised here because of the case where we return None. You can't index none
                return amount * to_rates['rate']
            else:
                return amount * (to_rates['rate'] / from_rates['rate'])
        except TypeError:
            print('Please enter a valid currency!')
            print(file.read())
            return 0.0

def main() -> None:
    rates: dict[str, dict] = load_rates('rates.json')
    amount = float(input("Type amount: "))
    base = str(input("Type 3-character base rate: "))
    to = str(input("Type 3-character to rate: "))

    #Passed-in values
    result: float = convert(amount, base, to, rates=rates, json_file = 'rates.json')
    #When calling a function, there's no need to type-annotate it, hence why json_file doesn't have ": str" here

    print(result)

if __name__ == '__main__':
    main()

'''
HW
1. Right now it works fine if you insert a rate that exists, but make it so that if the use enters
enters a rate that doesn't exist, the program tells them that the currency is invalid, then
show them a list of all the valid currency options
2. Edit the script so that the "to" currency can also be specified as euro
3. [Hard] Instead of loading the data from a local JSON file, try loading the data from an API.
This task will require you to search online for a free API for currency exchange rates, and to make
a request to it so that you can load that data in this script.
'''