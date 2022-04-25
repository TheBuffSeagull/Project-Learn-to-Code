from flask import current_app


current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1 # --> += is shorthand for current_number = current_number + 1