class User:
    login: str = ""
    password: str = ""

    def __init__(self):
        self.set_login()
        self.set_password()

    def get_login(self) -> str:
        return self.login

    def get_password(self) -> str:
        return self.password

    def set_login(self):
        self.login = str(input("Provide your gmail login: "))

    def set_password(self):
        self.password = str(input("Provide your password: "))
