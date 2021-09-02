import string

allowed_chars = string.ascii_lowercase + " "
password_database = {"usr": "super secure password"}

def check_password(user, guess):
    actual = password_database[user]
    return actual == guess

def main():
    user = "usr"
    guess = input("password: ")
    correct = check_password(user, guess)
    print(f'{guess} {correct}')

if __name__ == '__main__':
    main()