from flask import current_app


current_number = 0
while current_number < 10:
    current_number += 1 # --> += is shorthand for current_number = current_number + 1
    if current_number % 2 == 0:
        continue

    print(current_number)
