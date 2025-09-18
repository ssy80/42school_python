def callLimit(limit: int):
    """Return a decorator that limits the number of calls to a function."""

    count = 0

    def callLimiter(function):
        """Decorator that limits the number of calls to a function."""

        def limit_function(*args: any, **kwds: any):
            """Limit the number of calls to a function."""

            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")
                return None
        return limit_function
    return callLimiter


"""def main():
    '''main()'''

    @callLimit(3)
    def f():
        print("f()")

    @callLimit(1)
    def g():
        print("g()")

    for i in range(3):
        f()
        g()


if __name__ == "__main__":
    main()"""
