# HVAC Analysis

This repository holds various analysis related to HVAC.

Includes:

- Spreadsheet cooling coil model
  (`cooling_coil_heat_exchanger_analysis.xlsx`). This is a cooling coil
  model based on the work by Elmahdy and Mitalas, also employed in
  EnergyPlus.

- `SolAirTemperatureCalculations.xlsx`. Spreadsheet of sol-air temperature calculations for a building in College Station, TX.

- `slr_test_data.txt`: Test data from [Wikipedia](https://en.wikipedia.org/wiki/Simple_linear_regression)
  - Result: Slope: 61.272 Constant: -39.062

- `sat_h.xlim` and `sat_h.xlsx`: Exploration of linear approximations to saturated enthalpy at standard atmospheric pressure.
  Approximations are very useful if used over the range of temperatures for condenser water return temperature, as this makes the solution for the Braun cooling tower model explicit.

- `wang_derivative.maxima`: Derivative of the Wang chiller regression form vs. condenser water return temperature.
