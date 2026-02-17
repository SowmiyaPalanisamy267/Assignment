#1. Bank account calculation
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance   # private attribute(Encapsulation)

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.interest_rate / 100
        interest_amount = self.get_balance() * interest
        self.deposit(interest_amount)
        print(f"Your interest {interest_amount} has been added. New balance: {self.get_balance()}")


class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance, minimum_balance):
        super().__init__(account_number, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):    # Overriding withdraw method of the parent BankAccount by child CurrentAccount
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif self.get_balance() - amount < self.minimum_balance:
            print("Cannot withdraw: Minimum balance requirement violated")
        else:
            super().withdraw(amount)


print("---- Savings Account ----")
sa = SavingsAccount("SA101", 1000, 5)
sa.deposit(500)
sa.calculate_interest()
sa.withdraw(300)
print("Final Balance:", sa.get_balance())

print("\n---- Current Account ----")
ca = CurrentAccount("CA201", 2000, 500)
ca.withdraw(1000)
ca.withdraw(500)  # Should fail (minimum balance rule)
print("Final Balance:", ca.get_balance())
########################################################################

#2.Employee salary calculation
class Employee():
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def calculate_salary(self):
        return self.salary


class RegularEmployee(Employee):
    def __init__(self, name, salary, bonus):
      super().__init__(name, salary)
      self.bonus = bonus
    def calculate_salary(self):
        return self.salary + self.bonus


class ContractEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name, salary = 0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


class Manager(Employee):
    def __init__(self, name, salary, allowance):
        super().__init__(name, salary)
        self.allowance = allowance
    def calculate_salary(self):
        return self.salary + self.allowance

employees = [
    RegularEmployee("Sowmiya", 30000, 5000),
    ContractEmployee("Nishaan", 1000, 40),
    Manager("Akshvi", 50000, 10000)
]
for emp in employees:
    print(f"{emp.name} earns: {emp.calculate_salary()}")  #polymorphism
########################################################################

#3.Rental calculation of vehicles
class Vehicle:
    def __init__(self, model, rental_rate):
        self.model = model
        self.rental_rate = rental_rate

    def calculate_rental(self, duration):
        return self.rental_rate * duration


class Car(Vehicle):
    def calculate_rental(self, duration):
        return self.rental_rate * duration


class Bike(Vehicle):
    def calculate_rental(self, duration):
        return self.rental_rate * duration


class Truck(Vehicle):
    def calculate_rental(self, duration):
        return self.rental_rate * duration


vehicles = [
    Car("Sedan", 1000),
    Bike("Sports Bike", 100),
    Truck("Heavy Truck", 2000)
]

durations = [3, 10, 2]

for v, d in zip(vehicles, durations):
    print(f"{v.model} rental cost: {v.calculate_rental(d)}")
########################################################################

