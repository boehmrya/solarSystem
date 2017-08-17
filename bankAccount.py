

class bankAccount:
	def __init__(self, ibalance, icustomerid):
		self.balance = ibalance
		self.customerid = icustid

	def checkBalance(self):
		return self.balance

	def deposit(self, amount):
		self.balance = self.balance + amount

	def withdraw(self, amount):
		self.balance = self.balance - amount

	def transfer(self, other, amount):
		self.balance = self.balance - amount
		other.balance = other.balance + amount

	# to string method
	def __str__(self):
		account = self.customerId + ": " + self.balance
		return account