# ThreeFive Number Printer

## Description

Here we have two Python scripts that print numbers from a specified range. For multiples of three, they print "Three", for multiples of five, they print "Five", and for numbers which are multiples of both three and five, they print "ThreeFive". These scripts demonstrate different approaches in Python programming, featuring interactive command-line interfaces, exception handling, and some colouring you may find familiar 😆

## Scripts

### Script 1: Simple ThreeFive Printer

- A straightforward script using basic conditional logic.
- Emphasises simplicity leaving little areas where things can go wrong.

##

### Script 2: Advanced ThreeFive Printer

- Making use of functional programming techniques and colored output in this script.
- Interactive CLI with user input validation.
- Offers helpful hints after repeated invalid inputs for user friendliness and usability.

### Example

```
# For Script 2
Please enter your start number: 1
Please enter your end number: 15

Printing numbers from 1 to 15 in ThreeFive format:

1
2
Three
4
Five
Three
7
8
Three
Five
11
Three
13
14
ThreeFive
```

### Installation

To run the scripts, you need Python installed on your system. Additionally, for Script 2, the `colorama` Python package is required for colored output. You may need to install it using pip:

```bash
pip install colorama
```

## Usage

To start the scripts, navigate to the directory containing the scripts and run:

For Script 1:

```bash
python simple_yet_effective.py
```

For Script 2:

```bash
python functional_route_w_flare.py
```

Follow the on-screen prompts to enter the range of numbers you want to print.
