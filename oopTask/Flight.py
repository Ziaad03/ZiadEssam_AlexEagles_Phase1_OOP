from Meal import Meal
from AdditionalService import AdditionalService
import Customer



class Flight:
    def __init__(self,flightNumber:int ,departureTime: str, arrivalTime: str, departureAirport: str, arrivalAirport: str, flightPrice: float):
        self.flightNumber = flightNumber
        self.departureTime = departureTime
        self.arrivalTime = arrivalTime
        self.departureAirport = departureAirport
        self.arrivalAirport = arrivalAirport
        self.flightPrice = flightPrice
        self.meal = None
        self.additionalService = []
        self.customer= [] 
        self.airline = None
        

    def getFlightDetails(self):
        return {
            'flightNumber': self.flightNumber,
            'Departure Time': self.departureTime,
            'Arrival Time': self.arrivalTime,
            'Departure Airport': self.departureAirport,
            'Arrival Airport': self.arrivalAirport,
            'Flight Price': self.flightPrice,
            'meal': self.meal,
            'Additional Service': self.additionalService
        }

    def addCustomer(self, customer : Customer):
        self.customer.append(customer)
    
    def calculateFlightPrice(self):
        # based on meal or additional service will calculate price
        totalPrice = 0
        if self.meal:
            totalPrice += self.meal.price
        if len(self.additionalService) != 0:
            for service in self.additionalService:
                totalPrice += service.price  # assuming all additional services have price attribute  # change to actual logic if needed  # change to actual logic if needed  # change to actual logic if needed  # change to actual logic if needed  # change to actual logic if needed  # change to actual logic if needed  # change to actual logic if needed  # change to actual logic if needed  # change to actual logic if needed  # change to actual logic if needed  # change to actual logic if needed  # change to actual logic if needed  # change to actual logic if needed  # change to actual logic if needed  # change to actual logic if needed  # change to actual logic if needed  # change to actual logic if needed  # change to actual logic if needed  # change to actual logic if needed  # change to actual logic if needed  # change to actual logic if needed  # change to actual logic if needed
            
        return (self.flightPrice + totalPrice) 
    
    def addMeal(self, meal: Meal):
        self.meal = meal
    
    def addAdditionalService(self, additionalService: AdditionalService):
        self.additionalService.append(additionalService)