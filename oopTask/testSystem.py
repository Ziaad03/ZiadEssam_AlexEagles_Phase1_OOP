
from Flight import Flight
from Customer import Customer
from BookingProcess import BookingProcess
from Meal import Meal
from AdditionalService import AdditionalService
from Airline import Airline

# Create an instance of EgyptAirline and QatarAirline
egyptAirline = Airline(name="EgyptAir",tax = 100)


# Create a flight
flight = Flight(flightNumber=25326 ,departureTime="12:00 AM", arrivalTime="14:00 AM", departureAirport="CAI", arrivalAirport="DOH", flightPrice=500, )

#create meal
meal = Meal(mealType="Vegan", price=60)

#create additional service
additionalService = AdditionalService(serviceType="Wifi", price=100)

# Add meal to flight
flight.addMeal(meal)

# Add additional service to flight
flight.addAdditionalService(additionalService)



# Add flight to airline
egyptAirline.addFlight(flight)

# Create a customer
customer = Customer(name="Ziad Essam", phoneNumber=123456789, age=30, socialId=987654321)

#create booking process
bookingProcess = BookingProcess(customer, egyptAirline)

# Book a flight to customer
bookingProcess.bookAFlightToCustomer(flight)


