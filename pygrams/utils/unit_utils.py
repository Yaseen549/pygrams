def convert_to_bit(value, unit="byte"):
    """
    Converts a given value to bits.

    Parameters:
    ----------
    value : float
        The numerical value to convert.
    unit : str, optional
        The unit of the input value (default is "byte"). Supported units: "byte", "kilobyte", "megabyte", "gigabyte", "terabyte".

    Returns:
    -------
    float
        The value converted to bits.

    Raises:
    ------
    ValueError
        If the unit is not supported.

    Examples:
    --------
    >>> convert_to_bit(1, "byte")
    8.0
    >>> convert_to_bit(1, "kilobyte")
    8192.0
    """
    units_to_bits = {
        "byte": 8,
        "kilobyte": 8 * 1024,
        "megabyte": 8 * 1024**2,
        "gigabyte": 8 * 1024**3,
        "terabyte": 8 * 1024**4,
        "petabyte": 8 * 1024**5,
        "exabyte": 8 * 1024**6,
        "zettabyte": 8 * 1024**7,
        "yottabyte": 8 * 1024**8,
    }

    if unit not in units_to_bits:
        raise ValueError(f"Unsupported unit: {unit}. Supported units: {', '.join(units_to_bits.keys())}")

    return value * units_to_bits[unit]


def convert_to_byte(value, unit="bit"):
    """
    Converts a given value to bytes.

    Parameters:
    ----------
    value : float
        The numerical value to convert.
    unit : str, optional
        The unit of the input value (default is "bit"). Supported units: "bit", "kilobyte", "megabyte", "gigabyte", "terabyte".

    Returns:
    -------
    float
        The value converted to bytes.

    Raises:
    ------
    ValueError
        If the unit is not supported.

    Examples:
    --------
    >>> convert_to_byte(8, "bit")
    1.0
    >>> convert_to_byte(1, "kilobyte")
    1024.0
    """
    units_to_bytes = {
        "bit": 1 / 8,
        "kilobyte": 1024,
        "megabyte": 1024**2,
        "gigabyte": 1024**3,
        "terabyte": 1024**4,
        "petabyte": 1024**5,
        "exabyte": 1024**6,
        "zettabyte": 1024**7,
        "yottabyte": 1024**8,
    }

    if unit not in units_to_bytes:
        raise ValueError(f"Unsupported unit: {unit}. Supported units: {', '.join(units_to_bytes.keys())}")

    return value * units_to_bytes[unit]


def convert_to_kilobyte(value, unit="byte"):
    """
    Converts a given value to kilobytes.

    Parameters:
    ----------
    value : float
        The numerical value to convert.
    unit : str, optional
        The unit of the input value (default is "byte"). Supported units: "bit", "byte", "megabyte", "gigabyte", "terabyte".

    Returns:
    -------
    float
        The value converted to kilobytes.

    Raises:
    ------
    ValueError
        If the unit is not supported.

    Examples:
    --------
    >>> convert_to_kilobyte(1024, "byte")
    1.0
    >>> convert_to_kilobyte(1, "megabyte")
    1024.0
    """
    units_to_kilobytes = {
        "bit": 1 / (8 * 1024),
        "byte": 1 / 1024,
        "megabyte": 1024,
        "gigabyte": 1024**2,
        "terabyte": 1024**3,
        "petabyte": 1024**4,
        "exabyte": 1024**5,
        "zettabyte": 1024**6,
        "yottabyte": 1024**7,
    }

    if unit not in units_to_kilobytes:
        raise ValueError(f"Unsupported unit: {unit}. Supported units: {', '.join(units_to_kilobytes.keys())}")

    return value * units_to_kilobytes[unit]


def convert_to_megabyte(value, unit="byte"):
    """
    Converts a given value to megabytes.

    Parameters:
    ----------
    value : float
        The numerical value to convert.
    unit : str, optional
        The unit of the input value (default is "byte"). Supported units: "bit", "byte", "kilobyte", "gigabyte", "terabyte".

    Returns:
    -------
    float
        The value converted to megabytes.

    Raises:
    ------
    ValueError
        If the unit is not supported.

    Examples:
    --------
    >>> convert_to_megabyte(1048576, "byte")
    1.0
    >>> convert_to_megabyte(1, "gigabyte")
    1024.0
    """
    units_to_megabytes = {
        "bit": 1 / (8 * 1024**2),
        "byte": 1 / 1024**2,
        "kilobyte": 1 / 1024,
        "gigabyte": 1024,
        "terabyte": 1024**2,
        "petabyte": 1024**3,
        "exabyte": 1024**4,
        "zettabyte": 1024**5,
        "yottabyte": 1024**6,
    }

    if unit not in units_to_megabytes:
        raise ValueError(f"Unsupported unit: {unit}. Supported units: {', '.join(units_to_megabytes.keys())}")

    return value * units_to_megabytes[unit]


