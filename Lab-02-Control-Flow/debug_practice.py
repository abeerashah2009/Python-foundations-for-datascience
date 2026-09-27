# Debug Practice - Corrected Version

# Error 1 fixed: Convert input to float
temperature = float(input("Enter temperature: "))
humidity = float(input("Enter humidity: "))

# Error 2 fixed: Added colon
# Error 3 fixed: Correct indentation
if temperature > 80:
    print("It's hot!")

if humidity > 70 and temperature > 85:
    print("Very uncomfortable weather")
elif humidity < 30 or temperature < 40:  # Error 4 fixed: Added colon
    print("Dry or cold conditions")

# Error 5 fixed: Conditions arranged from highest to lowest
if temperature > 100:
    print("Extremely hot")
elif temperature > 90:
    print("Very hot")

print("Program finished")
