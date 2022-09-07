class Employee:

    def __init__(self, name, salary):
        self.name = name;
        self.salary = salary;


    def set_name(self, name):
        self.name = name


    def set_salary(self, salary):
        self.salary = salary


    def get_name(self):
        return self.name;

    def get_salary(self):
        return self.salary;

    def __str__(self) -> str:
        return f"""
     "Name - " {self.name} 
     "Salary - " {self.salary}
     """

   # def show(self):
      #  print("Name - ", self.name, "\nSalary - ", self.salary)
