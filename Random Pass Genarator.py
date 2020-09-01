import random
import string

def random_password(length):
    password = string.ascii_letters + string.digits + string.punctuation
    result_str = ''.join(random.choice(password) for i in range(length))
    print("Random String is: ", result_str)

random_password(10)