def convert_to_gigabyte(value, unit="byte"):
    """
    Converts a given value to gigabytes.

    Parameters:
    ----------
    value : float
        The numerical value to convert.
    unit : str, optional
        The unit of the input value (default is "byte"). Supported units: "bit", "byte", "kilobyte", "megabyte", "terabyte".

    Returns:
    -------
    float
        The value converted to gigabytes.

    Raises:
    ------
    ValueError
        If the unit is not supported.

    Examples:
    --------
    >>> convert_to_gigabyte(1073741824, "byte")
    1.0
    >>> convert_to_gigabyte(1, "terabyte")
    1024.0
    """
    units_to_gigabytes = {
        "bit": 1 / (8 * 1024**3),
        "byte": 1 / 1024**3,
        "kilobyte": 1 / 1024**2,
        "megabyte": 1 / 1024,
        "terabyte": 1024,
        "petabyte": 1024**2,
        "exabyte": 1024**3,
        "zettabyte": 1024**4,
        "yottabyte": 1024**5,
    }

    if unit not in units_to_gigabytes:
        raise ValueError(f"Unsupported unit: {unit}. Supported units: {', '.join(units_to_gigabytes.keys())}")

    return value * units_to_gigabytes[unit]


def convert_to_terabyte(value, unit="byte"):
    """
    Converts a given value to terabytes.

    Parameters:
    ----------
    value : float
        The numerical value to convert.
    unit : str, optional
        The unit of the input value (default is "byte"). Supported units: "bit", "byte", "kilobyte", "megabyte", "gigabyte".

    Returns:
    -------
    float
        The value converted to terabytes.

    Raises:
    ------
    ValueError
        If the unit is not supported.

    Examples:
    --------
    >>> convert_to_terabyte(1099511627776, "byte")
    1.0
    >>> convert_to_terabyte(1024, "gigabyte")
    1.0
    """
    units_to_terabytes = {
        "bit": 1 / (8 * 1024**4),
        "byte": 1 / 1024**4,
        "kilobyte": 1 / 1024**3,
        "megabyte": 1 / 1024**2,
        "gigabyte": 1 / 1024,
        "petabyte": 1024,
        "exabyte": 1024**2,
        "zettabyte": 1024**3,
        "yottabyte": 1024**4,
    }

    if unit not in units_to_terabytes:
        raise ValueError(f"Unsupported unit: {unit}. Supported units: {', '.join(units_to_terabytes.keys())}")

    return value * units_to_terabytes[unit]


def convert_to_petabyte(value, unit="byte"):
    """
    Converts a given value to petabytes.

    Parameters:
    ----------
    value : float
        The numerical value to convert.
    unit : str, optional
        The unit of the input value (default is "byte"). Supported units: "bit", "byte", "kilobyte", "megabyte", "gigabyte", "terabyte".

    Returns:
    -------
    float
        The value converted to petabytes.

    Raises:
    ------
    ValueError
        If the unit is not supported.

    Examples:
    --------
    >>> convert_to_petabyte(1125899906842624, "byte")
    1.0
    >>> convert_to_petabyte(1024, "terabyte")
    1.0
    """
    units_to_petabytes = {
        "bit": 1 / (8 * 1024**5),
        "byte": 1 / 1024**5,
        "kilobyte": 1 / 1024**4,
        "megabyte": 1 / 1024**3,
        "gigabyte": 1 / 1024**2,
        "terabyte": 1 / 1024,
        "exabyte": 1024,
        "zettabyte": 1024**2,
        "yottabyte": 1024**3,
    }

    if unit not in units_to_petabytes:
        raise ValueError(f"Unsupported unit: {unit}. Supported units: {', '.join(units_to_petabytes.keys())}")

    return value * units_to_petabytes[unit]


