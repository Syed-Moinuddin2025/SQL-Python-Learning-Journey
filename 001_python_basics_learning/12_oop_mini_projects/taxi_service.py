# taxi_service.py
import os

class Taxi:
    def __init__(self, driver_name, car_number):
        self.driver = driver_name
        self.car_number = car_number
        self.available = True
        self.total_trips = 0
        self.total_earning = 0
        self.trip_history = []

    def pick_customer(self, customer_name):
        if self.available:
            print(f"🚖 {self.car_number} driven by {self.driver} picked up {customer_name}.")
            self.current_customer = customer_name
            self.available = False
        else:
            print(f"❌ Taxi {self.car_number} is currently not available.")

    def drop_customer(self, distance_km):
        if not self.available:
            rate_per_km = 15
            fare = distance_km * rate_per_km
            self.total_trips += 1
            self.total_earning += fare
            self.trip_history.append(
                (self.current_customer, distance_km, fare, self.driver)
            )
            print(f"✅ {self.car_number} has dropped the customer.")
            print(f"💰 Trip Fare: ₹{fare}")
            self.available = True
        else:
            print(f"🚕 Taxi {self.car_number} is already available.")

    def status(self):
        status_text = "Available ✅" if self.available else "Busy ❌"
        print(f"🔍 Taxi {self.car_number} ({self.driver}): {status_text}")

    def change_driver(self, new_driver_name):
        print(f"👷 Driver changed from {self.driver} to {new_driver_name}")
        self.driver = new_driver_name

    def summary(self):
        print(f"\n📊 Summary for Taxi {self.car_number}")
        print(f"   Total Trips: {self.total_trips}")
        print(f"   Total Earning: ₹{self.total_earning}")
        print(f"   Trip Details:")
        for i, (customer, km, fare, driver) in enumerate(self.trip_history, 1):
            print(f"    {i}. {customer} | {km} km | ₹{fare} | Driver: {driver}")

    def save_summary_to_file(self):
        # Save in the same folder where this script is
        folder = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(folder, f"{self.car_number}_summary.txt")

        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"📊 Summary for Taxi {self.car_number}\n")
            f.write(f"Total Trips: {self.total_trips}\n")
            f.write(f"Total Earning: ₹{self.total_earning}\n")
            f.write(f"Trip Details:\n")
            for i, (customer, km, fare, driver) in enumerate(self.trip_history, 1):
                f.write(f"{i}. {customer} | {km} km | ₹{fare} | Driver: {driver}\n")

        print(f"📁 Summary saved to file: {filename}")
