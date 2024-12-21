import socket
import platform
import subprocess
import socket

def get_ip_address():
    """
    Gets the current IP address of the machine.

    Returns:
    -------
    str
        The current IP address.

    Raises:
    ------
    OSError
        If the IP address cannot be determined.

    Examples:
    --------
    >>> get_ip_address()
    '192.168.1.10'
    """
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except Exception as e:
        raise OSError(f"Unable to get IP address: {e}")


def ping_host(host):
    """
    Pings a host to check its availability.

    Parameters:
    ----------
    host : str
        The hostname or IP address of the host to ping.

    Returns:
    -------
    bool
        True if the host is reachable, False otherwise.

    Examples:
    --------
    >>> ping_host("google.com")
    True
    >>> ping_host("unknownhost")
    False
    """
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]
    try:
        return subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0
    except Exception:
        return False


def check_port_open(host, port):
    """
    Check if a specific port is open on a host.

    Parameters:
    ----------
    host : str
        The host address (e.g., '127.0.0.1' or 'example.com').
    port : int
        The port number to check.

    Returns:
    -------
    bool
        True if the port is open, False otherwise.

    Examples:
    --------
    >>> check_port_open('localhost', 80)
    True
    >>> check_port_open('example.com', 8080)
    False
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # 1 second timeout
            result = s.connect_ex((host, port))  # Returns 0 if connection successful
            return result == 0
    except socket.error:
        return False