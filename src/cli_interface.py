from prompt_toolkit import prompt
from users import UserQuery as user


def main_prompt():
    user_name = prompt('User name:  ')
    if user().user_exists(user_name):
        print('Logged in: %s' % user_name)
    else:
        print("User does not existsa")




if __name__ == '__main__':
    main_prompt()