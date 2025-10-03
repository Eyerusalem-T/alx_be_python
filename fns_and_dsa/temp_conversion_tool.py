# === ✅ Definition of Global Conversion Factors ===
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9     # Factor for converting Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5     # Factor for converting Celsius to Fahrenheit



# === ✅ Implementation of Conversion Functions ===
def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global conversion factor.
    """
    return (fahrenheit - FREEZING_POINT_FAHRENHEIT) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global conversion factor.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_FAHRENHEIT


# === ✅ User Interaction + Implementation of Value Error Handling ===
def main():
    """
    Handles user input, conversion selection, and displays the result.
    """
    try:
        # User enters a number (may raise ValueError if not numeric)
        temperature = float(input("Enter the temperature to convert: "))
        
        # User chooses C or F
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Perform conversion based on unit
        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    # === ✅ Implementation of ValueError Handling ===
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")


# Run the program
if __name__ == "__main__":
    main()
