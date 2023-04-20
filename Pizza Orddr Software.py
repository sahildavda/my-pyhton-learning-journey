Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Pizza Order Software

# Display available pizza options
print("Welcome to Pizza World!")
print("Our available pizza options are:")
print("1. Margherita - $10")
print("2. Pepperoni - $12")
print("3. Veggie - $11")
print("4. Hawaiian - $13")

... # Get user's pizza choice
... choice = int(input("Enter the number corresponding to your desired pizza: "))
... 
... # Initialize variables
... pizza = ""
... price = 0
... 
... # Determine pizza choice and set pizza and price accordingly
... if choice == 1:
...     pizza = "Margherita"
...     price = 10
... elif choice == 2:
...     pizza = "Pepperoni"
...     price = 12
... elif choice == 3:
...     pizza = "Veggie"
...     price = 11
... elif choice == 4:
...     pizza = "Hawaiian"
...     price = 13
... else:
...     print("Invalid choice. Exiting...")
...     exit()
... 
... # Get additional toppings
... toppings = input("Would you like to add any toppings? (comma-separated, e.g. mushrooms, onions, etc.): ")
... 
... # Calculate total price based on number of toppings
... if toppings:
...     toppings_list = toppings.split(", ")
...     num_toppings = len(toppings_list)
...     price += num_toppings * 1.5
... 
... # Display order summary
... print("Thank you for your order!")
... print("Your pizza: " + pizza)
... print("Toppings: " + toppings)
... print("Total price: $" + str(price))
