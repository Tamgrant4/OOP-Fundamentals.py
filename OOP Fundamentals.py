# Q1 Task 1

class Vehicle:
  def __init__(self, reg_num, type, owner):
    self.registration_number = reg_num
    self.type = type
    self.owner = owner

  def update_owner(self, new_owner):
    self.owner = new_owner

# Create a few Vehicle objects
car = Vehicle("ABC123", "Car", "John Doe")
bike = Vehicle("DEF456", "Motorcycle", "Jane Smith")

# Print the initial owners
print(f"Car owner: {car.owner}")
print(f"Bike owner: {bike.owner}")

# Update the owners
car.update_owner("Mary Brown")
bike.update_owner("David Miller")

# Print the updated owners
print(f"\nCar owner (after update): {car.owner}")
print(f"Bike owner (after update): {bike.owner}")

# TAsk 2

class Event:
  def __init__(self, name, date):
    self.name = name
    self.date = date
    self.participant_count = 0  # Initialize participant count to 0

  def add_participant(self):
    self.participant_count += 1  # Increase participant count by 1

  def get_participant_count(self):
    return self.participant_count  # Return current participant count

#  Q 2 Task 1

class Building:
  def __init__(self, name, floors):
    self.name = name
    self.floors = floors

  def save_to_file(self, filename):
    """Saves building details to a text file."""
    with open(filename, 'w') as file:
      file.write(f"{self.name},{self.floors}\n")

  @classmethod
  def load_from_file(cls, filename):
    """Loads building details from a text file and returns a list of Building objects."""
    buildings = []
    with open(filename, 'r') as file:
      for line in file:
        name, floors = line.strip().split(',')
        buildings.append(cls(name, int(floors)))  # Create Building objects
    return buildings

# Example usage
building1 = Building("City Hall", 10)
building2 = Building("Library", 3)

# Save buildings to a file
building1.save_to_file("buildings.txt")
building2.save_to_file("buildings.txt", mode='a')  # Append mode for multiple buildings

# Simulate loading from file (without actually reading again here)
loaded_buildings = Building.load_from_file("buildings.txt")

for building in loaded_buildings:
  print(f"Building Name: {building.name}, Floors: {building.floors}")


# Q3 Task1 


class Bus:
  """Represents a public transportation bus."""
  CITY_NAME = "Anytown"  # Class variable (common for all buses)
  BASE_FARE = 2.50  # Class variable (common for all buses)

  def __init__(self, route_number, capacity):
    self.route_number = route_number  # Instance variable
    self.capacity = capacity  # Instance variable

from public_transport import Bus

# Create bus instances
bus1 = Bus(101, 50)
bus2 = Bus(202, 75)

# Access class variables
print(f"City Name (class variable): {Bus.CITY_NAME}")
print(f"Base Fare (class variable): ${Bus.BASE_FARE:.2f}")

# Access instance variables
print(f"\nBus 1 Route Number: {bus1.route_number}")
print(f"Bus 1 Passenger Capacity: {bus1.capacity}")

print(f"\nBus 2 Route Number: {bus2.route_number}")
print(f"Bus 2 Passenger Capacity: {bus2.capacity}")

