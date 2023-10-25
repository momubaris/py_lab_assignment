from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Dog is barking bow bow!")
class Cat(Animal):
    def sound(self):
        print("cat is crying meaw meaw")
class Cow(Animal):
    def sound(self):
        print("cow is crying maau maau")
dog=Dog()
cat=Cat()
cow=Cow()
print(dog.sound())
print(cat.sound())
print(cow.sound())
