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


# phone specific behavior or attributes
class Phone(Item):
	all = []

	def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
		# call to super function to have access to all attributes/ methods
		super(Phone, self).__init__(name, price, quantity)
		self.broken_phones = broken_phones
		Phone.all.append(self)

	def __repr__(self):
		return f"Phone('{self.name}', {self.price}, {self.quantity}, " \
			   f"{self.broken_phones})"


def main():
	# item1 = "Phone"
	# # all of these item1 attributes have item1 common,
	# # so we can create an oop
	# item1_price = 100
	# item1_quantity = 5
	# item1_price_total = item1_price * item1_quantity
	#
	# print(type(item1))
	# print(type(item1_price))
	# print(type(item1_quantity))
	# print(type(item1_price_total))
	#
	# # after oop
	# item2 = Item("Phone", 100, 5)
	# print(type(item2))
	# print(type(item2.name))
	# print(type(item2.price))
	# print(type(item2.quantity))
	# print(item2.calculate_total_price())
	#
	# item3 = Item("Laptop", 1000, 3)
	# print(type(item3))
	# print(type(item3.name))
	# print(type(item3.price))
	# print(type(item3.quantity))
	# print(item3.calculate_total_price())
	# item3.pay_rate = 0.7
	# print(item3.pay_rate)
	#
	# # you can also add more attributes to an already instantiated object
	# item2.has_numpad = False
	# print(item2.has_numpad)
	#
	# print(Item.__dict__)
	# print(item2.__dict__)
	# print(Item.all)
	# #for instance in Item.all:
	# #	print(instance.name)
	##################
	# print(Item.all)
	# Item.instantiate_from_csv()
	# print(Item.all)
	# phone1 = Item("jscPhonev10", 500, 5)
	# phone1.broken_phones = 1 # assigning values to instances manually not
	# good
	# phone2 = Item("jscPhonev20", 700, 5)
	# phone2.broken_phones = 1
	#########
	phone1 = Phone("jscPhonev10", 500, 5, 1)
	phone2 = Phone("jscPhonev20", 700, 5, 1)
	print(phone1)
	print(phone2)
	item5 = Item("item5", 300, 7)
	print(Item.all)
	print(Phone.all)
	print(phone1.calculate_total_price())


if __name__ == "__main__":
	main()
