# Heat index calculator
- Simple heat index calculator.
- Calculates heat index using percent relative humidity and ambient temperature.

# Calculation Process
## Constants
c1 = -42.379
c2 = 2.04901523
c3 = 10.14333127
c4 = -0.22475541
c5 = -6.83783 * 10 ** -3
c6 = -5.481717 * 10 ** -2
c7 = 1.22874 * 10 ** -3
c8 = 8.5282 * 10 ** -4
c9 = -1.99 * 10 ** -6

## Formula        
hi =  c1 + c2*t + c3*h + c4*t*h + c5*t*t + c6*h*h + c7*t*t*h + c8*t*h*h + c9*t*t*h*h
where;
    h = relative_humidity
    t = celcius_temperature

## Refinement Logic
Pseudocode:
    IF (h < 13) and (80 <= t <= 112) THEN 
        SET hi TO hi - ((13 - h) / 4) * ((17 - abs(t - 95)) / 17) ^ 0.5
    
    IF (h > 85) and (80 <= t <= 87) THEN
        SET hi TO hi + ((h - 85) / 10) * ((87 - t) / 5)
    
    IF hi < 80 THEN
        SET hi TO (t + 61 + (t - 68) * 1.2 + h * 0.094) * 0.5

# References
https://www.wpc.ncep.noaa.gov/html/heatindex_equation.shtml
