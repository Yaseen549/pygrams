def reverse_string(s):
    """
    Reverses the given string.

    Parameters:
    ----------
    s : str
        The string to be reversed.

    Returns:
    -------
    str
        The reversed string.

    Examples:
    --------
    >>> reverse_string("hello")
    'olleh'
    >>> reverse_string("Python")
    'nohtyP'
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")
    return s[::-1]


def reverse_words(sentence):
    """
    Reverses the words in a sentence.

    Parameters:
    ----------
    sentence : str
        The sentence whose words will be reversed.

    Returns:
    -------
    str
        The sentence with words reversed.

    Raises:
    ------
    TypeError
        If the input is not a string.

    Examples:
    --------
    >>> reverse_words("Hello World")
    'World Hello'

    >>> reverse_words("Python is fun")
    'fun is Python'
    """
    if not isinstance(sentence, str):
        raise TypeError("The input must be a string.")
    
    # Split the sentence into words, reverse the list, and join them back into a string
    return ' '.join(sentence.split()[::-1])


def capitalize_each_word(sentence):
    """
    Capitalizes the first letter of each word in a sentence.

    Parameters:
    ----------
    sentence : str
        The sentence in which each word's first letter will be capitalized.

    Returns:
    -------
    str
        The sentence with the first letter of each word capitalized.

    Raises:
    ------
    TypeError
        If the input is not a string.

    Examples:
    --------
    >>> capitalize_each_word("hello world")
    'Hello World'

    >>> capitalize_each_word("python is fun")
    'Python Is Fun'
    """
    if not isinstance(sentence, str):
        raise TypeError("The input must be a string.")
    
    # Split the sentence into words, capitalize each word, and join them back into a sentence
    return ' '.join(word.capitalize() for word in sentence.split())


def count_vowels_and_consonants(string):
    """
    Counts the vowels and consonants in a string.

    Parameters:
    ----------
    string : str
        The string to count vowels and consonants in.

    Returns:
    -------
    tuple
        A tuple (vowel_count, consonant_count) containing the counts of vowels and consonants.

    Raises:
    ------
    TypeError
        If the input is not a string.

    Examples:
    --------
    >>> count_vowels_and_consonants("Hello World")
    (3, 7)

    >>> count_vowels_and_consonants("Python is fun")
    (4, 8)
    """
    if not isinstance(string, str):
        raise TypeError("The input must be a string.")
    
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    
    for char in string:
        if char.isalpha():  # Ignore non-alphabet characters
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return vowel_count, consonant_count


def count_words(text):
    """
    Returns the count of words in a string.

    Parameters:
    ----------
    text : str
        A string to count words.

    Returns:
    -------
    int
        The number of words in the string.

    Raises:
    ------
    TypeError
        If the input is not a string.

    Examples:
    --------
    >>> count_words("Hello World")
    2

    >>> count_words("Python is awesome")
    3
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    
    words = text.split()
    return len(words)


def count_letters(text):
    """
    Returns the count of letters in a string.

    Parameters:
    ----------
    text : str
        A string to count letters.

    Returns:
    -------
    int
        The number of letters in the string.

    Raises:
    ------
    TypeError
        If the input is not a string.

    Examples:
    --------
    >>> count_letters("Hello World")
    10

    >>> count_letters("Python 3.8 is awesome!")
    17
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    
    return sum(1 for char in text if char.isalpha())


def count_sentences(text):
    """
    Returns the count of sentences in a string.

    Parameters:
    ----------
    text : str
        A string to count sentences.

    Returns:
    -------
    int
        The number of sentences in the string.

    Raises:
    ------
    TypeError
        If the input is not a string.

    Examples:
    --------
    >>> count_sentences("Hello World. Python is awesome!")
    2

    >>> count_sentences("This is sentence one. Here's sentence two!")
    2
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    
    return sum(1 for char in text if char in '.!?')


def find_longest_word(sentence):
    """
    Finds the longest word in a sentence.

    Parameters:
    ----------
    sentence : str
        A sentence to find the longest word.

    Returns:
    -------
    str
        The longest word in the sentence.

    Raises:
    ------
    TypeError
        If the input is not a string.

    Examples:
    --------
    >>> find_longest_word("The quick brown fox jumped over the lazy dog")
    'jumped'

    >>> find_longest_word("Python is awesome")
    'awesome'
    """
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string.")
    
    words = sentence.split()
    longest = max(words, key=len)
    return longest


def find_shortest_word(sentence):
    """
    Finds the shortest word in a sentence.

    Parameters:
    ----------
    sentence : str
        A sentence to find the shortest word.

    Returns:
    -------
    str
        The shortest word in the sentence.

    Raises:
    ------
    TypeError
        If the input is not a string.

    Examples:
    --------
    >>> find_shortest_word("The quick brown fox jumped over the lazy dog")
    'The'

    >>> find_shortest_word("Python is awesome")
    'is'
    """
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string.")
    
    words = sentence.split()
    shortest = min(words, key=len)
    return shortest


def remove_duplicates(string):
    """
    Removes duplicate characters from a string.

    Parameters:
    ----------
    string : str
        A string to remove duplicates.

    Returns:
    -------
    str
        A string with duplicates removed.

    Raises:
    ------
    TypeError
        If the input is not a string.

    Examples:
    --------
    >>> remove_duplicates("hello")
    'helo'

    >>> remove_duplicates("Python programming")
    'Python rgam'
    """
    if not isinstance(string, str):
        raise TypeError("Input must be a string.")
    
    return "".join(sorted(set(string), key=string.index))
