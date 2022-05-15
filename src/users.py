from main import MongoQuery


example_user = {
    "name": "Robert",
    "email": "roberts@email.com",
    "phone number": 7639405234,
    "account number": 1,
    "balance amount": 0.0,
}

example_user2 = {
    "name": "Mario",
    "email": "mario@outlook.com",
    "phone number": 9690405234,
    "account number": 2,
    "balance amount": 100,
}

example_user3 = {
    "name": "Louis",
    "email": "louis@outlook.com",
    "phone number": 96904012345,
    "account number": 3,
    "balance amount": 50,
}

example_user4 = {
    "name": "Mark",
    "email": "mark@gmail.com",
    "phone number": 96904012132,
    "account number": 4,
    "balance amount": 1000,
}

class UserQuery(object):
    def __init__(self) -> None:
        _MongoQuery = MongoQuery()
        self.db = _MongoQuery.connect_db("Test_Banking")
        self.users_collection = _MongoQuery.connect_collection(self.db, "users")

    
    def user_exists(self, name) -> int:
        if self.users_collection.count_documents({"name": name}, limit=1):
            return True
        return False

    def add_user(self, user_list) -> None:
        for user in user_list:
            if self.user_exists(user['name']):
                print(f"{user['name']} already exists , skipping insertion")
                continue
            print(f"inserting {user['name']}")
            result = self.users_collection.insert_one(user)
            print (f"{user['name']} --> {result}")

    def check_balance(self, account) -> float:
        user = account['name']
        if not self.user_exists(user):
            print(f"{user} does NOT exists in users collection.")
            return
        user = self.users_collection.find_one({"name": user})
        return user['balance amount']

    @staticmethod
    def print_something():
        print("something")



query = UserQuery()
# print (query.user_exists('Robert'))
# print (query.user_exists('sam'))
# query.add_user([example_user, example_user2, example_user3, example_user4])