from mimetypes import init


class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1
        

user_1 = User("001", "Rolf Jahnel")
user_2 = User("002", "Susanne Jahnel")
user_2.follow(user_1)

print(f"User-ID: {user_1.user_id}")
print(f"Username: {user_1.username}")
print(f"Followers: {user_1.followers}")
print(f"Following: {user_1.following}")
print("." * 60)
print(f"User-ID: {user_2.user_id}")
print(f"Username: {user_2.username}")
print(f"Followers: {user_2.followers}")
print(f"Following: {user_2.following}")