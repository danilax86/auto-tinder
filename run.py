from tinder_bot import TinderBot
from user import User


def main():
    bot = TinderBot()
    user = User()
    bot.login(user.get_login(), user.get_password())
    bot.auto_swipe()

if __name__ == '__main__':
    main()
