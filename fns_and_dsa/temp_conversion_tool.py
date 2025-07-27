FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5

def convert_to_celsius(fahrenheit):
  """ 
  Converts a temprature from Fahrenheit to Celsius
  """
  celsius=(fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
  return celsius

def convert_to_fahrenheit(celsius):
  """ 
  Converts a temprature from Celsius to Fahrenheit
  """
  fahrenheit=(celsius*CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
  return fahrenheit

def main ():
  """ 
  Thia function prompts the user to input temperature and 
  does conversations
  """
  while True:
    temp_input_str= input("Enter the temperature to convert: ")
    
    try:
      temperature_value= float(temp_input_str)
    except ValueError:
      print("Invalid temperature. Please enter a numeric vaule.")
      continue
    unit_choice= input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    if unit_choice == "F":
      converted_temperature=convert_to_celsius(temperature_value)
      print(f"{temperature_value} Fahrenheit is {converted_temperature} Celsius")
      break
    elif unit_choice == "C":
      converted_temperature=convert_to_fahrenheit(temperature_value)
      print(f"{temperature_value} Celsius is {converted_temperature} Fahrenheit")
    else:
      print("Invalid unit. Please enter C for celsius or F for fahrenheit")

if __name__ == "__main__":
    main()
