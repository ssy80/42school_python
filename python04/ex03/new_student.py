import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random id"""

    return "".join(random.choices(string.ascii_lowercase, k=15))


'''default_factory=generate_id tells the dataclass to call
generate_id each time a new Student is created'''


@dataclass
class Student:
    """Student class"""
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        """Post-initialization to set the login attribute."""
        self.login = self.name[0] + self.surname


"""def main():
    '''main()'''

    student = Student(name="Edward", surname="agle")
    student1 = Student(name="James", surname="test")
    print(student)
    print(student1)

    '''student2= Student(name = "Edward", surname = "agle", id = "toto")
    print(student2)'''


if __name__ == "__main__":
    main()"""
