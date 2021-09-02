# Super secure server 


password_database = {"usr": "super secure password two electric boogaloo"}

def check_password(user, guess):
    actual = password_database[user]

    if(len(guess) != len(actual)):
        return False

    for i in range(len(actual)):
        if guess[i] != actual[i]:
            return False
    return True

if __name__ == '__main__':
    while(True):
        if check_password('usr', input('user >> password: ')):
            print('Logged in')
            break
        else:
            print('Access denied')
        