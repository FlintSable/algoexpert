def add_prices(basket):
    total = 0
    for key in basket:
        total = total + basket[key]
        print(total)


groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, "coffee": 6.99, "milk": 3.99, "eggs": 2.98, "cheese": 5.44}
add_prices(groceries)