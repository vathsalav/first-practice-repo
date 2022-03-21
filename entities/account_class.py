

class Account:
    def __init__(self, account_id, customer_id, balance: float):
        self.account_id = account_id
        self.customer_id = customer_id
        self.balance = balance

    def account_to_dictionary(self):
        return{
            "accountId": self.account_id,
            "customerId": self.customer_id,
            "balance": self.balance
        }

