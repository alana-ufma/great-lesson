import hashlib
import string
import random

def random_key(size=5):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for x in range(size))

def generate_hash_key(salt, random_str_size=5):
    random_str = random_key(random_str_size)
    text = random_str + salt
    return hashlib.sha224(text.encode('utf-8')).hexdigest()


#
# def unique_slug_generator(model_instance, title, slug_field):
#     """
#     :param model_instance:
#     :param title:
#     :param slug_field:
#     :return:
#     """
#     slug = slugify(title)
#     model_class = model_instance.__class__
#
#     while model_class._default_manager.filter(slug=slug).exists():
#         object_pk = model_class._default_manager.latest('pk')
#         object_pk = object_pk.pk + 1
#
#         slug = f'{slug}-{object_pk}'
#
#     return slug
