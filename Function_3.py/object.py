class dog:
    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age
dog1 = dog(name="buddy", breed="boxer", age=15)
dog2 = dog(name="billybuck", breed="lab", age=10)
print(dog1.name)
print(dog1.breed)
print(dog2.age)