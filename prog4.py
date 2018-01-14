print('Fuel Estimator\n')

class Car:
    def __init__(self, mpg = 0,fuel = 0):
        self.mpg = mpg
        self.fuel = fuel
    def add_gas(self,fuel):
        self.fuel += fuel 
    def drive(self,miles):
        self.fuel = self.fuel - miles/self.mpg  
    def get_gas_level(self):
        return self.fuel
                  
def main():
    user_miles = int(input('MPG: '))
    user_fuel = int(input('Fuel: '))
    user_distance = int(input('Distance: '))

    my_suv = Car (user_miles)
    my_suv.add_gas(user_fuel)
    my_suv.drive(user_distance)

    
    print('%.2f gallons remaining.'%(my_suv.get_gas_level()))
    choice = input('Would you like to enter another (y/n): ')
    while choice != 'y' and choice != 'n':
        choice = input('Would you like to enter another (y/n): ')
    while choice == 'y':
        user_miles = int(input('MPG: '))
        user_fuel = int(input('Fuel: '))
        user_distance = int(input('Distance: '))


        my_suv = Car (user_miles)
        my_suv.add_gas(user_fuel)
        my_suv.drive(user_distance)
        
        print('%.2f gallons remaining.'%(my_suv.get_gas_level()))
        choice = input('Would you like to enter another (y/n): ')

        while choice != 'y' and choice != 'n':
            choice = input('Would you like to enter another (y/n): ')


if __name__ == '__main__':
    main()
    
