def hasCapitalLetter(aString):
    for letter in aString:
        if letter.isupper():
            return True
    else:
        return False


def hasSmallLetter(aString):
    for letter in aString:
        if letter.islower():
            return True
    else:
        return False


def hasUnderscore(aString):
    if "_" in aString:
        return True
    else:
        return False


def hasWhiteSpace(aString):
    if " " in aString:
        return True
    else:
        return False


def hasPeriod(aString):
    if "." in aString:
        return True
    else:
        return False


def hasColon(aString):
    if ":" in aString:
        return True
    else:
        return False


def hasSemiColon(aString):
    if ";" in aString:
        return True
    else:
        return False


def hasComma(aString):
    if "," in aString:
        return True
    else:
        return False


def hasOperator(aString):
    operators = ["+", "-", "*", "/", "%"]
    for eachOperator in operators:
        if eachOperator in aString:
            return True
    else:
        return False


def hasNumber(aString):
    for letter in aString:
        if letter.isdigit():
            return True
    else:
        return False


def hasSymbol(aString):
    symbols = ["[", "@", "_", "!", "#", "$", "%", "^", "&", "*", "(", ")", "<", ">", "?", "/", "\\", "|", "}", "{", "~", ":", "]", "'", "\""]
    for eachSymbol in symbols:
        if eachSymbol in aString:
            return True
    else:
        return False


def hasElement(string, value):
    if value in string:
        return True
    else:
        return False
