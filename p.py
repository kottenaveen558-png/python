class Animal:
     def __init__(self,name):
        self.name = name
        
     def speak(self):
        print("Animal makes a sound")
        
class Dog(Animal):
    super().speak(self)
    
    def speak(self):
        print("Dog barks")


d1 = Dog("Tommy")
d1.speak()
    
