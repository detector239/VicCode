from item import Item
from phone import Phone

# Creating items
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Mouse", 50, 5)
item3.pay_rate = 0.7 # pay_rate will find it in instance level so it won't take the value from Class level-0.8

# Applying disscount
item2.apply_discount()
print(item3.price)
item3.apply_discount()
print(item3.price)


# Calculating the total price
print(f"The total price of {item1.name} is {item1.calculate_total_price()}")
print(f"The total price of {item3.name} is {item3.calculate_total_price()}\n")


# Printing all the atributes from class and instance level 
print(f"All the atributes from the Item class are: {Item.__dict__}")
print(f"All the atributes from the item1 variable are: {item1.__dict__}")


# Prints the list 'all' from the class level
print(Item.all)
Item.print_all_items_instantiated()


# Using the staticmethod function
print(f"3.7 is integer: {Item.is_int_num(3.7)}")
print(f"10.0 is integer: {Item.is_int_num(10.0)}")


# Creating phones
phone1 = Phone("Phonev10", 500, 5, 1)
print(f"The total price for phone1 is {phone1.calculate_total_price()}")
phone2 = Phone("Phonev20", 700, 5, 1)


# Printing the list all from Phone and Item class
print(f"All the items are:\n{Item.all}")
print(f"All the phones are:\n{Phone.all}")