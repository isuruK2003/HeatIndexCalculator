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

hi =  c1 + c2*t + c3*h + c4*t*h + c5*t*t + c6*h*h + c7*t*t*h + c8*t*h*h + c9*t*t*h*h

