Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Welcome to the rollercoaster!")
... name = input("What is your name? ")
... height = int(input("What is your height in cm? "))
... bill = 0
... 
... if height >= 120:
...     print("Hey " + name + ", you can ride the roller coaster!")
...     age = int(input("What is your age? "))
...   
...     if age < 12:
...         bill = 5
...         print("Child tickets are $5.")
...   
...     elif age <= 18:
...         bill = 7
...         print("Youth tickets are $7.")
...     elif age >= 45 and age <=55:
...       print("Everything is going to be ok, Have a free ride on us!")
...   
...   
...     else:
...         bill = 12 
...         print("Adult tickets are $12.")
...         photo = input("Do you want a photo to save this memory for just $3? Yes/No ")
...    
...         if photo.lower() == "yes":
...             bill += 3 
...             print(f"Your final bill with a photo is ${bill}.")
...         else:
...             print(f"Your final bill is ${bill}.") 
...   
... else:
