from colorama import Fore, Style, init
init(autoreset=True)

def check_multiples(number, mappings):
    """
    Return a string based on the multiples of the number.
    For each key in mappings that divides the number, append the value to the output string.
    """
    return "".join(word for divisor, word in mappings.items() if number % divisor == 0) or number

def main(start, end):
    mappings = {3: Fore.LIGHTGREEN_EX + "Three" + Style.RESET_ALL,
                5: Fore.LIGHTGREEN_EX + "Five" + Style.RESET_ALL}
    numbers = range(start, end + 1)
    results = map(lambda x: check_multiples(x, mappings), numbers)
    for result in results:
        print(result)

if __name__ == "__main__":
    print(Fore.LIGHTGREEN_EX + "\nWelcome to the ThreeFive number printer!")
    print("Let's print numbers with a twist. Numbers divisible by 3 and 5 get replaced!\n" + Style.RESET_ALL)

    invalid_attempts = 0

    while True:
        try:
            start_input = input("Please enter your start number: ")
            print("")
            if not start_input.isdigit():
                raise ValueError("That's not a number.")
            start = int(start_input)
            if start < 1 or start > 100:
                raise ValueError("Start number should be between 1 and 100.")

            end_input = input("Please enter your end number: ")
            print("")
            if not end_input.isdigit():
                raise ValueError("That's not a number.")
            end = int(end_input)
            if end > 100:
                raise ValueError("Let's stick to numbers under or equal to 100!")
            elif end < start:
                raise ValueError("End number should be greater than or equal to the start number.")

            invalid_attempts = 0  # Reset counter after valid input
            print(f"\n{Fore.WHITE}Printing numbers from {start} to {end} in ThreeFive format:\n")
            main(start, end)

            repeat = input("\nWould you like to try another range? (yes/no): ").lower()
            if repeat != 'yes':
                print(Fore.LIGHTGREEN_EX + "\nThank you for using the ThreeFive number printer. Goodbye!\n")
                break

        except ValueError as ve:
            invalid_attempts += 1
            print(f"\n{Fore.LIGHTGREEN_EX}Oops! {ve}")
            if invalid_attempts > 3:
                print("Hint: Make sure you're entering numeric values. Start and end numbers should both be between 1 and 100.")
            print("Please try again.\n" + Style.RESET_ALL)
