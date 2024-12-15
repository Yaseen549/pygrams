def generate_bar_chart(data):
    """
    Generates a basic ASCII bar chart.

    Parameters:
    ----------
    data : dict
        A dictionary where the keys are categories and the values are numbers representing the quantity.

    Returns:
    -------
    str
        A string representing the bar chart.

    Raises:
    ------
    TypeError
        If the input is not a dictionary.
    ValueError
        If the dictionary values are not numbers.

    Examples:
    --------
    >>> generate_bar_chart({"A": 5, "B": 3, "C": 8})
    'A | *****\nB | ***\nC | ********'

    >>> generate_bar_chart({"Apple": 10, "Banana": 7, "Cherry": 4})
    'Apple | **********\nBanana | *******\nCherry | ****'
    """
    if not isinstance(data, dict):
        raise TypeError("Input must be a dictionary.")
    
    chart = ""
    for category, value in data.items():
        if not isinstance(value, (int, float)):
            raise ValueError("All values in the dictionary must be numbers.")
        bar = '*' * int(value)
        chart += f"{category} | {bar}\n"
    
    return chart


def generate_pie_chart(data):
    """
    Creates an ASCII pie chart.

    Parameters:
    ----------
    data : dict
        A dictionary where the keys are categories and the values are numbers representing the proportions.

    Returns:
    -------
    str
        A string representing the pie chart.

    Raises:
    ------
    TypeError
        If the input is not a dictionary.
    ValueError
        If the dictionary values are not numbers or if the total is 0.

    Examples:
    --------
    >>> generate_pie_chart({"A": 40, "B": 30, "C": 20, "D": 10})
    'A | ****\nB | ***\nC | **\nD | *'

    >>> generate_pie_chart({"Apple": 50, "Banana": 30, "Cherry": 20})
    'Apple | *****\nBanana | ***\nCherry | **'
    """
    if not isinstance(data, dict):
        raise TypeError("Input must be a dictionary.")
    
    total = sum(data.values())
    if total == 0:
        raise ValueError("The total value of the data must be greater than 0.")
    
    chart = ""
    for category, value in data.items():
        if not isinstance(value, (int, float)):
            raise ValueError("All values in the dictionary must be numbers.")
        proportion = int((value / total) * 10)  # Scale the value for a simple pie chart
        chart += f"{category} | {'*' * proportion}\n"
    
    return chart


def plot_line_graph(data):
    """
    Produces a basic line graph in the terminal.

    Parameters:
    ----------
    data : list of int
        A list of numbers representing the data points to plot on the line graph.

    Returns:
    -------
    str
        A string representing the line graph.

    Raises:
    ------
    TypeError
        If the input is not a list of integers or floats.

    Examples:
    --------
    >>> plot_line_graph([5, 10, 15, 10, 5])
    '5 | *\n10 | **\n15 | ***\n10 | **\n5 | *'

    >>> plot_line_graph([1, 2, 3, 4, 5])
    '1 | *\n2 | **\n3 | ***\n4 | ****\n5 | *****'
    """
    if not isinstance(data, list) or not all(isinstance(i, (int, float)) for i in data):
        raise TypeError("Input must be a list of numbers (integers or floats).")
    
    chart = ""
    for value in data:
        bar = '*' * int(value)
        chart += f"{value} | {bar}\n"
    
    return chart


