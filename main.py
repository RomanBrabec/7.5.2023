import json
import pickle

class Airplane:
    # Initialize an Address instance
    def __init__(self, numberPilots, numberEngines):
        self.numberPilots = numberPilots
        self.numberEngines = numberEngines


    # Define string representation of Address instance
    def __str__(self):
        return f"{self.numberEngines}{self.numberPilots}"

    # Convert the Address object to a dictionary
    def to_dict(self):
        return {
            "countPilots": self.numberPilots,
            "countEngines": self.numberEngines
        }

file_namePKL = 'letadlo.pkl'
file_nameJSON = 'letadlo.json'

def serializePkl(data):
    # Create a full file path
    path = file_namePKL
    # Open the file in write mode
    with open(path,"wb") as file:
        # Serialize and save data to the file
        pickle.dump(data, file)

# Define a function to load data from a file and deserialize it
def deserializePKL():
    # Create a full file path
    path = file_namePKL
    # Open the file in read mode
    with open(path, "rb") as file:
        # Load and deserialize data from the file
        data = pickle.load(file)
    # Return the deserialized data
    return data

def serializeJSON(data):
    # Create a full file path
    path = file_nameJSON
    # Open the file in write mode
    with open(path,"w") as file:
        # Serialize and save data to the file
        json.dump(data, file)

def deserializeJSON():
    # Create a full file path
    path = file_nameJSON
    # Open the file in read mode
    with open(path, "r") as file:
        # Load and deserialize data from the file
        data = json.load(file)
    # Return the deserialized data
    return data

# Define the Address class


# Create a Human instance
b747 = Airplane("43", "4")

print(serializePkl(b747))
print(deserializePKL())

print(serializeJSON(b747.to_dict()))
print(deserializeJSON())
# Serialize the Human instance to a JSON string
# serialized = json.dumps(b747.to_dict())
# print(f"Serialized object:\n\n{serialized}\n\n")
#
# # Deserialize the JSON string back into a dictionary
# deserialized = json.loads(serialized)
#
# # Create a new Human instance from the deserialized dictionary
# #second_obj = Human(deserialized["name"], deserialized["last_name"], Address(**deserialized["address"]))
#
# # Print the deserialized Human instance
# print(f"Deserialized object:\n\n{deserialized}")
