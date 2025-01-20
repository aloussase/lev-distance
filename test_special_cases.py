from lev import levenshtein_distance


def test_empty_strings():
    """Test empty strings."""
    assert levenshtein_distance("", "") == 0
    assert levenshtein_distance("", "hello") == 5
    assert levenshtein_distance("world", "") == 5


def test_special_characters():
    """Test strings with special characters."""
    assert levenshtein_distance("café", "cafe") == 1
    assert levenshtein_distance("naïve", "naive") == 1
    assert levenshtein_distance("résumé", "resume") == 2


def test_case_sensitivity():
    """Test case sensitivity."""
    # 'P' -> 'p'
    assert levenshtein_distance("Python", "python") == 1

    # 'J' -> 'j' y 'S' -> 's'
    assert levenshtein_distance("JavaScript", "javascript") == 2

    # 'T' -> 't' y 'S' -> 's'
    assert levenshtein_distance("TypeScript", "typescript") == 2
