from lev import levenshtein_distance

def test_adding_one_character():
    """Test strings where one character is added."""
    assert levenshtein_distance("hola", "holas") == 1
    assert levenshtein_distance("test", "tests") == 1
    assert levenshtein_distance("run", "runs") == 1

def test_removing_one_character():
    """Test strings where one character is removed."""
    assert levenshtein_distance("tests", "test") == 1
    assert levenshtein_distance("python", "pytho") == 1
    assert levenshtein_distance("hello", "hell") == 1

def test_different_lengths():
    """Test strings with bigger length differences."""
    assert levenshtein_distance("python", "py") == 4
    assert levenshtein_distance("hello", "hi") == 4
    assert levenshtein_distance("typescript", "type") == 6

def test_completely_different_lengths():
    """Test strings with very different lengths."""
    assert levenshtein_distance("programming", "code") == 10
    assert levenshtein_distance("javascript", "java") == 6
    assert levenshtein_distance("development", "dev") == 8

def test_complex_transformations():
    """Test strings requiring multiple complex transformations."""
    # Reordering characters
    assert levenshtein_distance("algoritmo", "logaritmo") == 3
    # Multiple operations needed
    assert levenshtein_distance("desarrollo", "dessarollo") == 2
    assert levenshtein_distance("inteligencia", "inteligente") == 3

def test_repeated_patterns():
    """Test strings with repeated patterns."""
    assert levenshtein_distance("programaprograma", "programador") == 6
    assert levenshtein_distance("testtesttest", "test") == 8
    assert levenshtein_distance("pythonpython", "pythonjava") == 6

def test_edge_cases():
    """Test edge cases with special patterns."""
    # Same characters but different order
    assert levenshtein_distance("amor", "roma") == 4
    # Palindrome vs normal
    assert levenshtein_distance("reconocer", "conocer") == 2
    # Repeated characters
    assert levenshtein_distance("mississippi", "missouri") == 6
