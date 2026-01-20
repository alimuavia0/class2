num = float(input("Please enter temperature in number: "))
typ = input("Please enter temperature type (F or C): ").upper()

if typ == "F":
    # Input Fahrenheit → convert to Celsius
    rst = (num - 32) * 5 / 9
    print("Temperature in Celsius:", round(rst, 2))

elif typ == "C":
    # Input Celsius → convert to Fahrenheit
    rst = (num * 9 / 5) + 32
    print("Temperature in Fahrenheit:", round(rst, 2))

else:
    print("Something went wrong! Please enter C or F")
