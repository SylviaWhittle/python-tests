import numpy as np
import timeit
import PasswordCheck
import random
import string
import itertools

allowed_chars = string.ascii_lowercase + " "

# Attempt a password
def try_password(user, attempt):
    return PasswordCheck.check_password(user, attempt)

# Create random string
def random_string(size):
    return ''.join(random.choices(allowed_chars, k=size))

def crack_length(user, max_len=32) -> int:
    trials = 1000
    times = np.empty(max_len)
    for i in range(max_len):
        # Use timeit for time taken
        # Take a sample by repeating 
        i_time = timeit.repeat(stmt='try_password(user, attempt)',
                                setup=f'user={user!r};attempt=random_string({i!r})',
                                globals=globals(),
                                number=trials,
                                repeat=10)
        # Store the shortest time out of the sample
        # this is to ensure that no random lag affects the longest response times.
        times[i] = min(i_time)


    most_likely_n = np.argsort(times)[::-1][:5]
    print(most_likely_n, times[most_likely_n] / times[most_likely_n[0]])

    most_likely = int(np.argmax(times))
    return most_likely

def crack_password(user, length):
    old_guess = random_string(length)
    counter = itertools.count()
    trials = 100
    while True:
        i = next(counter) % length
        for character in allowed_chars:
            new_guess = old_guess[:i] + character + old_guess[i+1:]

            # New guess
            new_time = timeit.repeat(stmt='try_password(user, attempt)',
                                        setup=f'user={user!r};attempt={new_guess!r}',
                                        globals=globals(),
                                        number=trials)
            # Old guess
            old_time = timeit.repeat(stmt='try_password(user, attempt)',
                                        setup=f'user={user!r};attempt={old_guess!r}',
                                        globals=globals(),
                                        number=trials)

            if try_password(user, new_guess):
                return new_guess

            if min(new_time) > min(old_time):
                old_guess = new_guess
                print(old_guess)

def main():
    #print(crack_length('usr'))
    print("Password: " + crack_password('usr', 21))

if __name__ == '__main__':
    main()