# 📍 GPS Class
class GPS:
    def show_location(self):
        return "Current location: Mumbai"

# 🎵 MusicSystem Class
class MusicSystem:
    def play_music(self):
        return "Playing: 'Believer - Imagine Dragons'"

# 🚗 SmartCar inherits both
class SmartCar(GPS, MusicSystem):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_info(self):
        return f"🚗 {self.brand} {self.model}"
# Create object
car = SmartCar("Hyundai", "Venue")

# Call methods
print(car.show_info())
print(car.show_location())
print(car.play_music())
