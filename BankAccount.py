class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name = name
  def __repr__(self):
    return "Name: %s, Balance: %s" % (str(self.name), str(self.balance))
  def show_balance(self):
    print "Balance: %s" % (self.balance)
  def deposit(self, amount):
    if amount <= 0:
      print "Error"
      return
    else:
      print "Balance %s. Deposit %s" % (self.balance, amount)
      self.balance += amount
      self.show_balance()
  def withdraw(self, amount):
    if amount > self.balance:
      print "Error"
      return
    else:
      print "Balance %s. Withdraw %s" % (self.balance, amount)
      self.balance -= amount
      self.show_balance()


my_account = BankAccount("Ana's")
print my_account
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print my_account
