# Buggy version
class EmployeeBug:
    def __init__(self, id, salary):
        int_id = id   
        int_salary = salary 
      

#Correct version
class Employee:
    def __init__(self, id, salary):
        self.id = id         
        self.salary = salary  

# Test the Buggy version 
print("=== Buggy Example ===")
e1 = EmployeeBug(101, 5000)
try:
    print(e1.id)  
except AttributeError as err:
    print("Error:", err)

# Test Correct version 
print("\n=== Correct Example ===")
e2 = Employee(102, 6000)
print("Employee ID:", e2.id)
print("Employee Salary:", e2.salary)
