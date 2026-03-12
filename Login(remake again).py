class User:
    def __init__(self, first_name, last_name, username, location, age):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.location = location
        self.age = age
    
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1 

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User("Anila", "Raelynn", "raenilaa2", "Pekanbaru", 19)

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print(f"Jumlah login attempts setelah 3 kali increment: {user1.login_attempts}")

user1.reset_login_attempts()
print(f"Jumlah login attempts setelah di-reset: {user1.login_attempts}")