# Write a class called Address that has two attributes: number and street name. Make sure
# you have an init method that initializes the object appropriately


class address (object):
    def __init__(self, number, street):
        self.number = number
        self.street = street

class campusAddress (address):
    def __init__(self, officeNumber):
        super().__init__(number='221b', street='Baker')
        self.officeNumber = officeNumber
