
class Demo:
    def __init__(self,No1,No2):
        self.i = No1
        self.j = No2

    def Fun(self):
        print(self.i)
        print(self.j)
    
    def Gun(self):    
        print(self.i)
        print(self.j)
    
def main():
    
    obj1 = Demo(11,21)
    obj2 = Demo(51,101)

    obj1.Fun()
    obj2.Fun()

    obj1.Gun()
    obj2.Gun()
    
if __name__ == "__main__":
    main()