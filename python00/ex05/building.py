import sys
import string


def main():
    """
        Accept a string as argument, parse and counts the total characters, upper, lower, 
        punctuation, spaces and digits in the string
    """
    if len(sys.argv) == 1:
        arg = input("What is the text to count?\n")
    elif len(sys.argv) == 2:
        arg = sys.argv[1]
    else:
        print("AssertionError: more than one argument is provided")
        return

    total = len(arg)
    upper_count = sum(1 for c in arg if c.isupper())
    lower_count = sum(1 for c in arg if c.islower())
    punc_count = sum(1 for c in arg if c in string.punctuation)
    spaces_count = sum(1 for c in arg if c.isspace())
    digits_count = sum(1 for c in arg if c.isdigit())

    print(f"The text contains {total} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punc_count} punctuation marks")
    print(f"{spaces_count} spaces")
    print(f"{digits_count} digits")


if __name__ == "__main__":
    main()
