
# Create a shopping cart programme that will continuously ask the user for the food product and the price of the product.
# Have an exit clause if the user wishes to stop adding more to their cart.
# At the end show the food items and the total cost to the user.

foods = []
prices = []
total = 0

while True:
    food = input("Enter the food to buy or press q to exit: ")
    if food.lower() == 'q':  # Fix: call lower()
        break
    else:
        price = float(input(f"Enter the price of {food}: R"))
        foods.append(food)
        prices.append(price)  # Fix: append price, not prices

print("-----YOUR CART----")  

for food in foods:
    print(food)

total = 0
for price in prices:
    total += price

print(f"\nYour Total is: R{total}")