Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Welcome to the Tip Calculator!")
... bill = float(input("What was the total bill? "))
... tip = int(input("What percentage tip would you like to give ? 12, 15, 18 or 20 ? " ))
... people = int(input("How many people would split the bill ? "))
... billwithtip = tip / 100 * bill + bill
... print("Total payable amount is ", billwithtip)
... tipaspercent = tip/100 
... totaltip = tipaspercent*bill
... totalbill = bill+totaltip
... billperperson = totalbill/people
... finalamt=round(billperperson, 2)
... print(f"Each person should pay {finalamt} ")
