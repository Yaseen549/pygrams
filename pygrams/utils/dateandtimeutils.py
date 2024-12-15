from datetime import datetime
from dateutil.relativedelta import relativedelta

def days_until(date):
    """
    Returns the number of days until a specified future date.

    Parameters:
    ----------
    date : datetime
        A future date to compare with the current date.

    Returns:
    -------
    int
        The number of days remaining until the specified date.

    Raises:
    ------
    TypeError
        If the input is not a datetime object.

    Examples:
    --------
    >>> days_until(datetime(2025, 1, 1))
    365

    >>> days_until(datetime(2024, 12, 25))
    13
    """
    if not isinstance(date, datetime):
        raise TypeError("Input must be a datetime object.")
    
    today = datetime.now()
    delta = date - today
    return delta.days


def add_months_to_date(date, months):
    """
    Adds a specified number of months to a date.

    Parameters:
    ----------
    date : datetime
        The date to which months will be added.
    months : int
        The number of months to add.

    Returns:
    -------
    datetime
        The new date after adding the specified number of months.

    Raises:
    ------
    TypeError
        If the date is not a datetime object or months is not an integer.

    Examples:
    --------
    >>> add_months_to_date(datetime(2024, 12, 12), 2)
    datetime.datetime(2025, 2, 12, 0, 0)

    >>> add_months_to_date(datetime(2024, 1, 1), -1)
    datetime.datetime(2023, 12, 1, 0, 0)
    """
    if not isinstance(date, datetime):
        raise TypeError("Input date must be a datetime object.")
    if not isinstance(months, int):
        raise TypeError("Months must be an integer.")
    
    return date + relativedelta(months=months)
