class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def bark(self):
        print(self.name, "is barking..")


if __name__ == '__main__':
    dog = Dog("Tim")
    dog.bark()
    dog.name = 'Bill'
    dog.bark()
