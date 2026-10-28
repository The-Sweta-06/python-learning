class Employee:
    name = "Sweta"
    language = "Py" # This is a class attribute
    salary = 1200000
    
sweta = Employee()
sweta.name = "Sweta" # This is an instance attribute
print(sweta.name, sweta.language, sweta.salary)

rohan = Employee()
rohan.name = "Rohan Roro Robinson"
print(rohan.salary, rohan.language)


# Here name is instance attribute and salary and language are class attributes as they directly belong to the class