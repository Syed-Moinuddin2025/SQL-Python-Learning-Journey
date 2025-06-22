# 🔐 Encapsulation Example - Password Protected Account

class UserAccount:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  # 🔒 private variable

    def get_password(self):
        return "❌ Access Denied: Password is private"

    def check_password(self, input_password):
        if input_password == self.__password:
            print("✅ Access granted!")
        else:
            print("❌ Wrong password!")

    def change_password(self, old_pass, new_pass):
        if old_pass == self.__password:
            self.__password = new_pass
            print("🔁 Password changed successfully!")
        else:
            print("❌ Current password is incorrect!")

# ✅ Create user account
user1 = UserAccount("Syed123", "mypassword")

# ❌ Direct access blocked
print(user1.get_password())

# 🔍 Check password
user1.check_password("wrongpass")
user1.check_password("mypassword")

# 🔁 Change password
user1.change_password("mypassword", "new123")

# ✅ Test with new password
user1.check_password("new123")
