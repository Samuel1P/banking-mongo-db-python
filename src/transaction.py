from datetime import datetime
from main import MongoQuery
from users import UserQuery


Robert = {
    "name": "Robert",
    "email": "roberts@email.com",
    "phone number": 7639405234,
    "account number": 1,
    "balance amount": 12.0,
}

Mario = {
    "name": "Mario",
    "email": "mario@outlook.com",
    "phone number": 9690405234,
    "account number": 2,
    "balance amount": 100,
}

class TransactionQuery():
    def __init__(self) -> None:
        _MongoQuery = MongoQuery()
        self._UserQuery = UserQuery()
        self.db = _MongoQuery.connect_db("Test_Banking")
        self.users_collection = _MongoQuery.connect_collection(self.db, "users")
        self.transactions_collection = _MongoQuery.connect_collection(self.db, "transactions")

    def transfer_money(self, sender, receiver, amount):
        if not self._UserQuery.user_exists(sender):
            print(f"{sender} does NOT exists in users collection.")
            return
        if not self._UserQuery.user_exists(receiver):
            print(f"{receiver} does NOT exists in users collection.")
            return
        sender = self.users_collection.find_one({"name": sender})
        receiver = self.users_collection.find_one({"name": receiver})
        if sender['balance amount'] < amount:
            return False, "Not enough balance"
        result1 = self.users_collection.update_one({"name": sender['name']}, {'$inc': {'balance amount': -amount}})
        result2 = self.users_collection.update_one({"name": receiver['name']}, {'$inc': {'balance amount': amount}})
        print (result1, result2)
        return True, "TS-13678176"

    def generate_transaction_code(self, type):
        return type+"-"+datetime.utcnow().strftime("%Y%m%d%H%M%S")

transfer_query = TransactionQuery()
user_query = UserQuery()

print (user_query.check_balance({'name': 'Robert'}))

#print (Robert, Mario)

