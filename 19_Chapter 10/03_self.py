class Employee:
    language = "Python" # This is a class attribute
    salary = 1200000
    
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    @staticmethod
    def greet(self):
        print("Good morning")
sweta = Employee()
# sweta.language = "JavaScript" # This is an instance attribute

sweta.greet()
sweta.getInfo()

# Employee.getInfo(harry)

