"""
MAIN
"""

from python_library.transform_load import load
from python_library.crud_query import full_crudquery


def main():
    """Main function for the Transform-Load and CRUD Query script"""

    # transform and load
    load()

    # query
    full_crudquery()


if __name__ == "__main__":
    main()
