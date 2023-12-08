class Dog:
    # class attribute
    breed = "Canine"
    
    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create instances of Dog
dog1 = Dog("Fido", 2)
dog2 = Dog("Rex", 3)

# Access the class and instance attributes
print(dog1.__class__.breed)
print(dog1.name)
print(dog2.__class__.breed)
print(dog2.name)