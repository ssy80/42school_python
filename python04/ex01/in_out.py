def square(x: int | float) -> int | float:
    """Return the square of a number."""

    return x * x


def pow(x: int | float) -> int | float:
    """Return the number raised to the power of itself."""

    return x ** x


def outer(x: int | float, function) -> object:
    """Return a closure that applies a function
    to a number and counts calls."""

    count = 0

    def inner() -> float:
        nonlocal count
        nonlocal x
        count += 1
        x = function(x)
        return x
    return inner


'''A closure (my_counter()) is a function object that remembers values
 in enclosing scopes even if they are not present
  in memory anymore'''
'''
When you define a function inside another function,
the inner function can use variables from the outer function’s scope.
If you return the inner function, it retains those variables
'''


def main():
    """main()"""

    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())
    print("---")
    another_counter = outer(1.5, pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())


if __name__ == "__main__":
    main()
