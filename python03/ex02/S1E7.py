from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family"""

    family_name = "Baratheon"
    eyes = "brown"
    hairs = "dark"

    def __init__(self, first_name, is_alive=True):
        """Constructor of Baratheon"""
        super().__init__(first_name, is_alive)
        self.family_name = Baratheon.family_name
        self.eyes = Baratheon.eyes
        self.hairs = Baratheon.hairs

    def die(self):
        """Change is_alive to False """
        self.is_alive = False

    def __str__(self):
        """Return str representation of Baratheon"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return str representation of Baratheon"""
        return self.__str__()

    @classmethod
    def create_baratheon(cls, first_name, is_alive=True):
        """Class method to create Baratheon"""
        return cls(first_name, is_alive)


class Lannister(Character):
    """Representing the Lannister family"""

    family_name = "Lannister"
    eyes = "blue"
    hairs = "light"

    def __init__(self, first_name, is_alive=True):
        """Constructor of Lannister"""
        super().__init__(first_name, is_alive)
        self.family_name = Lannister.family_name
        self.eyes = Lannister.eyes
        self.hairs = Lannister.hairs

    def die(self):
        """Change is_alive to False """
        self.is_alive = False

    def __str__(self):
        """Return str representation of Lannister"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return str representation of Lannister"""
        return self.__str__()

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Class method to create Lannister"""
        return cls(first_name, is_alive)


"""def main():
    '''main()'''
    Robert = Baratheon("Robert")
    print(Robert.__dict__)
    print(Robert.__str__)
    print(Robert.__repr__)
    print(Robert.is_alive)
    Robert.die()
    print(Robert.is_alive)
    print(Robert.__doc__)
    print("---")
    Cersei = Lannister("Cersei")
    print(Cersei.__dict__)
    print(Cersei.__str__)
    print(Cersei.is_alive)
    print("---")
    Jaine = Lannister.create_lannister("Jaine", True)
    print(f"Name:\
    {Jaine.first_name, type(Jaine).__name__}, Alive: {Jaine.is_alive}")

    Test = Baratheon.create_baratheon("Test", True)
    print(f"Name:\
    {Test.first_name, type(Test).__name__}, Alive: {Test.is_alive}")


if __name__ == "__main__":
    main()"""
