from datetime import datetime, timedelta
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


def get_day_of_week(date):
    """
    Gets the day of the week from a given date.

    Parameters:
    ----------
    date : str or datetime.date
        The date to get the day of the week from. It can be a string in the format 'YYYY-MM-DD' or a datetime.date object.

    Returns:
    -------
    str
        The name of the day of the week (e.g., 'Monday', 'Tuesday').

    Examples:
    --------
    >>> get_day_of_week('2024-12-21')
    'Saturday'
    >>> get_day_of_week(datetime.date(2024, 12, 21))
    'Saturday'
    """
    if isinstance(date, str):
        date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    return date.strftime('%A')


def add_hours_to_time(time, hours):
    """
    Adds a specific number of hours to a given time.

    Parameters:
    ----------
    time : str or datetime.datetime
        The initial time to which hours will be added. It can be a string in the format 'HH:MM:SS' or a datetime.datetime object.
    hours : int or float
        The number of hours to add.

    Returns:
    -------
    str
        The new time after adding the specified hours in 'HH:MM:SS' format.

    Examples:
    --------
    >>> add_hours_to_time('12:30:00', 2)
    '14:30:00'
    >>> add_hours_to_time(datetime.strptime('12:30:00', '%H:%M:%S'), 2)
    '14:30:00'
    """
    if isinstance(time, str):
        time = datetime.strptime(time, '%H:%M:%S')
    new_time = time + timedelta(hours=hours)
    return new_time.strftime('%H:%M:%S')


def format_duration(seconds):
    """
    Formats a duration given in seconds into hours, minutes, and seconds.

    Parameters:
    ----------
    seconds : int
        The duration in seconds to format.

    Returns:
    -------
    str
        The formatted duration as 'HH:MM:SS'.

    Examples:
    --------
    >>> format_duration(3661)
    '01:01:01'
    >>> format_duration(7325)
    '02:02:05'
    """
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f'{hours:02}:{minutes:02}:{seconds:02}'

