# === Definition of Global Conversion Factors ===
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9   # Factor for converting Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5   # Factor for converting Celsius to Fahrenheit
FREEZING_POINT_FAHRENHEIT = 32         # Freezing point of water in Fahrenheit


# === Implementation of Conversion Functions ===
def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global conversion factor.

    Args:
        fahrenheit (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature converted to Celsius.
    """
    return (fahrenheit - FREEZING_POINT_FAHRENHEIT) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global conversion factor.

    Args:
        celsius (float): Temperature in Celsius.

    Returns:
        float: Temperature converted to Fahrenheit.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_FAHRENHEIT


# === User Interaction with Error Handling ===
def main():
    """
    Main function to handle user interaction for temperature conversion.
    Prompts user for temperature and unit, performs conversion, and displays the result.
    """
    try:
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")


# Run program
if __name__ == "__main__":
    main()
