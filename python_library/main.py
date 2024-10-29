"""
MAIN
"""

from python_library.my_tool import load
from python_library.my_tool import full_crudquery


def main():
    """Main function for the Transform-Load and CRUD Query script"""

    # transform and load
    load()

    # query
    full_crudquery()


if __name__ == "__main__":
    main()
