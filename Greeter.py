def greet_user(username): # function definition tell python the name and info for the function inside '()'
    """Display a simple  greeting.""" #doc strings are used in fuctions to describe what it does (needs 3 quotation marks)
    name = username
    print(f"\nHello, {name}")

greet_user('Trevor')