Class Product():
"""class product is defined	to get the information about products"""
	def __init__(self,ide,price,quantity):
		"""defining initial function"""
		self.ide = ide
		"""Gives the id"""
		self.price= price
		"""Gives the price of the product"""
		self.quantity = quantity
		"""Gives the number of items present of that product"""

	def remove(self,n):
		"""This function removes the item present"""
		if self.quantity>self.n:
			self.quantity=self.quantity-self.n
		else:
			print("Exceeds the limit of items present")

		"""In the above remove function, we take a variable n to remove from the quantity of particular item present. 
			If it exceeds number of items present then it prints the same"""

	def add(self,n):
		self.quantity=self.quantity+m

		"""In this function if we want to add more items to a particular product then we can do the same by adding them 
			quantity of the product"""