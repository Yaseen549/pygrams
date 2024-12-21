import os
import shutil
import json

def read_file(file_path):
    """
    Reads the content of a file.

    Parameters:
    ----------
    file_path : str
        The path to the file to read.

    Returns:
    -------
    str
        The content of the file.

    Raises:
    ------
    FileNotFoundError
        If the file does not exist.
    IOError
        If an error occurs during file reading.

    Examples:
    --------
    >>> read_file("example.txt")
    'Hello, World!'
    """
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string.")
    
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {file_path} does not exist.")
    except IOError as e:
        raise IOError(f"An error occurred while reading the file: {e}")


def write_file(file_path, content):
    """
    Writes content to a file.

    Parameters:
    ----------
    file_path : str
        The path to the file to write to.
    content : str
        The content to write to the file.

    Raises:
    ------
    TypeError
        If content is not a string.
    IOError
        If an error occurs during file writing.

    Examples:
    --------
    >>> write_file("example.txt", "Hello, World!")
    None
    """
    if not isinstance(file_path, str) or not isinstance(content, str):
        raise TypeError("Both file_path and content must be strings.")
    
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except IOError as e:
        raise IOError(f"An error occurred while writing to the file: {e}")


def list_files_in_directory(directory_path):
    """
    Lists all files in a directory.

    Parameters:
    ----------
    directory_path : str
        The path to the directory.

    Returns:
    -------
    list
        A list of file names in the directory.

    Raises:
    ------
    FileNotFoundError
        If the directory does not exist.
    NotADirectoryError
        If the specified path is not a directory.

    Examples:
    --------
    >>> list_files_in_directory("/path/to/directory")
    ['file1.txt', 'file2.jpg']
    """
    if not isinstance(directory_path, str):
        raise TypeError("directory_path must be a string.")
    
    try:
        if not os.path.isdir(directory_path):
            raise NotADirectoryError(f"{directory_path} is not a directory.")
        return os.listdir(directory_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"The directory at {directory_path} does not exist.")
    except NotADirectoryError as e:
        raise NotADirectoryError(f"Error: {e}")


def delete_file(file_path):
    """
    Deletes a specified file.

    Parameters:
    ----------
    file_path : str
        The path to the file to delete.

    Raises:
    ------
    FileNotFoundError
        If the file does not exist.
    IOError
        If an error occurs during file deletion.

    Examples:
    --------
    >>> delete_file("example.txt")
    None
    """
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string.")
    
    try:
        os.remove(file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {file_path} does not exist.")
    except IOError as e:
        raise IOError(f"An error occurred while deleting the file: {e}")


def get_file_size(file_path):
    """
    Returns the size of a file in bytes.

    Parameters:
    ----------
    file_path : str
        The path to the file.

    Returns:
    -------
    int
        The size of the file in bytes.

    Raises:
    ------
    FileNotFoundError
        If the file does not exist.
    TypeError
        If the input is not a string.

    Examples:
    --------
    >>> get_file_size("example.txt")
    1024

    >>> get_file_size("image.jpg")
    204800
    """
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string.")
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file at {file_path} does not exist.")
    
    return os.path.getsize(file_path)


def get_file_lines(file_path):
    """
    Reads and returns all the lines in a file.

    Parameters:
    ----------
    file_path : str
        The path to the file.

    Returns:
    -------
    list of str
        A list of lines in the file.

    Raises:
    ------
    FileNotFoundError
        If the file does not exist.
    TypeError
        If the input is not a string.

    Examples:
    --------
    >>> get_file_lines("example.txt")
    ['Hello, world!', 'This is a file.']

    >>> get_file_lines("data.txt")
    ['Line 1', 'Line 2', 'Line 3']
    """
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string.")
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file at {file_path} does not exist.")
    
    with open(file_path, 'r') as file:
        return file.readlines()


def rename_file(file_path, new_name):
    """
    Renames a file to a new name.

    Parameters:
    ----------
    file_path : str
        The current path of the file to be renamed.
    new_name : str
        The new name for the file.

    Returns:
    -------
    None

    Raises:
    ------
    FileNotFoundError
        If the file does not exist.
    TypeError
        If the input is not a string.

    Examples:
    --------
    >>> rename_file("old_name.txt", "new_name.txt")
    Renames the file from old_name.txt to new_name.txt
    """
    if not isinstance(file_path, str) or not isinstance(new_name, str):
        raise TypeError("Both file path and new name must be strings.")
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file at {file_path} does not exist.")
    
    os.rename(file_path, new_name)


def copy_file(source_path, destination_path):
    """
    Copies a file from one location to another.

    Parameters:
    ----------
    source_path : str
        The path to the source file.
    destination_path : str
        The path to the destination file.

    Returns:
    -------
    None

    Raises:
    ------
    FileNotFoundError
        If the source file does not exist.
    TypeError
        If the input is not a string.

    Examples:
    --------
    >>> copy_file("source.txt", "destination.txt")
    Copies source.txt to destination.txt

    >>> copy_file("image.jpg", "backup_image.jpg")
    Copies image.jpg to backup_image.jpg
    """
    if not isinstance(source_path, str) or not isinstance(destination_path, str):
        raise TypeError("Both source path and destination path must be strings.")
    
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"The source file at {source_path} does not exist.")
    
    shutil.copy(source_path, destination_path)


def get_file_extension(filename):
    """
    Get the extension of a file based on its name.

    Parameters:
    ----------
    filename : str
        The name of the file, including the extension.

    Returns:
    -------
    str
        The file extension, including the dot (e.g., '.txt', '.py').

    Examples:
    --------
    >>> get_file_extension('example.txt')
    '.txt'
    >>> get_file_extension('image.png')
    '.png'
    """
    return os.path.splitext(filename)[1]


def read_json_file(filepath):
    """
    Parse and read a JSON file.

    Parameters:
    ----------
    filepath : str
        The path to the JSON file.

    Returns:
    -------
    dict
        The parsed JSON data as a Python dictionary.

    Raises:
    ------
    FileNotFoundError
        If the specified file does not exist.
    JSONDecodeError
        If the file is not a valid JSON file.

    Examples:
    --------
    >>> read_json_file('data.json')
    {'name': 'Alice', 'age': 30}
    """
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{filepath}' does not exist.")
    except json.JSONDecodeError:
        raise ValueError(f"The file '{filepath}' is not a valid JSON file.")
    

def write_json_file(filepath, data):
    """
    Write data to a JSON file.

    Parameters:
    ----------
    filepath : str
        The path to the JSON file where data will be written.
    data : dict
        The data to be written to the file (should be serializable to JSON).

    Returns:
    -------
    None

    Examples:
    --------
    >>> write_json_file('output.json', {'name': 'Bob', 'age': 25})
    """
    try:
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)
    except TypeError:
        raise ValueError("The data is not serializable to JSON.")
    
