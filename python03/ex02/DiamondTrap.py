from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):

    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)

    @property
    def eyes(self):
        return self._eyes

    @eyes.setter
    def eyes(self, colour):
        self._eyes = colour

    @property
    def hairs(self):
        return self._hairs

    @hairs.setter
    def hairs(self, colour):
        self._hairs = colour

    # will call @eyes.setter
    def set_eyes(self, colour):
        self.eyes = colour

    def get_eyes(self):
        return self.eyes

    # will call @hairs_setter
    def set_hairs(self, colour):
        self.hairs = colour

    def get_hairs(self):
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
