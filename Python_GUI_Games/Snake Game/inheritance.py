class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")


class Fish(Animal):  # fish class inherited all features from parent class Animal
    def __init__(self):
        super().__init__()  # calling animal class constructor

    def breathe(self):  # redefining breathe method using super
        super().breathe()
        print('doing this underwater')

    def swim(self):
        print("moving in water")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
