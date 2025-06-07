FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celcius):
    return celcius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))
    except ValueError:
        raise ValueError ("Invalid input, please enter a numeric value")
    
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'C':
        unitConverted = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {unitConverted}°F")
    elif unit == 'F':
        unitConverted = convert_to_celsius(temperature)
        print(f"{temperature}°F is {unitConverted}°C")
    else:
        print(f"Invalid input. Please enter 'F' to convert to fahrenheit or 'C' to convert to celcius")

if __name__ == "__main__":
    main()