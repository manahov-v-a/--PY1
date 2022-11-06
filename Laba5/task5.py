import random
import string


def get_random_password(equal=8) -> str:
    return ''.join(random.sample(string.ascii_letters + string.digits, equal))


print(get_random_password())
