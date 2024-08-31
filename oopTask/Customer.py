import Flight

class Customer:
    def __init__(self, name: str, phoneNumber: int, age: int, socialId: int ):
        self.name = name
        self.phoneNumber = phoneNumber
        self.age = age
        self.socialId = socialId
        self.flight = None

    def bookAFlight(self, flight : Flight):
        self.flight = flight
    