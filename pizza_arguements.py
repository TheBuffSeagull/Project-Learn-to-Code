def make_pizza(size, *toppings): # the "*"" next to toppings makes it into a tuple that will take any number of parameters
    """Summarize the pizza we are about to make"""
    print(f"\nMaking {size}-inch pizza with the folowing toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, 'pepperoni')
make_pizza(12 ,'mushrooms', 'green peppers', 'extra cheese')