import string
import random

def random_name(length: int) ->str:
    return ''.join([random.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(length)])


def random_age(a, b):
    return random.randint(a, b)