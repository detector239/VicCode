from item import Item


class Phone(Item): # inheritance  # 'Phone' is a child class and 'Item' is parent class
	def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
		# Call super function to have all the atributes/methods from 'Item' class
		super().__init__(name, price, quantity)# this line calls the comand 'Item.all.append(self)' so no need to write it

		# Run validation for the recived arguments
		assert price >= 0, f"Price '{price}' is not greater or equal to zero!"
		assert quantity >= 0, f"Quantity '{quantity}' is not greater or equal to zero!"
		assert broken_phones >= 0, f"Broken_phones '{broken_phones}' is not greater or equal to zero!"

		# Assign values to self object
		self.name = name
		self.price = price
		self.quantity = quantity
		self.broken_phones = broken_phones
		
		# Other action to execute
		print(f"PHONE {name} IS CREATED!\n")




