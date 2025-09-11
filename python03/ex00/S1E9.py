from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract Base Class of Character"""

    def __init__(self, first_name, is_alive=True):
        """Constructor of Character"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die():
        """Abstract method, sub class to implement"""
        pass


class Stark(Character):
    """Stark character Class"""

    def die(self):
        """Change Stark is_alive to False """
        self.is_alive = False


def main():
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)

    """hodor = Character("hodor")"""


if __name__ == "__main__":
    main()
