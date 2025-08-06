import sys
from ft_filter import ft_filter
import string


def main():
    """
    Accepts two arguments: a string(S), and an integer(N). The
    program will output a list of words from S that have a length greater than N and 
    words taht do not contain any punctuation and is printable.
    """
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
        return
    
    try:
        arg1 = str(sys.argv[1])
        arg2 = int(sys.argv[2])
    except ValueError:
        print("AssertionError: the arguments are bad")
        return
    
    words = [w for w in arg1.split() if len(w) > arg2]
    words = list(ft_filter(lambda w:all(c not in string.punctuation or c not in string.printable for c in w), words))
    print(words)


if __name__ == "__main__":
    main()