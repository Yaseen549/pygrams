# move the below to other functions
def charList(param):
    """returns all characters from a string of paragraph

    :param param:
    :return: list
    """
    a = param.replace(" ", "")
    return list(a)


def wordList(param):
    """Returns all the words as a list from a string of paragraph

    :param param:
    :return: list
    """
    return param.split(' ')


def joinList(list_of_words):
    """joins the list of words

    :param list_of_words:
    :return: list
    """
    return " ".join(list_of_words)

