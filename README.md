# Heat Index Calculator
- Simple heat index calculator.
- Calculates the heat index using percent relative humidity and ambient temperature.

## Calculation Process
### Constants
- c1 = -42.379
- c2 = 2.04901523
- c3 = 10.14333127
- c4 = -0.22475541
- c5 = -6.83783 * 10 ** -3
- c6 = -5.481717 * 10 ** -2
- c7 = 1.22874 * 10 ** -3
- c8 = 8.5282 * 10 ** -4
- c9 = -1.99 * 10 ** -6
## Formula
```
hi =  c1 + c2*t + c3*h + c4*t*h + c5*t*t + c6*h*h + c7*t*t*h + c8*t*h*h + c9*t*t*h*h
```
where "hi" is heat index and "t" and "h" are ambient temperature and percent relative humidity respectively.
# Refinement Logic
Pseudocode:
```
IF (h < 13) and (80 <= t <= 112) THEN
    hi = hi - ((13 - h) / 4) * ((17 - abs(t - 95)) / 17) ^ 0.5
END IF
    
IF (h > 85) and (80 <= t <= 87) THEN
    hi = hi + ((h - 85) / 10) * ((87 - t) / 5)
END IF
    
IF hi < 80 THEN
    hi = (t + 61 + (t - 68) * 1.2 + h * 0.094) * 0.5
END IF
```
# References
NOAA Heat Index Equation: https://www.wpc.ncep.noaa.gov/html/heatindex_equation.shtml