def convert_to_exabyte(value, unit="byte"):
    """
    Converts a given value to exabytes.

    Parameters:
    ----------
    value : float
        The numerical value to convert.
    unit : str, optional
        The unit of the input value (default is "byte"). Supported units: "bit", "byte", "kilobyte", "megabyte", "gigabyte", "terabyte", "petabyte".

    Returns:
    -------
    float
        The value converted to exabytes.

    Raises:
    ------
    ValueError
        If the unit is not supported.

    Examples:
    --------
    >>> convert_to_exabyte(1_152_921_504_606_846_976, "byte")
    1.0
    >>> convert_to_exabyte(1024, "petabyte")
    1.0
    """
    units_to_exabytes = {
        "bit": 1 / (8 * 1024**6),
        "byte": 1 / 1024**6,
        "kilobyte": 1 / 1024**5,
        "megabyte": 1 / 1024**4,
        "gigabyte": 1 / 1024**3,
        "terabyte": 1 / 1024**2,
        "petabyte": 1 / 1024,
        "zettabyte": 1024,
        "yottabyte": 1024**2,
    }

    if unit not in units_to_exabytes:
        raise ValueError(f"Unsupported unit: {unit}. Supported units: {', '.join(units_to_exabytes.keys())}")

    return value * units_to_exabytes[unit]


def convert_to_zettabyte(value, unit="byte"):
    """
    Converts a given value to zettabytes.

    Parameters:
    ----------
    value : float
        The numerical value to convert.
    unit : str, optional
        The unit of the input value (default is "byte"). Supported units: "bit", "byte", "kilobyte", "megabyte", "gigabyte", "terabyte", "petabyte", "exabyte".

    Returns:
    -------
    float
        The value converted to zettabytes.

    Raises:
    ------
    ValueError
        If the unit is not supported.

    Examples:
    --------
    >>> convert_to_zettabyte(1_180_591_620_717_411_303_424, "byte")
    1.0
    >>> convert_to_zettabyte(1024, "exabyte")
    1.0
    """
    units_to_zettabytes = {
        "bit": 1 / (8 * 1024**7),
        "byte": 1 / 1024**7,
        "kilobyte": 1 / 1024**6,
        "megabyte": 1 / 1024**5,
        "gigabyte": 1 / 1024**4,
        "terabyte": 1 / 1024**3,
        "petabyte": 1 / 1024**2,
        "exabyte": 1 / 1024,
        "yottabyte": 1024,
    }

    if unit not in units_to_zettabytes:
        raise ValueError(f"Unsupported unit: {unit}. Supported units: {', '.join(units_to_zettabytes.keys())}")

    return value * units_to_zettabytes[unit]


def convert_to_yottabyte(value, unit="byte"):
    """
    Converts a given value to yottabytes.

    Parameters:
    ----------
    value : float
        The numerical value to convert.
    unit : str, optional
        The unit of the input value (default is "byte"). Supported units: "bit", "byte", "kilobyte", "megabyte", "gigabyte", "terabyte", "petabyte", "exabyte", "zettabyte".

    Returns:
    -------
    float
        The value converted to yottabytes.

    Raises:
    ------
    ValueError
        If the unit is not supported.

    Examples:
    --------
    >>> convert_to_yottabyte(1_208_925_819_614_629_174_706_176, "byte")
    1.0
    >>> convert_to_yottabyte(1024, "zettabyte")
    1.0
    """
    units_to_yottabytes = {
        "bit": 1 / (8 * 1024**8),
        "byte": 1 / 1024**8,
        "kilobyte": 1 / 1024**7,
        "megabyte": 1 / 1024**6,
        "gigabyte": 1 / 1024**5,
        "terabyte": 1 / 1024**4,
        "petabyte": 1 / 1024**3,
        "exabyte": 1 / 1024**2,
        "zettabyte": 1 / 1024,
    }

    if unit not in units_to_yottabytes:
        raise ValueError(f"Unsupported unit: {unit}. Supported units: {', '.join(units_to_yottabytes.keys())}")

    return value * units_to_yottabytes[unit]


def convert_to_celsius(value, unit="fahrenheit"):
    """
    Converts a given temperature value to Celsius.

    Parameters:
    ----------
    value : float
        The temperature value to convert.
    unit : str, optional
        The unit of the input value (default is "fahrenheit"). Supported units: "fahrenheit", "kelvin".

    Returns:
    -------
    float
        The value converted to Celsius.

    Raises:
    ------
    ValueError
        If the unit is not supported.

    Examples:
    --------
    >>> convert_to_celsius(32, "fahrenheit")
    0.0
    >>> convert_to_celsius(273.15, "kelvin")
    0.0
    """
    if unit == "fahrenheit":
        return (value - 32) * 5/9
    elif unit == "kelvin":
        return value - 273.15
    else:
        raise ValueError("Unsupported unit: {unit}. Supported units: fahrenheit, kelvin")


