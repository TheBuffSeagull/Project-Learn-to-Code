# A class is a set of instructions for how to make an instance
# see line 21
class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        # The self paramater takes the paramater from the init above and turns them into attributes
        # attributes are globally accessible in other functions like sit and roll_over below
        self.name = name
        self.age = age

    def sit(self):
        """"Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

# We can use this one to make individual instances represeting specific dogs
my_dog = Dog("Willie", 6)
your_dog = Dog('peaches', 4)

print(f"My Dog's name is {my_dog.name}.")
print(f"My dog {my_dog.age} years old.\n")

print(f"Your Dog's name is {your_dog.name}.")
print(f"My dog {your_dog.age} years old.\n")

print(Dog.sit(my_dog))
print(Dog.sit(your_dog))
