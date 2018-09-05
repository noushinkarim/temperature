def kelvin_to_celsius(temp):
    """
    connvert T from K to C
    """
    return temp - 273.15

def celsius_to_fahr(temp):
    """
    convert T from C to F
    """
    return temp * (9/5) + 32


def kelvin_to_fahr(temp):
    """
    convert  from  K to  F
    """
    temp_c = kelvin_to_celsius(temp)
    result = celsius_to_fahr(temp_c)
    return result