def convert_to_fahrenheit(value, unit="celsius"):
    """
    Converts a given temperature value to Fahrenheit.

    Parameters:
    ----------
    value : float
        The temperature value to convert.
    unit : str, optional
        The unit of the input value (default is "celsius"). Supported units: "celsius", "kelvin".

    Returns:
    -------
    float
        The value converted to Fahrenheit.

    Raises:
    ------
    ValueError
        If the unit is not supported.

    Examples:
    --------
    >>> convert_to_fahrenheit(0, "celsius")
    32.0
    >>> convert_to_fahrenheit(273.15, "kelvin")
    32.0
    """
    if unit == "celsius":
        return (value * 9/5) + 32
    elif unit == "kelvin":
        return (value - 273.15) * 9/5 + 32
    else:
        raise ValueError("Unsupported unit: {unit}. Supported units: celsius, kelvin")


def convert_to_kelvin(value, unit="celsius"):
    """
    Converts a given temperature value to Kelvin.

    Parameters:
    ----------
    value : float
        The temperature value to convert.
    unit : str, optional
        The unit of the input value (default is "celsius"). Supported units: "celsius", "fahrenheit".

    Returns:
    -------
    float
        The value converted to Kelvin.

    Raises:
    ------
    ValueError
        If the unit is not supported.

    Examples:
    --------
    >>> convert_to_kelvin(0, "celsius")
    273.15
    >>> convert_to_kelvin(32, "fahrenheit")
    273.15
    """
    if unit == "celsius":
        return value + 273.15
    elif unit == "fahrenheit":
        return (value - 32) * 5/9 + 273.15
    else:
        raise ValueError("Unsupported unit: {unit}. Supported units: celsius, fahrenheit")


def convert_to_inches(value, unit="meters"):
    """
    Converts a given value to inches.

    Parameters:
    ----------
    value : float
        The numerical value to convert.
    unit : str, optional
        The unit of the input value (default is "meters"). Supported units: "meters", "feet", "kilometers".

    Returns:
    -------
    float
        The value converted to inches.

    Raises:
    ------
    ValueError
        If the unit is not supported.

    Examples:
    --------
    >>> convert_to_inches(1, "meters")
    39.3701
    >>> convert_to_inches(1, "feet")
    12.0
    """
    units_to_inches = {
        "meters": 39.3701,
        "feet": 12.0,
        "kilometers": 39370.1,
    }

    if unit not in units_to_inches:
        raise ValueError(f"Unsupported unit: {unit}. Supported units: {', '.join(units_to_inches.keys())}")

    return value * units_to_inches[unit]


def convert_to_feet(value, unit="meters"):
    """
    Converts a given value to feet.

    Parameters:
    ----------
    value : float
        The numerical value to convert.
    unit : str, optional
        The unit of the input value (default is "meters"). Supported units: "meters", "inches", "kilometers".

    Returns:
    -------
    float
        The value converted to feet.

    Raises:
    ------
    ValueError
        If the unit is not supported.

    Examples:
    --------
    >>> convert_to_feet(1, "meters")
    3.28084
    >>> convert_to_feet(12, "inches")
    1.0
    """
    units_to_feet = {
        "meters": 3.28084,
        "inches": 1 / 12.0,
        "kilometers": 3280.84,
    }

    if unit not in units_to_feet:
        raise ValueError(f"Unsupported unit: {unit}. Supported units: {', '.join(units_to_feet.keys())}")

    return value * units_to_feet[unit]


def convert_to_centimeters(meters):
    """
    Converts a given value in meters to centimeters.

    Parameters:
    ----------
    meters : float or int
        The value in meters to be converted.

    Returns:
    -------
    float
        The equivalent value in centimeters.

    Raises:
    ------
    TypeError
        If the input is not a number.

    Examples:
    --------
    >>> convert_to_centimeters(1)
    100.0
    >>> convert_to_centimeters(0.5)
    50.0
    """
    if not isinstance(meters, (int, float)):
        raise TypeError("meters must be a number.")
    return meters * 100


