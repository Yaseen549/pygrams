import re

def count_sentences(text):
    """
    Count the number of sentences in a given text.

    Parameters:
    ----------
    text : str
        The input string to count sentences in.

    Returns:
    -------
    int
        The number of sentences in the text.

    Examples:
    --------
    >>> count_sentences("This is a sentence. This is another sentence!")
    2
    >>> count_sentences("How are you? I'm good.")
    2
    """
    # Regular expression to match sentence-ending punctuation marks (.!?)
    sentence_endings = re.compile(r'[.!?]')
    sentences = sentence_endings.split(text)
    
    # Filter out empty sentences caused by split (if any)
    return len([s for s in sentences if s.strip()])


def find_longest_word(text):
    """
    Find the longest word in a given string.

    Parameters:
    ----------
    text : str
        The input string to find the longest word in.

    Returns:
    -------
    str
        The longest word in the string.

    Examples:
    --------
    >>> find_longest_word("I love programming in Python")
    'programming'
    >>> find_longest_word("The quick brown fox jumps over the lazy dog")
    'quick'
    """
    # Split the text into words and find the longest one
    words = text.split()
    longest_word = max(words, key=len)
    return longest_word

