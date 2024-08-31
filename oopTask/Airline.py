
from Flight import Flight

class Airline():
    def __init__(self, name: str, tax: int):
        self.name = name
        self.flights = []
        self.tax = tax

    def addFlight(self, flight: Flight):
        if flight  in self.flights:
            print("Flight already exists")
            return
        if flight.airline != None:
            print("Flight does not belong to this airline")
            return

        self.flights.append(flight)
        flight.airline = self.name

    def removeFlight(self, flight : Flight):
        self.flights.remove(flight)

    def getAllFlights(self):
        return self.flights
    
    
    def calculateFlightPrice(self, flight : Flight):
        return flight.calculateFlightPrice() + self.tax