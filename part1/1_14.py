from operator import attrgetter

class User:
    def __init__(self, user_id):
        self.user_id = user_id
    def __repr__(self) -> str:
        return 'User({})'.format(self.user_id)

users = [User(1), User(-2), User(99)] 
sorted(users, key=lambda u: u.user_id) #[User(-2), User(1), User(99)]
sorted(users, key=attrgetter('user_id')) #[User(-2), User(1), User(99)]

min(users, key=attrgetter('user_id')) #User(-2)
max(users, key=attrgetter('user_id')) #User(99)