from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):

    def __init__(self, first_name, is_alive=True):
        """Constructor"""
        super().__init__(first_name, is_alive)
        self._eyes = Baratheon.eyes
        self._hairs = Baratheon.hairs

    @property
    def eyes(self):
        """eyes property"""
        return self._eyes

    @eyes.setter
    def eyes(self, colour):
        """eyes setter"""
        self._eyes = colour

    @property
    def hairs(self):
        """hairs property"""
        return self._hairs

    @hairs.setter
    def hairs(self, colour):
        """hairs setter"""
        self._hairs = colour

    # will call @eyes.setter
    def set_eyes(self, colour):
        """set_eyes method to call @eyes.setter"""
        self.eyes = colour

    def get_eyes(self):
        """get_eyes method to call @eyes property"""
        return self.eyes

    # will call @hairs_setter
    def set_hairs(self, colour):
        """set_hairs method to call @hairs.setter"""
        self.hairs = colour

    def get_hairs(self):
        """get_hairs method to call @hairs property"""
        return self.hairs


def main():
    """main()"""

    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.set_eyes("blue")
    Joffrey.set_hairs("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hairs())
    print(Joffrey.__dict__)


if __name__ == "__main__":
    main()
