import string
import random

from ownerjobs.assets.assets_read import generate_random_string


def test_generate_random_string():
    length = 10
    result = generate_random_string(length)
    
    assert isinstance(result, str)
    assert len(result) == length
    assert all(c in string.ascii_letters for c in result)