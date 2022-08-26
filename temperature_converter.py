#Temperature converter

#Celcius to Fahrenheit
def celcius_to_fahrenheit():
    temperature = int(input("Enter the number of temperature : "))
    c_converter = (temperature * 9 / 5) + 32
    result = "{:.1f}".format(c_converter)
    print(f"The temperature is {result} fahrenheit.")

#Fahrenheit to celcius
def fahrenheit_to_celcius():
    temperature = int(input("Enter the number of temperature : "))
    f_converter = (temperature - 32)  * 5 / 9
    result = "{:.1f}".format(f_converter)
    print(f"The temperature is {result} celcius.")

#Start Program
print("Select the choices")

#condition control
while True: 
  try:
    print("(1) Celcius to Farenheit (2) Fahrenheit to Celcius")
    choices = int(input("Choice No. : "))
    if choices == 1:
        celcius_to_fahrenheit()
        break
    elif choices == 2:
        fahrenheit_to_celcius()
        break
    else:
        print("Please select the valid choice.") 
  except ValueError:
        print("Invalid Value. Please select a choice again.")
