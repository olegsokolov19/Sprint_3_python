import random
import string


def get_random_name(length=6):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))


def get_random_email():
    return 'olegsokolov02' + str(random.randint(100, 999)) + '@ya.ru'

def get_random_password(length=8):
    return ''.join(random.choice(string.ascii_letters) for i in range(1, length))
