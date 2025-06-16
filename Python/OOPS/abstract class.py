from abc import ABC, abstractmethod
class xyz(ABC):
    @abstractmethod
    def show(self):
        pass
    def display(self):
        print("Hello")
class pqr(xyz):
    def __init__(self):
        self.display()
