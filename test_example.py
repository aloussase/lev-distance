from lev import levenshtein_distance

def test_it_works():
    """Test that casa is similar to caca."""

    assert levenshtein_distance("casa", "caca") == 1
