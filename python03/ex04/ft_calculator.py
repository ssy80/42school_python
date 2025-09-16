class calculator:

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        total = sum(a * b for a, b in zip(V1, V2))
        print(f"Dot product is: {total}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        total = [float(a + b) for a, b in zip(V1, V2)]
        print(f"Add Vector is: {total}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        total = [float(a - b) for a, b in zip(V1, V2)]
        print(f"Sous Vector is: {total}")


def main():
    """main()"""

    a = [5, 10, 2]
    b = [2, 4, 3]
    calculator.dotproduct(a, b)
    calculator.add_vec(a, b)
    calculator.sous_vec(a, b)


if __name__ == "__main__":
    main()
