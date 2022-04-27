from setuptools import find_namespace_packages


def get_formatted_name(first_name, last_name, middle_name = ""):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("\nEnter 'q' at any time to quit.")
    f_name = input("First name:")
    if f_name == 'q':
        break
    l_name = input("Last name:")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")