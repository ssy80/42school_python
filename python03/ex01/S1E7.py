from S1E9 import Character


class Baratheon(Character):
    #your code here
    def die(self):
        is_alive = False

class Lannister(Character):
    #your code here
    def die(self):
        is_alive = False
    
    # decorator
    def create_lannister(self, first_name, is_alive=True):
        """def wrapper(*args, **kwargs):
            character = func(*args, **kwargs)
            print(f"Lannister created: {character}")
            return character"""
        return wrapper
    #your code here


def main():
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
    #Jaine = Lannister.create_lannister("Jaine", True)
    #print(f"Name : {Jaine.first_name, type(Jaine).__name__}, Alive : {Jaine.is_alive}")


if __name__ == "__main__":
    main()