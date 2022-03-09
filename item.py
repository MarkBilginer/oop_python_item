import csv


class Item:
	pay_rate = 0.8  # class attribute, the pay rate after %20 discount
	all = []

	# magic method
	# called automatically
	# quantity = 0 the default value marks this already as an integer
	def __init__(self, name: str, price: float, quantity=0):
		# Run validations to the received arguments
		# assert helps us catch bugs early on
		assert price >= 0, f"Price {price} is not greater than zero!"
		assert quantity >= 0, f"Quantity {quantity} is not greater than zero!"

		# Assign to self object
		print(f"I am created: {name}")
		self.name = name
		self.price = price
		self.quantity = quantity
		# self.price_total = self.price * self.quantity # created a function
		# instead
		# Actions to execute
		Item.all.append(self)

	def calculate_total_price(self) -> int:
		return self.price * self.quantity

	# self gives the object context to the method
	def apply_discount(self):
		# Item.pay_rate keeps being 0.8, even if we change it
		# after object creation, cause it refers to the class attribute
		# self.price = self.price * Item.pay_rate
		# if we change pay_rate with assignment
		# then this gets changed as well since it is instance.
		self.price = self.price * self.pay_rate

	# class method gives the class context to the method
	@classmethod
	def instantiate_from_csv(cls):
		with open("./item.csv", "r") as csv_file:
			csv_reader = csv.DictReader(csv_file)
			line_count = 0
			for row in csv_reader:
				# the init method gets called, remember
				Item(
					name=row["name"],
					price=float(row["price"]),
					quantity=int(row["quantity"])
				)

	# static method doesnt give any context to the function
	@staticmethod
	def is_integer(num):
		# We will count out the floats that are point zero
		# For i.e 5.0, 10.0
		if isinstance(num, float):
			return num.is_integer()
		elif isinstance(num, int):
			return True
		else:
			return False

	# control how to show object, when printed
	def __repr__(self):
		return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"