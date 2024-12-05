def char_list(param):
    """Returns all characters from a string of paragraph (excluding spaces)

    :param param: str - The input string
    :return: list - A list of characters excluding spaces
    """
    return list(param.replace(" ", ""))


def word_list(param):
    """Returns all the words as a list from a string of paragraph

    :param param: str - The input string
    :return: list - A list of words from the paragraph
    """
    return param.split(' ')


def join_list(list_of_words):
    """Joins the list of words into a single string

    :param list_of_words: list - List of words
    :return: str - A single string with words joined by space
    """
    return " ".join(list_of_words)
