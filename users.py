class User:
    def __init__(self, name, email_address):# now our method has 2 parameters/aka arguments!
        self.name = name			# and we use the values passed in to set the name attribute
        self.email = email_address		# and the email attribute
        self.account_balance = 0        # the account balance is set to $0, so no need for a third parameter

# adding the deposit method
    
    def make_deposit(self, amount):	# takes an argument that is the amount of the withdrawl
        self.account_balance += amount	# the specific user's account decreases by the amount of the value received
        return self # each function needs to be paired with a return statement
    
    def make_withdrawl(self, amount): # made a separate method to increase by the amount
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(self.name, self.account_balance)
        return self




guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
ali = User("Ali Tahir", "alitahir6001@gmail.com")  # these are all instances of the User Class.

print(guido.name)
print(monty.name)
print(ali.name)
print(guido.account_balance)

guido.make_deposit(5000).make_deposit(100).make_deposit(50).make_withdrawl(500).display_user_balance()
monty.make_deposit(1000000).make_deposit(0.50).make_withdrawl(500000).make_withdrawl(1).display_user_balance()
ali.make_deposit(500000).make_withdrawl(500).make_withdrawl(100).make_withdrawl(353.45).display_user_balance()

# I spent WAY too much time on this one assignment but after I asked for help I realized I was repeating attributes inside the functions that the console wasn't recognizing.