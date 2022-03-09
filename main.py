from item import Item
from phone import Phone


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
