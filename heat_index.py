def get_float_input(message, error_message='Please enter a numerical value'):
    while True:
        try:
            value = float(input(message))
        except ValueError:
            print(error_message)
        else:
            return value

def get_relative_humidity():
    while True:
        humidity = get_float_input('>>> Enter percent relative humidity: ')
        if 0 <= humidity <= 100:
            return humidity
        print('>>> Humidity should be with in the range of 0 t 100.')


def get_temperature():
    while True:
        temperature = get_float_input('>>> Enter the temperature in celcius: ')
        if temperature > -273.15:
            return temperature
        else:
            print('*** Invalid Temperature ***')

def convert_to_farenheit(celcius):
    return celcius * (9/5) + 32

def calculate_hi(celcius_temperature, relative_humidity):
    h = relative_humidity
    t = celcius_temperature

    t = convert_to_farenheit(t) # Converting to Farenheit

    # Constants
    c1 = -42.379
    c2 = 2.04901523
    c3 = 10.14333127
    c4 = -0.22475541
    c5 = -6.83783 * 10 ** -3
    c6 = -5.481717 * 10 ** -2
    c7 = 1.22874 * 10 ** -3
    c8 = 8.5282 * 10 ** -4
    c9 = -1.99 * 10 ** -6

    # Formula
    hi =  c1 + c2*t + c3*h + c4*t*h + c5*t*t + c6*h*h + c7*t*t*h + c8*t*h*h + c9*t*t*h*h

    if h < 13 and 80 <= t <= 112:
        hi -= ((13 - h) / 4) * ((17 - abs(t - 95)) / 17) ** 0.5
    
    if h > 85 and 80 <= t <= 87:
        hi += ((h - 85) / 10) * ((87 - t) / 5)
    
    if hi < 80:
        hi = (t + 61 + (t - 68) * 1.2 + h * 0.094) * 0.5

    return round((hi -32) * (5 / 9), 3)

if __name__ == '__main__':
    try:
        relative_humidity = get_relative_humidity()
        temperature = get_temperature()
        print('--- Temperature in Farenheit:', convert_to_farenheit(temperature), '°F ---')
        hi = calculate_hi(temperature, relative_humidity)
        print('--- Heat Index: ',hi, '°C ---')
    except KeyboardInterrupt:
        print('\nExit')

# created according to: https://www.wpc.ncep.noaa.gov/html/heatindex_equation.shtml