import random
from ownerjobs.assets.assets_read import generate_random_email


def test_generate_random_email():
    result = generate_random_email()

    assert isinstance(result, str)
    assert "@" in result
    assert len(result) >= 6  # Minimum length of email
    assert len(result.split("@")[0]) >= 5  # Minimum length of username
    assert result.split("@")[1] in ['gmail.com', 'yahoo.com', 'hotmail.com', 'example.com']