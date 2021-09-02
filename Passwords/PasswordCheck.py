# Super secure server 


password_database = {"usr": "super secure password"}

def check_password(user, guess):
    actual = password_database[user]
    if(len(guess) != len(actual)):
        return False

    for i in range(len(actual)):
        if guess[i] != actual[i]:
            return False
    return True
