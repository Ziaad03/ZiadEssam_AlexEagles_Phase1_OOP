import tkinter as tk
from tkinter import messagebox
from Flight import Flight
from Customer import Customer
from BookingProcess import BookingProcess
from Airline import Airline
from Meal import Meal
from AdditionalService import AdditionalService
class BookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flight Booking System")
        self.root.geometry("800x800")

        # Welcome Label
        self.welcomeLabel = tk.Label(root, text="Welcome to the Flight Booking System")
        self.welcomeLabel.pack()

        # Search Flight
        self.searchLabel = tk.Label(root, text="Search Flight (e.g., CAI,DOH): (departure,arrival)")
        self.searchLabel.pack()
        self.searchEntry = tk.Entry(root)
        self.searchEntry.pack()
        self.searchButton = tk.Button(root, text="Search", command=self.searchFlight)
        self.searchButton.pack()

        # Flight Details Display
        self.flightLabel = tk.Label(root, text="Flight Details: flightNumber,departureAirport,arrivalAirport,departureTime,arrivalTime,price,airline")
        self.flightLabel.pack()
        self.flightListbox = tk.Listbox(root)
        self.flightListbox.pack()

        # Book Flight Button
        self.bookButton = tk.Button(root, text="Book Flight", command=self.bookFlight, state=tk.DISABLED)
        self.bookButton.pack()

    def searchFlight(self):
        searchQuery = self.searchEntry.get()
        self.flightListbox.delete(0, tk.END)  # Clear previous search results
        flightFound = False
        self.foundFlights = []

        with open("flights.txt", "r") as file:
            for line in file:
                flightDetails = line.strip().split(",")
                if searchQuery == f"{flightDetails[1]},{flightDetails[2]}":
                    self.foundFlights.append(line.strip())
                    self.flightListbox.insert(tk.END, line.strip())
                    flightFound = True

        if not flightFound:
            self.flightListbox.insert(tk.END, "No flights found.")
            self.bookButton.config(state=tk.DISABLED)
        else:
            self.bookButton.config(state=tk.NORMAL)

    def bookFlight(self):
        selectedIndex = self.flightListbox.curselection()
        if not selectedIndex:
            messagebox.showerror("Error", "Please select a flight to book.")
            return
        
        selectedFlight = self.foundFlights[selectedIndex[0]]
        self.flightListbox.delete(0, tk.END)
        self.flightListbox.insert(tk.END, f"Selected Flight: {selectedFlight}")
        self.bookButton.config(state=tk.DISABLED)
        

        # Extract flight details from selectedFlight
        flightDetails = selectedFlight.split(",")

        # Assign flight details to variables
        flightNumber = flightDetails[0]
        departureAirport = flightDetails[1]
        arrivalAirport = flightDetails[2]
        departureTime = flightDetails[3]
        arrivalTime = flightDetails[4]
        price = flightDetails[5]
        airline = flightDetails[6]

        


        # Clear booking fields
        self.searchEntry.delete(0, tk.END)
        self.flightListbox.delete(0, tk.END)
        self.bookButton


        
        
        # User credentials
        self.nameLabel = tk.Label(self.root, text="Enter Name:")
        self.nameLabel.pack()
        self.nameEntry = tk.Entry(self.root)
        self.nameEntry.pack()

        self.phoneLabel = tk.Label(self.root, text="Enter Phone Number:")
        self.phoneLabel.pack()
        self.phoneEntry = tk.Entry(self.root)
        self.phoneEntry.pack()

        # User age
        self.ageLabel = tk.Label(self.root, text="Enter Age:")
        self.ageLabel.pack()
        self.ageEntry = tk.Entry(self.root)
        self.ageEntry.pack()

        # User social id
        self.socialIdLabel = tk.Label(self.root, text="Enter Social ID:")
        self.socialIdLabel.pack()
        self.socialIdEntry = tk.Entry(self.root)
        self.socialIdEntry.pack()

        # Section for meals and additional services
        self.mealLabel = tk.Label(self.root, text="Choose a meal option:")
        self.mealLabel.pack()
        self.mealOptions = ["small", "medium", "Large", "No Meal"]
        self.mealVariable = tk.StringVar(value=self.mealOptions[0])
        self.mealDropdown = tk.OptionMenu(self.root, self.mealVariable, *self.mealOptions)
        self.mealDropdown.pack()

        self.servicesLabel = tk.Label(self.root, text="Select additional services:")
        self.servicesLabel.pack()

        self.extraLuggageVariable = tk.IntVar()
        self.extraLuggageCheck = tk.Checkbutton(self.root, text="Extra Luggage", variable=self.extraLuggageVariable)
        self.extraLuggageCheck.pack()

        self.wifiVariable = tk.IntVar()
        self.wifiCheck = tk.Checkbutton(self.root, text="WIFI", variable=self.wifiVariable)
        self.wifiCheck.pack()

        

        # Create booking process

        # create flight
        self.flight = Flight(flightNumber, departureTime, arrivalTime, departureAirport, arrivalAirport, float(price))

        #If the user picked a meal then add it to the flight
        if self.mealVariable.get()!= "No Meal":
            if self.mealVariable.get() == "small":
                meal = Meal(mealType=self.mealVariable.get(), price=20)
            elif self.mealVariable.get() == "medium":
                meal = Meal(mealType=self.mealVariable.get(), price=40)
            elif self.mealVariable.get() == "Large":
                meal = Meal(mealType=self.mealVariable.get(), price=60)
            self.flight.addMeal(meal)

        # If the user add a service


        #If the user picked an additional service then add it to the flight
        additionalServices = []
        if self.extraLuggageVariable.get():
            additionalServices.append("Extra Luggage")
        if self.wifiVariable.get():
            additionalServices.append("WIFI")

        if additionalServices:
            for service in additionalServices:
                additionalService = AdditionalService(serviceType=service, price=100)
                self.flight.addAdditionalService(additionalService)

            
       

        
        # Create customer
        self.customer = Customer(name=self.nameEntry.get(), phoneNumber=self.phoneEntry.get(), age=self.ageEntry.get(), socialId=self.socialIdEntry.get())

        #create airline
        self.airline = Airline(name=airline, tax=100)
        self.airline.addFlight(self.flight)

        
        # Book the flight
        bookingProcess = BookingProcess(self.customer, self.airline)
        bookingProcess.bookAFlightToCustomer(self.flight)
       

    

        # Submit button to issue ticket
        self.submitButton = tk.Button(self.root, text="Submit", command=lambda: self.issueTicket(selectedFlight))
        self.submitButton.pack()

    def issueTicket(self, flight):
        name = self.nameEntry.get()
        phone = self.phoneEntry.get()
        meal = self.mealVariable.get()
        extraLuggage = self.extraLuggageVariable.get()
        wifi = self.wifiVariable.get()

        if name and phone:
            additionalServices = []
            if extraLuggage:
                additionalServices.append("Extra Luggage")
            if wifi:
                additionalServices.append("WIFI")

            servicesText = ", ".join(additionalServices) if additionalServices else "None"
            ticketInfo = (
                f"Ticket issued to {name}\n"
                f"Phone: {phone}\n"
                f"Flight Details: {flight}\n"
                f"Meal Option: {meal}\n"
                f"Additional Services: {servicesText}"
                f"\nTotal Price: {self.airline.calculateFlightPrice(self.flight)}" 
               
            )
            messagebox.showinfo("Ticket", ticketInfo)

            # Reset GUI
            self.nameLabel.pack_forget()
            self.nameEntry.pack_forget()
            self.phoneLabel.pack_forget()
            self.phoneEntry.pack_forget()
            self.ageLabel.pack_forget()
            self.ageEntry.pack_forget()
            self.socialIdLabel.pack_forget()
            self.socialIdEntry.pack_forget()
            self.mealLabel.pack_forget()
            self.mealDropdown.pack_forget()
            self.servicesLabel.pack_forget()
            self.extraLuggageCheck.pack_forget()
            self.wifiCheck.pack_forget()
            self.submitButton.pack_forget()
            self.flightListbox.delete(0, tk.END)
            self.searchEntry.delete(0, tk.END)
            self.bookButton.config(state=tk.DISABLED)
        else:
            messagebox.showerror("Error", "Please enter all credentials.")

#  run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = BookingApp(root)
    root.mainloop()
