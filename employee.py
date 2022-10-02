"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract, commissionType, wage, hours, commission, contractNo):
        self.name = name
        self.contract = contract
        self.commissionType = commissionType
        self.wage = wage
        self.hours = hours
        self.commission = commission
        self.contractNo = contractNo

    def get_pay(self):
        if self.commissionType == None:
            if self.contract == "salary":
                return self.wage
            else:
                return self.wage * self.hours
        else:
            if self.contract == "salary":
                return self.wage + self.get_commission_pay()
            else:
                return (self.wage * self.hours) + self.get_commission_pay()


        if self.contract == "salary":
            return self.wage
        else:
            return self.wage * self.hours

    def get_commission_pay(self):
        if self.commissionType == "bonus":
            return self.commission * self.contractNo
        elif self.commissionType == "contract":
            return self.commission
        else:
            return

    def __str__(self):
        if self.commissionType == None:
            if self.contract == "salary":
                return f'{self.name} works on a monthly salary of {self.wage}.  Their total pay is {self.get_pay()}.'
            else:
                return f'{self.name} works on a contract of {self.hours} hours at {self.wage}/hour.  Their total pay is {self.get_pay()}.'
        elif self.commissionType == "bonus":
            if self.contract == "salary":
                return f'{self.name} works on a monthly salary of {self.wage} and receives a commission for {self.contractNo} contract(s) at {self.commission}/contract.  Their total pay is {self.get_pay()}.'
            else:
                return f'{self.name} works on a contract of {self.hours} hours at {self.wage}/hour and receives a commission for {self.contractNo} contract(s) at {self.commission}/contract.  Their total pay is {self.get_pay()}.'
        elif self.commissionType == "contract":
            if self.contract == "salary":
                return f'{self.name} works on a monthly salary of {self.wage} and receives a bonus commission of {self.get_commission_pay()}.  Their total pay is {self.get_pay()}.'
            else:
                return f'{self.name} works on a contract of {self.hours} hours at {self.wage}/hour and receives a bonus commission of {self.get_commission_pay()}.  Their total pay is {self.get_pay()}.'


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', "salary", None, 4000, None, None, 0)


# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', "hourly", None, 25, 100, None, 0)


# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', "salary", "bonus", 3000, None, 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', "hourly", "bonus", 25, 150, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', "salary", "contract", 2000, None, 1500, None)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', "hourly", "contract", 30, 120, 600, None)
