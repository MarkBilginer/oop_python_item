from item import Item
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