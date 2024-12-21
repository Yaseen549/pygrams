from datetime import datetime, timedelta
import hashlib


def days_between(date1, date2):
    """
    Calculates the number of days between two dates.

    Parameters:
    ----------
    date1 : str or datetime
        The first date.
    date2 : str or datetime
        The second date.

    Returns:
    -------
    int
        The number of days between the two dates.

    Raises:
    ------
    ValueError
        If either of the dates cannot be parsed.
    TypeError
        If the inputs are not strings or datetime objects.

    Examples:
    --------
    >>> days_between("2024-12-01", "2024-12-12")
    11

    >>> days_between(datetime(2024, 12, 1), datetime(2024, 12, 12))
    11
    """
    if not isinstance(date1, (str, datetime)) or not isinstance(date2, (str, datetime)):
        raise TypeError("Both dates must be strings or datetime objects.")
    
    # If dates are strings, convert them to datetime objects
    if isinstance(date1, str):
        date1 = datetime.strptime(date1, "%Y-%m-%d")
    if isinstance(date2, str):
        date2 = datetime.strptime(date2, "%Y-%m-%d")
    
    # Calculate and return the number of days between the two dates
    delta = date2 - date1
    return abs(delta.days)


def add_days(date, days):
    """
    Adds a specified number of days to a date.

    Parameters:
    ----------
    date : str or datetime
        The date to which days will be added.
    days : int
        The number of days to add to the date.

    Returns:
    -------
    datetime
        The new date after adding the specified number of days.

    Raises:
    ------
    ValueError
        If the number of days is not an integer.
    TypeError
        If the date is not a string or datetime object.

    Examples:
    --------
    >>> add_days("2024-12-01", 5)
    datetime(2024, 12, 6)

    >>> add_days(datetime(2024, 12, 1), 5)
    datetime(2024, 12, 6)
    """
    if not isinstance(date, (str, datetime)):
        raise TypeError("Input date must be a string or datetime object.")
    if not isinstance(days, int):
        raise ValueError("The number of days must be an integer.")
    
    # If date is a string, convert it to a datetime object
    if isinstance(date, str):
        date = datetime.strptime(date, "%Y-%m-%d")
    
    # Add the specified number of days to the date
    return date + timedelta(days=days)


def format_date(date, format):
    """
    Converts a date to a specific format.

    Parameters:
    ----------
    date : str or datetime
        The date to format.
    format : str
        The format to which the date will be converted.

    Returns:
    -------
    str
        The date formatted according to the specified format.

    Raises:
    ------
    ValueError
        If the date format is incorrect.
    TypeError
        If the date is not a string or datetime object.

    Examples:
    --------
    >>> format_date("2024-12-01", "%B %d, %Y")
    'December 01, 2024'

    >>> format_date(datetime(2024, 12, 1), "%d/%m/%Y")
    '01/12/2024'
    """
    if not isinstance(date, (str, datetime)):
        raise TypeError("Input date must be a string or datetime object.")
    
    # If date is a string, convert it to a datetime object
    if isinstance(date, str):
        date = datetime.strptime(date, "%Y-%m-%d")
    
    # Format the date according to the given format
    return date.strftime(format)


def is_weekend(date):
    """
    Checks if a date falls on a weekend (Saturday or Sunday).

    Parameters:
    ----------
    date : str or datetime
        The date to check.

    Returns:
    -------
    bool
        True if the date is a weekend, False otherwise.

    Raises:
    ------
    TypeError
        If the input is not a string or datetime object.

    Examples:
    --------
    >>> is_weekend("2024-12-07")
    True

    >>> is_weekend("2024-12-01")
    False
    """
    if not isinstance(date, (str, datetime)):
        raise TypeError("Input date must be a string or datetime object.")
    
    # If date is a string, convert it to a datetime object
    if isinstance(date, str):
        date = datetime.strptime(date, "%Y-%m-%d")
    
    # Check if the date is a weekend
    return date.weekday() >= 5  # 5 and 6 correspond to Saturday and Sunday


def generate_hash(data, algorithm='sha256'):
    """
    Generate a hash of the given input string using the specified algorithm.

    Parameters:
    ----------
    data : str
        The input string to be hashed.
    algorithm : str, optional
        The hash algorithm to use ('md5', 'sha256', etc.). Default is 'sha256'.

    Returns:
    -------
    str
        The resulting hash as a hexadecimal string.

    Examples:
    --------
    >>> generate_hash("hello", 'md5')
    '5d41402abc4b2a76b9719d911017c592'
    >>> generate_hash("hello", 'sha256')
    '2cf24dba5fb0a30e26e83b2ac5b9e29e1b1681e03bda6d1d64752c0f6c4d86f4'
    """
    try:
        # Create a hash object based on the algorithm
        hash_object = hashlib.new(algorithm)
        hash_object.update(data.encode('utf-8'))  # Update the hash object with the data
        return hash_object.hexdigest()  # Return the hex representation of the hash
    except ValueError:
        raise ValueError(f"Unsupported algorithm: {algorithm}")
