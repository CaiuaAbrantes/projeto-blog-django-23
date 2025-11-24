from random import SystemRandom
import string
from django.utils.text import slugify

def random_latters(k=5):
    return ''.join(SystemRandom().choices(
        string.ascii_letters + string.digits,
        k=k
    ))
    
def slugify_new(text):
    return slugify(text) + '-' + random_latters()
