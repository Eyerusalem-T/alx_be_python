class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance  # Encapsulated attribute

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self._account_balance += amount

    def withdraw(self, amount):
        """Deduct the specified amount from the account balance if sufficient funds exist."""
        if 0 < amount <= self._account_balance:
            self._account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current account balance in a user-friendly format."""
        print(f"Current Balance: ${self._account_balance:.2f}")