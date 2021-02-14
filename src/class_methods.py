class Person:
    number_of_person = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_persons(cls):
        return cls.number_of_person

    @classmethod
    def add_person(cls):
        cls.number_of_person += 1


if __name__ == '__main__':
    p1 = Person('Tim')
    p2 = Person('Jill')

    print(Person.number_of_persons())