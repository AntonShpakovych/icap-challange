import os
import uuid

from django.utils.text import slugify


def path_for_product_image(instance, filename):
    _, extension = os.path.splitext(filename)
    return os.path.join(
        "uploads/movies/",
        f"{slugify(instance.title)}-{uuid.uuid4()}{extension}"
    )
