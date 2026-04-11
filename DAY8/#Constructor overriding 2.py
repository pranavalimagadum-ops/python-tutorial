#Constructor overriding  
class Father:  
    def __init__(self):  
        print("Father:= i am on time at breakfast table")  
  
class Child(Father):  
    def __init__(self):  
        print("Child:= i will be late for breakfast")  
        super().__init__()
  
obj = Child()  