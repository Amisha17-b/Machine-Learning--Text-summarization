#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
# This line indicates that this script should be executed using the Python interpreter found in the environment's PATH.


import os
import sys


def main():
    """Run administrative tasks."""
    # Set the DJANGO_SETTINGS_MODULE environment variable to 'ts.settings'.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ts.settings')
    try:
         # Attempt to import execute_from_command_line function from django.core.management module.
        from django.core.management import execute_from_command_line
    except ImportError as exc:
         # If Django is not installed or not available on PYTHONPATH, raise ImportError.
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
     # Execute Django management commands from the command line arguments.
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # If this script is executed directly, call the main function.
    main()
