from lev import levenshtein_distance

def test_equal_strings():
    """Test that the distance between two equal strings is 0."""
    
    # Casos basicos
    assert levenshtein_distance("hello", "hello") == 0
    assert levenshtein_distance("world", "world") == 0
    assert levenshtein_distance("python", "python") == 0
    # Caso especial: cadenas vacias
    assert levenshtein_distance("", "") == 0
    
    # Cadenas largas
    assert levenshtein_distance("a" * 100, "a" * 100) == 0

    # Cadenas con caracteres especiales
    assert levenshtein_distance("café", "café") == 0
    assert levenshtein_distance("naïve", "naïve") == 0

    # Cadenas mixtas
    assert levenshtein_distance("Hello, World!", "Hello, World!") == 0

def test_equal_unicode_and_emojis():
    """Test equal strings with Unicode characters and emojis."""
    assert levenshtein_distance("😊🚀", "😊🚀") == 0
    assert levenshtein_distance("mañana", "mañana") == 0
    assert levenshtein_distance("straße", "straße") == 0
    assert levenshtein_distance("Good morning ☀️", "Good morning ☀️") == 0
