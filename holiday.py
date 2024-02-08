#create a function and name it hotel_cost, with the argument being num_nights and return the total cost of hotel stay

def hotel_cost(num_nights):
    total_hotel_cost = 80 * int(num_nights) # Assuming $80 per night
    return total_hotel_cost

#create a function and name it plane_cost, with the argument being city_flight and return the cost of the flight

def plane_cost(city_flight):
    if city_flight == "Kigali":
        flight_cost = 800
    elif city_flight == "Monaco":
        flight_cost= 100
    else:
        #default cost for any other city
        flight_cost = 500
    return flight_cost

#create a function and name it car_rental, with the argument being rental_days and return the total cost of the car rental

def car_rental(rental_days):
    total_car_rental = 150 * int(rental_days) # Assuming $150 per day
    return total_car_rental

#create a function and name it holiday_cost, with the arguments being hotel_cost, plane_cost, car_rental and return the total cost of the holiday

def holiday_cost(hotel_cost, plane_cost, car_rental):
    total_holiday_cost = hotel_cost + plane_cost + car_rental
    return total_holiday_cost


#create a variable called city_flight and store in the city where they will be fying to
city_flight = input("Enter the name of the city where you will have your holiday: ")

#create a variable called num_nights and store the number of nights they will be staying in a hotel
num_nights = input("Enter the number of nights you will stay in the hotel: ")

#create a variable called rental_days and store the number of days for which they will be hiring a car
rental_days = input("Enter the number of days you will rent a car: ")

#calculate individual costs
hotel = hotel_cost(num_nights)
plane = plane_cost(city_flight)
car = car_rental(rental_days)

# calculate total holiday cost
total_holiday_cost = holiday_cost(hotel, plane, car)

#Print out the details of the holiday
print("My holiday: \n")
print(f"city of flight:{city_flight}")
print(f"Hotel cost: ${hotel}")
print(f"Flight cost: ${plane}")
print(f"car rental cost: ${car}")
print(f"Total Holiday cost: ${total_holiday_cost}")
