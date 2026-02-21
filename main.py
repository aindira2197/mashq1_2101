class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("...")


class Dog(Animal):
    def __init__(self, name, hususiyat):
        super().__init__(name)
        self.hususiyat = hususiyat


    def speak(self):
        super().speak()
        print("Voo voo ...")


d = Dog("Bobik", "4 oyoqli")
d.speak()