def convert_to_meters(value, unit="inches"):
    """
    Converts a given value to meters.

    Parameters:
    ----------
    value : float
        The numerical value to convert.
    unit : str, optional
        The unit of the input value (default is "inches"). Supported units: "inches", "feet", "kilometers".

    Returns:
    -------
    float
        The value converted to meters.

    Raises:
    ------
    ValueError
        If the unit is not supported.

    Examples:
    --------
    >>> convert_to_meters(39.3701, "inches")
    1.0
    >>> convert_to_meters(3.28084, "feet")
    1.0
    """
    units_to_meters = {
        "inches": 1 / 39.3701,
        "feet": 1 / 3.28084,
        "kilometers": 1000.0,
    }

    if unit not in units_to_meters:
        raise ValueError(f"Unsupported unit: {unit}. Supported units: {', '.join(units_to_meters.keys())}")

    return value * units_to_meters[unit]


def convert_to_kilometers(meters):
    """
    Converts a given value in meters to kilometers.

    Parameters:
    ----------
    meters : float or int
        The value in meters to be converted.

    Returns:
    -------
    float
        The equivalent value in kilometers.

    Raises:
    ------
    TypeError
        If the input is not a number.

    Examples:
    --------
    >>> convert_to_kilometers(1000)
    1.0
    >>> convert_to_kilometers(500)
    0.5
    """
    if not isinstance(meters, (int, float)):
        raise TypeError("meters must be a number.")
    return meters / 1000


def convert_to_miles(meters):
    """
    Converts a given value in meters to miles.

    Parameters:
    ----------
    meters : float or int
        The value in meters to be converted.

    Returns:
    -------
    float
        The equivalent value in miles.

    Raises:
    ------
    TypeError
        If the input is not a number.

    Examples:
    --------
    >>> convert_to_miles(1609.34)
    1.0
    >>> convert_to_miles(800)
    0.4971
    """
    if not isinstance(meters, (int, float)):
        raise TypeError("meters must be a number.")
    return meters / 1609.34


def convert_to_seconds(time_value, time_unit):
    """
    Convert time value in hours, minutes, or days to seconds.

    Parameters:
    ----------
    time_value : float or int
        The value to be converted.
    time_unit : str
        The unit of time ('hours', 'minutes', or 'days').

    Returns:
    -------
    float
        The equivalent value in seconds.

    Raises:
    ------
    ValueError
        If the time unit is not 'hours', 'minutes', or 'days'.

    Examples:
    --------
    >>> convert_to_seconds(1, 'hours')
    3600.0
    >>> convert_to_seconds(30, 'minutes')
    1800.0
    >>> convert_to_seconds(2, 'days')
    172800.0
    """
    if time_unit == 'hours':
        return time_value * 3600  # 1 hour = 3600 seconds
    elif time_unit == 'minutes':
        return time_value * 60  # 1 minute = 60 seconds
    elif time_unit == 'days':
        return time_value * 86400  # 1 day = 86400 seconds
    else:
        raise ValueError("Invalid time unit. Please use 'hours', 'minutes', or 'days'.")


def convert_to_minutes(time_value, time_unit):
    """
    Convert time value in seconds, hours, or days to minutes.

    Parameters:
    ----------
    time_value : float or int
        The value to be converted.
    time_unit : str
        The unit of time ('seconds', 'hours', or 'days').

    Returns:
    -------
    float
        The equivalent value in minutes.

    Raises:
    ------
    ValueError
        If the time unit is not 'seconds', 'hours', or 'days'.

    Examples:
    --------
    >>> convert_to_minutes(3600, 'seconds')
    60.0
    >>> convert_to_minutes(2, 'hours')
    120.0
    >>> convert_to_minutes(1, 'days')
    1440.0
    """
    if time_unit == 'seconds':
        return time_value / 60  # 1 minute = 60 seconds
    elif time_unit == 'hours':
        return time_value * 60  # 1 hour = 60 minutes
    elif time_unit == 'days':
        return time_value * 1440  # 1 day = 1440 minutes
    else:
        raise ValueError("Invalid time unit. Please use 'seconds', 'hours', or 'days'.")


def convert_to_hours(time_value, time_unit):
    """
    Convert time value in seconds, minutes, or days to hours.

    Parameters:
    ----------
    time_value : float or int
        The value to be converted.
    time_unit : str
        The unit of time ('seconds', 'minutes', or 'days').

    Returns:
    -------
    float
        The equivalent value in hours.

    Raises:
    ------
    ValueError
        If the time unit is not 'seconds', 'minutes', or 'days'.

    Examples:
    --------
    >>> convert_to_hours(3600, 'seconds')
    1.0
    >>> convert_to_hours(120, 'minutes')
    2.0
    >>> convert_to_hours(1, 'days')
    24.0
    """
    if time_unit == 'seconds':
        return time_value / 3600  # 1 hour = 3600 seconds
    elif time_unit == 'minutes':
        return time_value / 60  # 1 hour = 60 minutes
    elif time_unit == 'days':
        return time_value * 24  # 1 day = 24 hours
    else:
        raise ValueError("Invalid time unit. Please use 'seconds', 'minutes', or 'days'.")


