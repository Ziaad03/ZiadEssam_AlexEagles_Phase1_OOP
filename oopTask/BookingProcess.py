from Customer import Customer
from Flight import Flight
import Airline

class BookingProcess:
    def __init__(self, customer : Customer, airline: Airline):
        self.customer = customer
        self.airline = airline
    def bookAFlightToCustomer(self, flight : Flight):
        # If a customer already has a flight, remove it
        if self.customer.flight:
            self.customer.flight.removeCustomer(self.customer)
            self.customer.flight = None
        self.customer.bookAFlight(flight)
        flight.addCustomer(self.customer)
        #search if a flight in egypt airline has a flight number that matches with the customer flight number
        for flight in self.airline.flights:
            if flight.flightNumber == self.customer.flight.flightNumber:
                print("Flight booked in ", self.airline.name)
                print("Flight number: ", flight.flightNumber)
                print("customer social Id:", self.customer.socialId)
                print("flight price: ", self.airline.calculateFlightPrice(flight))

        
        