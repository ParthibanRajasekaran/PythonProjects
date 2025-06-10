class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        print("Welcome to the Quiz!")

    def follow(self, user):
        self.following += 1
        user.followers += 1


user_1 = User("001", "parth")
user_2 = User("002", "anushka")

user_1.follow(user_2)

print(user_1.following)
print(user_1.followers)
print(user_2.followers)
print(user_2.following)