def convert_to_days(time_value, time_unit):
    """
    Convert time value in seconds, minutes, or hours to days.

    Parameters:
    ----------
    time_value : float or int
        The value to be converted.
    time_unit : str
        The unit of time ('seconds', 'minutes', or 'hours').

    Returns:
    -------
    float
        The equivalent value in days.

    Raises:
    ------
    ValueError
        If the time unit is not 'seconds', 'minutes', or 'hours'.

    Examples:
    --------
    >>> convert_to_days(86400, 'seconds')
    1.0
    >>> convert_to_days(1440, 'minutes')
    1.0
    >>> convert_to_days(24, 'hours')
    1.0
    """
    if time_unit == 'seconds':
        return time_value / 86400  # 1 day = 86400 seconds
    elif time_unit == 'minutes':
        return time_value / 1440  # 1 day = 1440 minutes
    elif time_unit == 'hours':
        return time_value / 24  # 1 day = 24 hours
    else:
        raise ValueError("Invalid time unit. Please use 'seconds', 'minutes', or 'hours'.")


def convert_to_months(time_value, time_unit):
    """
    Convert time value in days or years to months.

    Parameters:
    ----------
    time_value : float or int
        The value to be converted.
    time_unit : str
        The unit of time ('days' or 'years').

    Returns:
    -------
    float
        The equivalent value in months.

    Raises:
    ------
    ValueError
        If the time unit is not 'days' or 'years'.

    Examples:
    --------
    >>> convert_to_months(30, 'days')
    1.0
    >>> convert_to_months(1, 'years')
    12.0
    """
    if time_unit == 'days':
        return time_value / 30  # 1 month = ~30 days (approximation)
    elif time_unit == 'years':
        return time_value * 12  # 1 year = 12 months
    else:
        raise ValueError("Invalid time unit. Please use 'days' or 'years'.")


def convert_to_years(time_value, time_unit):
    """
    Convert time value in days, months, or hours to years.

    Parameters:
    ----------
    time_value : float or int
        The value to be converted.
    time_unit : str
        The unit of time ('days', 'months', or 'hours').

    Returns:
    -------
    float
        The equivalent value in years.

    Raises:
    ------
    ValueError
        If the time unit is not 'days', 'months', or 'hours'.

    Examples:
    --------
    >>> convert_to_years(365, 'days')
    1.0
    >>> convert_to_years(12, 'months')
    1.0
    >>> convert_to_years(8760, 'hours')
    1.0
    """
    if time_unit == 'days':
        return time_value / 365  # 1 year = 365 days
    elif time_unit == 'months':
        return time_value / 12  # 1 year = 12 months
    elif time_unit == 'hours':
        return time_value / 8760  # 1 year = 8760 hours (365 days * 24 hours)
    else:
        raise ValueError("Invalid time unit. Please use 'days', 'months', or 'hours'.")


def convert_to_liters(volume_value, volume_unit):
    """
    Convert volume value in various units (gallons, quarts, cups) to liters.

    Parameters:
    ----------
    volume_value : float or int
        The value to be converted.
    volume_unit : str
        The unit of volume ('gallons', 'quarts', 'cups').

    Returns:
    -------
    float
        The equivalent value in liters.

    Raises:
    ------
    ValueError
        If the volume unit is not 'gallons', 'quarts', or 'cups'.

    Examples:
    --------
    >>> convert_to_liters(1, 'gallons')
    3.78541
    >>> convert_to_liters(2, 'quarts')
    1.892705
    >>> convert_to_liters(4, 'cups')
    0.9463525
    """
    if volume_unit == 'gallons':
        return volume_value * 3.78541  # 1 gallon = 3.78541 liters
    elif volume_unit == 'quarts':
        return volume_value * 0.946352  # 1 quart = 0.946352 liters
    elif volume_unit == 'cups':
        return volume_value * 0.236588  # 1 cup = 0.236588 liters
    else:
        raise ValueError("Invalid volume unit. Please use 'gallons', 'quarts', or 'cups'.")

