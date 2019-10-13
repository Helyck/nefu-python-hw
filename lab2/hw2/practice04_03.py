def convert_fahr_to_cels(deg_fahr):
    """Convert a temperature given in degrees Fahrenheit to degrees Celcius."""
    return round(5 * (deg_fahr - 32)/9, 2)


def convert():
    """Ask the user for a temperature in degrees Fahrenheir, and print out the temperature in degrees Celsius."""

    s = input("Enter temperature in degrees Fahrenheir: ")
    f_deg = float(s)
    print(convert_fahr_to_cels(f_deg))


if __name__ == '__main__':
    convert()
