# unit_converter.py
print("1. Celsius to Fahrenheit\n2. Kilometers to Miles")
choice = input("Choose conversion: ")

if choice == "1":
    celsius = float(input("Enter Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F") 
elif choice == "2":
    km = float(input("Enter kilometers: "))
    miles = km * 0.621371
    print(f"{km} km = {miles} miles")
else:
    print("Invalid choice")
