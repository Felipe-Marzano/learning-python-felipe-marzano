# Training how to use 'class'
# Class Bike witg all the info I wanted
class Bike:
    def __init__(self, brand, year, model, cc, color, value):
        self.brand = brand
        self.year = year
        self.model = model
        self.cc = cc
        self.color = color
        self.value = value

# Function to show all info about the bike
    def bike_info(self):
        print(self.brand, self.year, self.model,
              self.cc, self.color, self.value)


# First bike
bike1 = Bike('Honda', 'Bros', '2021', '160', 'Red', 'R$ 18.727,00')
bike1.bike_info()

# Secound bike
bike2 = Bike('Honda', '2023', 'PCX', '160', 'Preta', 'R$ 20.290,00')
bike2.bike_info()

# Third bike
bike3 = Bike('Yamaha', '2023', 'NMax', '160', 'Cinza', 'R$ 20.654,00')
bike3.bike_info()

# Printing the brand of all bikes
print(bike1.brand, bike2.brand, bike3.brand)
