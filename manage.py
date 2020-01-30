#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ascsite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


def save_pid():
    import os
    from CI.config import SETTINGS
    settings = SETTINGS()
    curr_process = os.getpid()
    f = open(settings.CURRPID_ADDRESS, "wt")
    f.write(str(curr_process))
    f.close()


if __name__ == '__main__':
    save_pid()
    main()
