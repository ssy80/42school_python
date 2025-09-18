class calculator:

    def __init__(self, nums):
        """Constructor for calculator class"""
        self.nums = nums

    def __add__(self, object) -> None:
        """Add object to each element in nums and print the result"""
        self.nums = [n + object for n in self.nums]
        print(self.nums)

    def __mul__(self, object) -> None:
        """Multiply each element in nums by object and print the result"""
        self.nums = [n * object for n in self.nums]
        print(self.nums)

    def __sub__(self, object) -> None:
        """Subtract object from each element in nums and print the result"""
        self.nums = [n - object for n in self.nums]
        print(self.nums)

    def __truediv__(self, object) -> None:
        """Divide each element in nums by object and print the result"""
        if int(object) == 0:
            print("Error: division by zero")
            return
        self.nums = [n / object for n in self.nums]
        print(self.nums)


def main():
    """main()"""

    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5
    v3 / 0


if __name__ == "__main__":
    main()
