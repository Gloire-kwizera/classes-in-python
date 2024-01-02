class person:
    def __init__(self,name,age):
        self.Name = name
        self.Age = age
        
    def printname(self):
      print(f"my name is {self.Name}, and am {self.Age} years old")


str1=person("gloire", 23)   
str1.printname() 
