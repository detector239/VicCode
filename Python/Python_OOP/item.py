
class Item:
	pay_rate = 0.8 # this is for prices with discount 
	all = []
	def __init__(self, name: str, price: float, quantity=0):
		# Run validation for the recived arguments
		assert price >= 0, f"Price '{price}' is not greater or equal to zero!"
		assert quantity >= 0, f"Quantity '{quantity}' is not greater or equal to zero!"

		# Assign values to self object
		self.__name = name
		self.price = price
		self.quantity = quantity
		
		# Other action to execute
		print(f"ITEM {name} IS CREATED!\n")
		Item.all.append(self)
# If we want to use just the getter then we need to write just one '_' after 'self.'
	@property  # Getter
	def name(self):
		print(f"-You are trying to access the value of 'name' atribute from {self.__name}.")
		return self.__name

	@name.setter # Setter
	def name(self, value):
		print(f"--You are trying to change the value of 'name' atribute from {self.__name}.")
		if len(value) > 20:
			raise Exception("Your name is too long")
		else:
			self.__name = value
	
	def __repr__(self):
		return f"Class name:{self.__class__.__name__} with atributes:('{self.name}', {self.price}, {self.quantity})"

	def calculate_total_price(self):
		return self.price*self.quantity

	@classmethod # this line is used when we want the next function to be reachable only at class level like 'Item...'
	def print_all_items_instantiated(cls):
		text = f"{cls.all[0]}"
		for el in cls.all:
			if text != f"{el}":
				text = text + f", '{el}'"
		print(f"[{text}]")


	@staticmethod # this line is used when we want the next function to be like it was not in this class so no parameter 'self' or 'cls' needed
	def is_int_num(num):
		if isinstance(num, float):
			return num.is_integer()
		elif isinstance(num, int):
			return True
		else:
			return False

	def apply_discount(self):
		self.price = self.price * self.pay_rate


