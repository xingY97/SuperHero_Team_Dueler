class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print('{} is eating' . format(self.name))
    def drink(self):
        print('{} is drinking'.format(self.name))