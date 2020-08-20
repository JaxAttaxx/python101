#Celsius_D = input('Can you give the Degrees in Celsius please?')


while True:
    try:
        Celsius_D = float(input('Can you give the Degrees in Celsius please?'))
        Fahrenheit_D = (Celsius_D) * (9/5) +32
        Fahrenheit_D_str = str(Fahrenheit_D) + ' F'

        print(Fahrenheit_D_str)
        break
    except ValueError:
        print('Please try in numerals...' )
        
#Fahrenheit_D = float(Celsius_D) * (9/5) +32
#Fahrenheit_D_str = str(Fahrenheit_D) + ' F'

#print(Fahrenheit_D_str)