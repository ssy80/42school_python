import sys
import string

def main():
    """
    Accepts one argument: a string. 
    The program will output an equivalent of the string in morse code.
    """
    NESTED_MORSE = { 
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
        "0": "----- ",
    }

    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad 1")
        return

    arg = sys.argv[1]

    if not all(c.isalnum() or c.isspace() for c in arg):
        print("AssertionError: the arguments are bad 2")
        return

    print("".join(NESTED_MORSE[c.upper()] for c in arg))


if __name__ == "__main__":
    main()
