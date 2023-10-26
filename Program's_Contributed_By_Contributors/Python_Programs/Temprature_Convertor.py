def convert_temperature(temperature, from_scale, to_scale):
  """Converts a temperature from one scale to another.

  Args:
    temperature: The temperature to convert.
    from_scale: The scale of the temperature to convert from.
    to_scale: The scale of the temperature to convert to.

  Returns:
    The converted temperature.
  """

  if from_scale == "Celsius" and to_scale == "Fahrenheit":
    return (temperature * 9 / 5) + 32
  elif from_scale == "Fahrenheit" and to_scale == "Celsius":
    return (temperature - 32) * 5 / 9
  else:
    raise ValueError("Invalid temperature scales.")

if __name__ == "__main__":
  temperature = float(input("Enter the temperature: "))
  from_scale = input("Enter the from scale (Celsius or Fahrenheit): ")
  to_scale = input("Enter the to scale (Celsius or Fahrenheit): ")

  print(convert_temperature(temperature, from_scale, to_scale))
