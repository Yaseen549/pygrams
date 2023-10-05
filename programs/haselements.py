def hasCapitalLetter(aString):
    """Checks if it has a Capital Letter

    :param aString:
    :return: bool
    """
    for letter in aString:
        if letter.isupper():
            return True
    else:
        return False


def hasSmallLetter(aString):
    """Checks if it has a Small Letter

    :param aString:
    :return: bool
    """
    for letter in aString:
        if letter.islower():
            return True
    else:
        return False


def hasUnderscore(aString):
    """Checks if it has an underscore (_)

    :param aString:
    :return: bool
    """
    if "_" in aString:
        return True
    else:
        return False


def hasWhiteSpace(aString):
    """Checks if it has a white space ( )

    :param aString:
    :return: bool
    """
    if " " in aString:
        return True
    else:
        return False


def hasPeriod(aString):
    """Checks if it has a period (.)

    :param aString:
    :return: bool
    """
    if "." in aString:
        return True
    else:
        return False


def hasColon(aString):
    """Checks if it has a colon (:)

    :param aString:
    :return: bool
    """
    if ":" in aString:
        return True
    else:
        return False


def hasSemiColon(aString):
    """Checks if it has a semi colon (;)

    :param aString:
    :return: bool
    """
    if ";" in aString:
        return True
    else:
        return False


def hasComma(aString):
    """Checks if it has a comma (,)

    :param aString:
    :return: bool
    """
    if "," in aString:
        return True
    else:
        return False


def hasOperator(aString):
    """Checks if it has any operator (+,-,/,*,%)

    :param aString:
    :return: bool
    """
    operators = ["+", "-", "*", "/", "%"]
    for eachOperator in operators:
        if eachOperator in aString:
            return True
    else:
        return False


def hasNumber(aString):
    """Checks if it has a number (digit/s)

    :param aString:
    :return: bool
    """
    for letter in aString:
        if letter.isdigit():
            return True
    else:
        return False


def hasSymbol(aString):
    """Checks if it has any special character

    :param aString:
    :return: bool
    """
    symbols = ["[", "@", "_", "!", "#", "$", "%", "^", "&", "*", "(", ")", "<", ">", "?", "/", "\\", "|", "}", "{", "~", ":", "]", "'", "\""]
    for eachSymbol in symbols:
        if eachSymbol in aString:
            return True
    else:
        return False


def hasElement(string, element):
    """Checks if it contains the given element in the string

    :param aString:
    :return: bool
    """
    if element in string:
        return True
    else:
        return False
