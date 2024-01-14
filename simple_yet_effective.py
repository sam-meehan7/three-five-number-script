import argparse

def print_threes_and_fives(start, end):
    for i in range(start, end + 1):
        output = ""
        if i % 3 == 0:
            output += "Three"
        if i % 5 == 0:
            output += "Five"
        print(output or i)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Print numbers from 1 to 100 with special rules.")
    parser.add_argument('--start', type=int, default=1, help='Starting number (default: 1)')
    parser.add_argument('--end', type=int, default=100, help='Ending number (default: 100)')
    args = parser.parse_args()

    print("Printing numbers from {} to {}. Numbers divisible by 3 are replaced by 'Three', by 5 by 'Five', and by both 3 and 5 by 'ThreeFive'.".format(args.start, args.end))
    print_threes_and_fives(args.start, args.end)
