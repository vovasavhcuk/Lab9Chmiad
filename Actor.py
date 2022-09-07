from Employee import Employee


class Actor(Employee):
    count = 0;

    def __init__(self,  name, salary, role, film):
        super().__init__(name, salary)
        self.role = role
        self.film = film

    def set_role(self, role):
        self.role = role

    def set_film(self, film):
        self.film = film


    def get_role(self):
        return self.role

    def get_film(self):
        return self.film


    def __str__(self) -> str:
     return f"""
     {super(Actor, self).__str__()}
     "role - " {self.role} 
     "Film - " {self.film}
     """

    def copy(self):
        x = [self.get_name(), self.get_salary(), self.get_role(), self.get_film()]
        return x
